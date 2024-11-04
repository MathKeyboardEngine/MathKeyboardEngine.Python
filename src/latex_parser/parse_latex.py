from typing import List, Union

from src import AscendingBranchingNode, DecimalSeparatorNode, DescendingBranchingNode, DigitNode, KeyboardMemory, MatrixNode, RoundBracketsNode, StandardBranchingNode, StandardLeafNode, insert, insert_with_encapsulate_current, move_right
from src._helpers.coalesce import coalesce
from src._helpers.first_or_none import first_or_none
from src.latex_parser._helpers.get_bracket_pair_content import get_bracket_pair_content
from src.latex_parser.LatexParserConfiguration import LatexParserConfiguration


def parse_latex(latex : Union[str, None], latexparserconfiguration : Union[LatexParserConfiguration, None] = None) -> KeyboardMemory:
        if latexparserconfiguration is None:
            latexparserconfiguration = LatexParserConfiguration()
        if latex is None:
            return KeyboardMemory()
        x = latex.strip()
        k = KeyboardMemory()
        while x != '':
            if x[0] == ' ':
                x = x.lstrip()
                continue

            decimal_separator_match = first_or_none(lambda pattern: x.startswith(pattern), latexparserconfiguration.decimal_separator_matchers)
            if decimal_separator_match is not None:
                insert(k, DecimalSeparatorNode(coalesce(latexparserconfiguration.preferred_decimal_separator, decimal_separator_match)))
                x = x[len(decimal_separator_match):]
                continue

            if x[0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or (latexparserconfiguration.additional_digits is not None and x[0] in latexparserconfiguration.additional_digits):
                insert(k, DigitNode(str(x[0])))
                x = x[1:]
                continue

            handled = False

            if x.startswith(r'\begin{'):
                matrix_type_and_rest = get_bracket_pair_content(x, r'\begin{', '}')
                if not matrix_type_and_rest.content.endswith('matrix') and not matrix_type_and_rest.content.endswith('cases'):
                    raise Exception(r'Expected a word ending with "matrix" or "cases" after "\begin{".')
                matrix_content = matrix_type_and_rest.rest[:matrix_type_and_rest.rest.index(r'\end{' + matrix_type_and_rest.content + '}')]
                lines = matrix_content.split('\\\\')
                insert(k, MatrixNode(matrix_type_and_rest.content, len(lines[0].split('&')), len(lines)))
                for line in lines:
                    for elementlatex in line.split('&'):
                        nodes = parse_latex(elementlatex, latexparserconfiguration).syntax_tree_root.nodes
                        insert(k, nodes)
                        move_right(k)
                matrix_end = r'\end{' + matrix_type_and_rest.content + '}'
                x = x[(x.index(matrix_end) + len(matrix_end)):]
                continue

            if latexparserconfiguration.prefer_roundbracketsnode and (x[0] == '(' or x.startswith(r'\left(')):
                opening = '(' if x[0] == '(' else r'\left('
                closing = ')' if x[0] == '(' else r'\right)'
                bracketsnode = RoundBracketsNode(opening, closing)
                insert(k, bracketsnode)
                brackets_content_and_rest = get_bracket_pair_content(x, opening, closing)
                brackets_content_nodes = parse_latex(brackets_content_and_rest.content, latexparserconfiguration).syntax_tree_root.nodes
                insert(k, brackets_content_nodes)
                k.current = bracketsnode
                x = brackets_content_and_rest.rest
                continue

            if x.startswith('\\'):
                for prefix in ['\\left\\', '\\right\\', r'\left', r'\right']:
                    if x.startswith(prefix) and not x[len(prefix)].isalpha():
                        insert(k, StandardLeafNode(prefix + x[len(prefix)]))
                        x = x[(len(prefix) + 1):]
                        handled = True
                        break
                if handled:
                    continue

                text_opening = r'\text{'
                if x.startswith(text_opening):
                    bracket_pair_content_and_rest = get_bracket_pair_content(x, text_opening, '}')
                    textnode = StandardBranchingNode(text_opening, '}')
                    insert(k, textnode)
                    for character in bracket_pair_content_and_rest.content:
                        insert(k, StandardLeafNode(str(character)))
                    k.current = textnode
                    x = bracket_pair_content_and_rest.rest
                    continue

                command = '\\'
                if x[1].isalpha():
                    for i in range(1, len(x)):
                        character = x[i]
                        if character.isalpha():
                            command += character
                        elif character == '{' or character == '[':
                            opening = command + character
                            closing_bracket_1 = '}' if character == '{' else ']'
                            bracket_pair_1_content_and_rest = get_bracket_pair_content(x, opening, closing_bracket_1)
                            placeholder_1_nodes = parse_latex(bracket_pair_1_content_and_rest.content, latexparserconfiguration).syntax_tree_root.nodes
                            if len(bracket_pair_1_content_and_rest.rest) > 0 and bracket_pair_1_content_and_rest.rest[0] == '{':
                                multi_placeholder_branchingnode = DescendingBranchingNode(opening, closing_bracket_1 + '{', '}')
                                insert(k, multi_placeholder_branchingnode)
                                insert(k, placeholder_1_nodes)
                                move_right(k)
                                bracket_pair_2_content_and_rest = get_bracket_pair_content(bracket_pair_1_content_and_rest.rest, '{', '}')
                                placeholder_2_nodes = parse_latex(bracket_pair_2_content_and_rest.content, latexparserconfiguration).syntax_tree_root.nodes
                                insert(k, placeholder_2_nodes)
                                k.current = multi_placeholder_branchingnode
                                x = bracket_pair_2_content_and_rest.rest
                            else:
                                single_placeholder_branchingnode = StandardBranchingNode(opening, str(closing_bracket_1))
                                insert(k, single_placeholder_branchingnode)
                                insert(k, placeholder_1_nodes)
                                k.current = single_placeholder_branchingnode
                                x = bracket_pair_1_content_and_rest.rest
                            handled = True
                            break
                        else:
                            break
                    if handled:
                        continue
                    insert(k, StandardLeafNode(command))
                    x = x[len(command):]
                else:
                    insert(k, StandardLeafNode('\\' + x[1]))
                    x = x[2:]
                continue

            if x.startswith('_{'):
                opening = '_{'
                closing_bracket_1 = '}'
                bracket_pair_1_content_and_rest = get_bracket_pair_content(x, opening, closing_bracket_1)
                if bracket_pair_1_content_and_rest.rest.startswith('^{'):
                    ascendingbranchingnode = AscendingBranchingNode(opening, '}^{', '}')
                    insert(k, ascendingbranchingnode)
                    placeholder_1_nodes = parse_latex(bracket_pair_1_content_and_rest.content, latexparserconfiguration).syntax_tree_root.nodes
                    insert(k, placeholder_1_nodes)
                    move_right(k)
                    bracket_pair_2_content_and_rest = get_bracket_pair_content(bracket_pair_1_content_and_rest.rest, '^{', '}')
                    placeholder_2_nodes = parse_latex(bracket_pair_2_content_and_rest.content, latexparserconfiguration).syntax_tree_root.nodes
                    insert(k, placeholder_2_nodes)
                    k.current = ascendingbranchingnode
                    x = bracket_pair_2_content_and_rest.rest
                    continue
            
            various = [ 
                ('^{', lambda: AscendingBranchingNode('', '^{', '}')), 
                ('_{', lambda: DescendingBranchingNode('', '_{', '}'))
            ]
            for opening___get_tree_node in various:
                opening = opening___get_tree_node[0]
                if x.startswith(opening):
                    node = opening___get_tree_node[1]()
                    insert_with_encapsulate_current(k, node)
                    bracket_pair_content_and_rest = get_bracket_pair_content(x, opening, '}')
                    second_placeholder_nodes = parse_latex(bracket_pair_content_and_rest.content, latexparserconfiguration).syntax_tree_root.nodes
                    insert(k, second_placeholder_nodes)
                    k.current = node
                    x = bracket_pair_content_and_rest.rest
                    handled = True
                    break
            if handled:
                continue

            insert(k, StandardLeafNode(str(x[0])))
            x = x[1:]
            continue
        return k