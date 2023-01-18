import pytest

from src import KeyboardMemory, TreeNode
from tests._testhelpers.UnitTestLatexConfiguration import UnitTestLatexConfiguration


def test_not_implementing_get_latex_part_should_raise():
    with pytest.raises(Exception) as ex:
        treenode = IncompleteTreeNode()
        treenode.get_latex_part(KeyboardMemory(), UnitTestLatexConfiguration())
    assert 'Not implemented: `get_latex_part`.' == str(ex.value)


class IncompleteTreeNode(TreeNode):
    def __init__(self):
        super().__init__()