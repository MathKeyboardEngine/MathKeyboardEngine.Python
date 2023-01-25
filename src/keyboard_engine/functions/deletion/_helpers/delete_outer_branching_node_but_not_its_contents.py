from src.syntax_tree_components.Placeholder.Placeholder import Placeholder


def delete_outer_branching_node_but_not_its_contents(non_empty_placeholder: Placeholder):
    outer_branchingnode = non_empty_placeholder.parent_node
    index_of_outer_branchingnode = outer_branchingnode.parent_placeholder.nodes.index(outer_branchingnode)
    outer_branchingnode.parent_placeholder.nodes[index_of_outer_branchingnode : index_of_outer_branchingnode + 1] = non_empty_placeholder.nodes
    for node in non_empty_placeholder.nodes:
        node.parent_placeholder = outer_branchingnode.parent_placeholder
