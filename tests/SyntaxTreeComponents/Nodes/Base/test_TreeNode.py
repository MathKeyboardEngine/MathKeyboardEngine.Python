import pytest
from src import TreeNode, KeyboardMemory
from tests.testhelpers.UnitTestLatexConfiguration import UnitTestLatexConfiguration

def test_not_implementing_getLatexPart_should_raise():
    with pytest.raises(Exception) as ex:
        treeNode = IncompleteTreeNode()
        treeNode.getLatexPart(KeyboardMemory(), UnitTestLatexConfiguration())
    assert 'Not implemented: `getLatexPart`.' == str(ex.value)


class IncompleteTreeNode(TreeNode):
    def __init__(self):
        super().__init__()