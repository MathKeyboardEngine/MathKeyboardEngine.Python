from src import AscendingBranchingNode, KeyboardMemory, LatexConfiguration, insert, getEditModeLatex

def test_allows_customizing_the_shape_of_the_cursor_and_empty_Placeholder():
    # Arrange
    k = KeyboardMemory()
    insert(k, AscendingBranchingNode('', '^{', '}'))
    myLatexConfiguration = LatexConfiguration()
    # Act
    myLatexConfiguration.activePlaceholderShape = 'myCursor'
    myLatexConfiguration.passivePlaceholderShape = 'myEmptyPlace'
    # Assert
    assert r'myCursor^{myEmptyPlace}' == getEditModeLatex(k, myLatexConfiguration)

def test_allows_customizing_the_color_of_the_cursorand_Placeholders():
    # Arrange
    k = KeyboardMemory()
    insert(k, AscendingBranchingNode('', '^{', '}'))
    myLatexConfiguration = LatexConfiguration()
    myLatexConfiguration.activePlaceholderShape = r'\blacksquare'
    myLatexConfiguration.passivePlaceholderShape = r'\blacksquare'
    # Act
    myLatexConfiguration.activePlaceholderColor = 'orange'
    myLatexConfiguration.passivePlaceholderColor = 'gray'
    # Assert
    assert r'{\color{orange}\blacksquare}^{{\color{gray}\blacksquare}}' == getEditModeLatex(k, myLatexConfiguration)