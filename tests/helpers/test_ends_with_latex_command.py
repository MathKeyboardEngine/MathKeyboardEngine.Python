from src.helpers.concat_latex import ends_with_latex_command

def test_returns_True_for_latex_commands_with_a_slash_and_letters():
    for s in [r'\pi', r'2\pi', r'2\times\pi', r'\sin']:
      assert ends_with_latex_command(s)

def test_returns_false_for_other_stuff():
    for s in [r'\pi^2', r'\sin6', r'\sin a', '', r'\|', r'\\']:
      assert not ends_with_latex_command(s)