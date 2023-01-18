from src import AscendingBranchingNode, KeyboardMemory, LatexConfiguration, get_edit_mode_latex, insert


def test_allows_customizing_the_shape_of_the_cursor_and_empty_Placeholder():
    # Arrange
    k = KeyboardMemory()
    insert(k, AscendingBranchingNode('', '^{', '}'))
    config = LatexConfiguration()
    # Act
    config.active_placeholder_shape = 'my_cursor'
    config.passive_placeholder_shape = 'my_empty_place'
    # Assert
    assert r'my_cursor^{my_empty_place}' == get_edit_mode_latex(k, config)


def test_allows_customizing_the_color_of_the_cursorand_Placeholders():
    # Arrange
    k = KeyboardMemory()
    insert(k, AscendingBranchingNode('', '^{', '}'))
    config = LatexConfiguration()
    config.active_placeholder_shape = r'\blacksquare'
    config.passive_placeholder_shape = r'\blacksquare'
    # Act
    config.active_placeholder_color = 'orange'
    config.passive_placeholder_color = 'gray'
    # Assert
    assert r'{\color{orange}\blacksquare}^{{\color{gray}\blacksquare}}' == get_edit_mode_latex(k, config)
