import pytest

from src import get_view_mode_latex, parse_latex, LatexParserConfiguration, DigitNode, DescendingBranchingNode, MatrixNode, RoundBracketsNode, insert, insert_with_encapsulate_current, StandardLeafNode, AscendingBranchingNode, BranchingNode, StandardBranchingNode, DecimalSeparatorNode
from tests._testhelpers.UnitTestLatexConfiguration import UnitTestLatexConfiguration

def test_can_handle_empty_and_null_input():
    for testinput in ['', ' ', None]:
        # Act
        k = parse_latex(testinput)
        # Assert
        assert '⬚' == get_view_mode_latex(k, UnitTestLatexConfiguration())
    

def test_parses_exactly():
    for testinput in [
       r'1',
       r'123',
       r'1.2',
       r'x',
       r'xyz',
       r'2x',
       r'\frac{1}{2}',
       r'3\frac{1}{2}',
       r'\frac{1}{2}3',
       r'\frac{1+x}{2-y}',
       r'\frac{7}{\frac{8}{9}}',
       r'\binom{10}{2}',
       r'\binom{\frac{4}{2}}{1}',
       r'\frac{\frac{\binom{10}{x}}{x-1}}{\frac{2a-x}{a}}',
       r'2^x',
       r'2^{x}',
       r'2^{x+1}',
       r'2^{\frac{1}{2}}',
       r'1+2^{\frac{3}{4}}+5',
       r'a_{1}',
       r'a_1',
       r'a_{n-1}',
       r'a_{n-2}a_{n-1}a_{n}',
       r'x^\frac{1}{2}',
       r'x^{\frac{1}{2}}',
       r'x^\frac{p^2}{2}',
       r'x^\frac{p^{2}}{2}',
       r'x^\pi',
       r'x^{\pi}',
       r'a_1\times a_2',
       r'a_{1}\times a_{2}',
       r'\sqrt{2}',
       r'a\sqrt{2}b',
       r'\sin\pi',
       r'\sin{\pi}',
       r'\|',
       r'\sin6',
       r'\sin{6}',
       r'\sin(6)',
       r'\sin\left(6\right)',
    ]:
        # Act
        k = parse_latex(testinput)
        # Assert
        assert testinput == get_view_mode_latex(k, UnitTestLatexConfiguration())


def test_can_handle_non_decimal_number_base():
    # Arrange
    myParserConfig = LatexParserConfiguration()
    myParserConfig.additional_digits = ['↊', '↋']
    # Act
    k = parse_latex('6↊↋', myParserConfig)
    # Assert
    for node in k.syntax_tree_root.nodes:
        assert isinstance(node, DigitNode)

    insert_with_encapsulate_current(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    insert(k, DigitNode('2'))
    assert r'\frac{6↊↋}{2}' == get_view_mode_latex(k, UnitTestLatexConfiguration())


def test_allows_commands_with_bracket_only_difference():
    # Act & Assert
    assert r'\sqrt[3]{27}' == get_view_mode_latex(parse_latex(r'\sqrt[3]{27}'), UnitTestLatexConfiguration())
    assert r'\sqrt{3}{27}', get_view_mode_latex(parse_latex(r'\sqrt{3}{27}'), UnitTestLatexConfiguration())
    assert r'\sqrt[3][27]', get_view_mode_latex(parse_latex(r'\sqrt[3][27]'), UnitTestLatexConfiguration())
    assert r'\sqrt{3}[27]', get_view_mode_latex(parse_latex(r'\sqrt{3}[27]'), UnitTestLatexConfiguration())


def test_throws_on_missing_closing_bracket():
    with pytest.raises(Exception) as ex:
        parse_latex(r'\frac{1}{2')
    assert 'A closing } is missing.' == str(ex.value)


def test_expected_standardLeafNodes():
    for testinput in [
            r'a',
            r'\|',
            r'\pi',
            r'\left{',
            r'\left\{',
            r'\right}',
            r'\right\}',
            r'\right|',
            r'\right\|',
            r'\right]',
            r'\right\]',
            r'\left(',
            r'\right)'
            ]:
        my_parser_config = LatexParserConfiguration()
        my_parser_config.prefer_roundbracketsnode = False
        # Act
        k = parse_latex(testinput, my_parser_config)
        # Assert
        nodes = k.syntax_tree_root.nodes
        assert 1 == len(nodes)
        node = nodes[0]
        assert isinstance(node, StandardLeafNode)
        assert testinput == get_view_mode_latex(k, UnitTestLatexConfiguration())
    

def test_sinus_and_argument_are_separate_LeafNodes():
    for testinput in [r'\sin6', r'\sin 6']:
        # Act
        k = parse_latex(testinput)
        # Assert
        nodes = k.syntax_tree_root.nodes
        assert 2 == len(nodes)
        assert isinstance(nodes[0], StandardLeafNode)
        assert isinstance(nodes[1], DigitNode)
        assert r'\sin6' == get_view_mode_latex(k, UnitTestLatexConfiguration())


def test_can_understand_sin_as_a_StandardBranchingNode():
    # Arrange
    latex = r'\sin{6}'
    # Act
    k = parse_latex(latex)
    # Assert
    outer_nodes = k.syntax_tree_root.nodes
    assert 1 == len(outer_nodes)
    outer_node = outer_nodes[0]
    assert isinstance(outer_node, StandardBranchingNode)
    inner_nodes = outer_node.placeholders[0].nodes
    assert 1 == len(inner_nodes)
    inner_node = inner_nodes[0]
    assert isinstance(inner_node, DigitNode)
    assert latex == get_view_mode_latex(k, UnitTestLatexConfiguration())
    

def test_it_understands_several_decimal_separator_symbols_by_default():
    for separator in ['.', '{,}']:
        # Arrange
        latex = '1' + separator + '2'
        # Act
        k = parse_latex(latex)
        # Assert
        nodes = k.syntax_tree_root.nodes
        assert 3 == len(nodes)
        separatorNode = nodes[1]
        assert isinstance(nodes[0], DigitNode)
        assert isinstance(separatorNode, DecimalSeparatorNode)
        assert isinstance(nodes[2], DigitNode)
        assert latex == get_view_mode_latex(k, UnitTestLatexConfiguration())


def test_it_allows_modifying_the_decimal_separator_even_after_parsing():
    # Arrange
    preferredDecimalSeparator = '{,}'
    myParserConfig = LatexParserConfiguration()
    myParserConfig.preferred_decimal_separator = lambda: preferredDecimalSeparator
    
    # Act 1
    k = parse_latex('1.2', myParserConfig)
    # Assert 1
    assert '1{,}2' == get_view_mode_latex(k, UnitTestLatexConfiguration())
    # Act 2
    preferredDecimalSeparator = ','
    # Assert 2
    assert '1,2' == get_view_mode_latex(k, UnitTestLatexConfiguration())


def test_it_understands_that_subscripts_can_be_DescendingBranchingNodes():
    # Arrange
    latex = r'a_{12}\times a_{34}'
    # Act
    k = parse_latex(latex)
    # Assert
    nodes = k.syntax_tree_root.nodes
    assert 3 == len(nodes)

    outerNode = nodes[0]
    assert isinstance(outerNode, DescendingBranchingNode)
    subscript1 = outerNode.placeholders[1].nodes
    assert 2 == len(subscript1)
    assert isinstance(subscript1[0], DigitNode)
    assert isinstance(subscript1[1], DigitNode)

    assert isinstance(nodes[1], StandardLeafNode)

    outerNode2 = nodes[0]
    assert isinstance(outerNode2, DescendingBranchingNode)
    subscript2 = outerNode2.placeholders[1].nodes
    assert 2 == len(subscript2)
    assert isinstance(subscript2[0], DigitNode)
    assert isinstance(subscript2[1], DigitNode)

    assert latex == get_view_mode_latex(k, UnitTestLatexConfiguration())


def test_it_understands_complex_latex():
    # Arrange
    latex = r'\exp\left[\int d^{4}xg\phi\bar{\psi}\psi\right]=\sum_{n=0}^{\infty}\frac{g^{n}}{n!}\left(\int d^{4}x\phi\bar{\psi}\psi\right)^{n}'
    # Act
    myParserConfig = LatexParserConfiguration()
    myParserConfig.prefer_roundbracketsnode = False
    
    k = parse_latex(latex, myParserConfig)
    # Assert
    nodes = k.syntax_tree_root.nodes

    assert isinstance(nodes[0], StandardLeafNode)
    assert r'\exp' == get_view_mode_latex(nodes[0], UnitTestLatexConfiguration())

    assert isinstance(nodes[1], StandardLeafNode)
    assert r'\left[' == get_view_mode_latex(nodes[1], UnitTestLatexConfiguration())

    assert isinstance(nodes[2], StandardLeafNode)
    assert r'\int'== get_view_mode_latex(nodes[2], UnitTestLatexConfiguration())

    assert isinstance(nodes[3], AscendingBranchingNode)
    assert 'd^{4}' == get_view_mode_latex(nodes[3], UnitTestLatexConfiguration())

    assert isinstance(nodes[4], StandardLeafNode)
    assert 'x' == get_view_mode_latex(nodes[4], UnitTestLatexConfiguration())

    assert isinstance(nodes[5], StandardLeafNode)
    assert 'g' == get_view_mode_latex(nodes[5], UnitTestLatexConfiguration())

    assert isinstance(nodes[6], StandardLeafNode)
    assert r'\phi' == get_view_mode_latex(nodes[6], UnitTestLatexConfiguration())

    assert isinstance(nodes[7], StandardBranchingNode)
    assert r'\bar{\psi}' == get_view_mode_latex(nodes[7], UnitTestLatexConfiguration())

    assert isinstance(nodes[8], StandardLeafNode)
    assert r'\psi' == get_view_mode_latex(nodes[8], UnitTestLatexConfiguration())

    assert isinstance(nodes[9], StandardLeafNode)
    assert r'\right]' == get_view_mode_latex(nodes[9], UnitTestLatexConfiguration())

    assert isinstance(nodes[10], StandardLeafNode)
    assert '=' == get_view_mode_latex(nodes[10], UnitTestLatexConfiguration())

    assert isinstance(nodes[11], StandardLeafNode)
    assert r'\sum' == get_view_mode_latex(nodes[11], UnitTestLatexConfiguration())

    assert isinstance(nodes[12], AscendingBranchingNode)
    assert r'_{n=0}^{\infty}' == get_view_mode_latex(nodes[12], UnitTestLatexConfiguration())

    assert isinstance(nodes[13], DescendingBranchingNode)
    assert r'\frac{g^{n}}{n!}' == get_view_mode_latex(nodes[13], UnitTestLatexConfiguration())

    assert isinstance(nodes[14], StandardLeafNode)
    assert r'\left(' == get_view_mode_latex(nodes[14], UnitTestLatexConfiguration())

    assert isinstance(nodes[15], StandardLeafNode)
    assert r'\int' == get_view_mode_latex(nodes[15], UnitTestLatexConfiguration())

    assert isinstance(nodes[16], AscendingBranchingNode)
    assert 'd^{4}' == get_view_mode_latex(nodes[16], UnitTestLatexConfiguration())

    assert isinstance(nodes[17], StandardLeafNode)
    assert 'x' == get_view_mode_latex(nodes[17], UnitTestLatexConfiguration())

    assert isinstance(nodes[18], StandardLeafNode)
    assert r'\phi' == get_view_mode_latex(nodes[18], UnitTestLatexConfiguration())

    assert isinstance(nodes[19], StandardBranchingNode)
    assert r'\bar{\psi}' == get_view_mode_latex(nodes[19], UnitTestLatexConfiguration())

    assert isinstance(nodes[20], StandardLeafNode)
    assert r'\psi' == get_view_mode_latex(nodes[20], UnitTestLatexConfiguration())

    assert isinstance(nodes[21], AscendingBranchingNode)
    assert r'\right)^{n}' == get_view_mode_latex(nodes[21], UnitTestLatexConfiguration())

    assert latex == get_view_mode_latex(k, UnitTestLatexConfiguration())


def test_it_understands_all_matrix_types():
    for matrix_type in ['matrix', 'pmatrix']:
        # Arrange
        latex = r'3\begin{' + matrix_type + r'}1+2 & x^{3} \\ \frac{4}{5} & x \\ \pi & x\left(x+6\right)\end{' + matrix_type + '}='
        # Act
        k = parse_latex(latex)
        # Assert
        nodes = k.syntax_tree_root.nodes
        assert 3 == len(nodes)
        assert isinstance(nodes[0], DigitNode)
        assert isinstance(nodes[1], MatrixNode)
        assert isinstance(nodes[2], StandardLeafNode)

        matrixNode = nodes[1]
        assert 6 == len(matrixNode.placeholders)

        placeholder0 = matrixNode.placeholders[0]
        assert 3 == len(placeholder0.nodes)
        assert '1+2' == get_view_mode_latex(placeholder0, UnitTestLatexConfiguration())

        placeholder1 = matrixNode.placeholders[1]
        assert 1 == len(placeholder1.nodes)
        placeholder1Node = placeholder1.nodes[0]
        assert 'x^{3}' == get_view_mode_latex(placeholder1, UnitTestLatexConfiguration())
        assert isinstance(placeholder1Node, AscendingBranchingNode)

        placeholder2 = matrixNode.placeholders[2]
        assert 1 == len(placeholder2.nodes)
        placeholder2Node = placeholder2.nodes[0]
        assert isinstance(placeholder2Node, DescendingBranchingNode)
        assert r'\frac{4}{5}' == get_view_mode_latex(placeholder2, UnitTestLatexConfiguration())

        assert 1 == len(matrixNode.placeholders[3].nodes)
        assert 'x' == get_view_mode_latex(matrixNode.placeholders[3].nodes[0], UnitTestLatexConfiguration())

        assert 1 == len(matrixNode.placeholders[4].nodes)
        assert r'\pi' == get_view_mode_latex(matrixNode.placeholders[4].nodes[0], UnitTestLatexConfiguration())

        placeholder5 = matrixNode.placeholders[5]
        assert 2 == len(placeholder5.nodes)
        assert r'x\left(x+6\right)' == get_view_mode_latex(placeholder5, UnitTestLatexConfiguration())

        assert latex == get_view_mode_latex(k, UnitTestLatexConfiguration())


def test_it_parses_begincases_and_text():
    # Arrange
    latex = r'x=\begin{cases}a & \text{if }b \\ c & \text{if }d\end{cases}'
    # Act
    k = parse_latex(latex)
    # Assert
    nodes = k.syntax_tree_root.nodes
    assert 3 == len(nodes)
    assert isinstance(nodes[2], MatrixNode)
    matrixNode = nodes[2]
    assert 4 == len(matrixNode.placeholders)
    placeholder1 = matrixNode.placeholders[1]
    assert 2 == len(placeholder1.nodes)
    assert r'\text{if }' == get_view_mode_latex(placeholder1.nodes[0], UnitTestLatexConfiguration())
    assert latex == get_view_mode_latex(k, UnitTestLatexConfiguration())


def test_it_throws_if_begin_does_not_contain_the_word_matrix_or_cases():
    with pytest.raises(Exception) as ex:
        parse_latex(r'\begin{test}12\\34\end{test}')
    assert r'Expected a word ending with "matrix" or "cases" after "\begin{".' == str(ex.value)


def test_latexparserconfiguration_prefer_roundbracketsnode():
    for latex in ['(x-1)', r'\left(x-1\right)']:
        # Arrange
        myParserConfig = LatexParserConfiguration()
        myParserConfig.prefer_roundbracketsnode = True
        # Act
        k = parse_latex(latex, myParserConfig)
        # Assert
        assert 1 == len(k.syntax_tree_root.nodes)
        node = k.syntax_tree_root.nodes[0]
        assert isinstance(node, RoundBracketsNode)
        roundBracketsNode = node
        assert latex == get_view_mode_latex(k, UnitTestLatexConfiguration())
        assert 3 == len(roundBracketsNode.placeholders[0].nodes)
    

def test_it_parses_lim_correctly():
    # Arrange
    latex = r'\lim_{x\rightarrow\infty}x'
    # Act
    k = parse_latex(latex)
    # Assert
    nodes = k.syntax_tree_root.nodes
    assert 2 == len(nodes)

    assert isinstance(nodes[0], DescendingBranchingNode)
    limitNode = nodes[0]
    assert 2 == len(limitNode.placeholders)

    assert isinstance(nodes[1], StandardLeafNode)

    assert latex == get_view_mode_latex(k, UnitTestLatexConfiguration())


def test_it_parses_sum_correctly():
    # Arrange
    latex = r'\sum_{0}^{\infty}'
    # Act
    k = parse_latex(latex)
    # Assert
    nodes = k.syntax_tree_root.nodes
    assert 2 == len(nodes)
    assert isinstance(nodes[0], StandardLeafNode)
    assert r'\sum' == get_view_mode_latex(nodes[0], UnitTestLatexConfiguration())
    assert isinstance(nodes[1], AscendingBranchingNode)
    sumNode = nodes[1]
    assert r'_{0}^{\infty}' == get_view_mode_latex(nodes[1], UnitTestLatexConfiguration())
    assert 2 == len(sumNode.placeholders)
    assert isinstance(sumNode.placeholders[0].nodes[0], DigitNode)
    assert isinstance(sumNode.placeholders[1].nodes[0], StandardLeafNode)
    assert latex == get_view_mode_latex(k, UnitTestLatexConfiguration())