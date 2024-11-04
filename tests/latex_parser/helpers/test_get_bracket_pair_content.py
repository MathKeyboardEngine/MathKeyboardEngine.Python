from src.latex_parser._helpers.get_bracket_pair_content import get_bracket_pair_content


def test_gets_bracket_pair_content():
    for testinput in [
      (r'\frac{', '}', r'\frac{1}{2}', '1', '{2}'),
      (r'\frac{', '}', r'\frac{123}{456}', '123', '{456}'),
      (r'\frac{', '}', r'\frac{\frac{1}{1-x}}{x}', r'\frac{1}{1-x}', '{x}'),
      (r'\frac{', '}', r'\frac{TEST\right}and\}\}\{}{x}', r'TEST\right}and\}\}\{', '{x}'),
      (r'\frac{', '}', r'\frac{1}{2}3', '1', '{2}3')
    ]:
      opening = testinput[0]
      closing_bracket = testinput[1]
      s_with_opening = testinput[2]
      expected_content = testinput[3]
      expected_rest = testinput[4]

      # Act
      result = get_bracket_pair_content(s_with_opening, opening, closing_bracket)
      # Assert
      assert expected_content == result.content
      assert expected_rest == result.rest
