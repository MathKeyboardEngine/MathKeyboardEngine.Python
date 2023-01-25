from typing import List

from src._helpers.coalesce import coalesce
from src._helpers.first_after_or_none import first_after_or_none
from src._helpers.first_before_or_none import first_before_or_none
from src.keyboard_engine.functions.deletion._helpers.delete_outer_branching_node_but_not_its_contents import delete_outer_branching_node_but_not_its_contents
from src.keyboard_engine.KeyboardMemory import KeyboardMemory
from src.syntax_tree_components.nodes.base.BranchingNode import BranchingNode
from src.syntax_tree_components.nodes.base.TreeNode import TreeNode
from src.syntax_tree_components.Placeholder.Placeholder import Placeholder


def delete_right(k: KeyboardMemory) -> None:
    if isinstance(k.current, Placeholder):
        if k.current.parent_node is not None and all(len(ph.nodes) == 0 for ph in k.current.parent_node.placeholders):
            previousNode = first_before_or_none(k.current.parent_node.parent_placeholder.nodes, k.current.parent_node)
            k.current.parent_node.parent_placeholder.nodes.remove(k.current.parent_node)
            k.current = coalesce(previousNode, k.current.parent_node.parent_placeholder)
        else:
            nodes = k.current.nodes
            if len(nodes) > 0:
                handle_deletion(k, nodes[0])
            elif k.current.parent_node is not None:
                parentNode = k.current.parent_node
                siblingPlaceholders: List[Placeholder] = parentNode.placeholders
                if siblingPlaceholders[0] == k.current and len(siblingPlaceholders) == 2:
                    nonEmptyPlaceholder = siblingPlaceholders[1]
                    k.current = coalesce(first_before_or_none(parentNode.parent_placeholder.nodes, parentNode), parentNode.parent_placeholder)
                    delete_outer_branching_node_but_not_its_contents(nonEmptyPlaceholder)
                else:
                    for i in range(siblingPlaceholders.index(k.current) + 1, len(siblingPlaceholders)):
                        if len(siblingPlaceholders[i].nodes) > 0:
                            k.current = siblingPlaceholders[i]
                            delete_right(k)
                            return
    else:
        next_node = first_after_or_none(k.current.parent_placeholder.nodes, k.current)
        if next_node is not None:
            handle_deletion(k, next_node)


def handle_deletion(k: KeyboardMemory, next_node: TreeNode) -> None:
    if isinstance(next_node, BranchingNode):
        if len(next_node.placeholders) == 1 and len(next_node.placeholders[0].nodes) > 0:
            delete_outer_branching_node_but_not_its_contents(next_node.placeholders[0])
        elif len(next_node.placeholders) == 2 and len(next_node.placeholders[0].nodes) == 0 and len(next_node.placeholders[1].nodes) > 0:
            delete_outer_branching_node_but_not_its_contents(next_node.placeholders[1])
        else:
            k.current = next_node.placeholders[0]
            delete_right(k)
    else:
        next_node.parent_placeholder.nodes.remove(next_node)
