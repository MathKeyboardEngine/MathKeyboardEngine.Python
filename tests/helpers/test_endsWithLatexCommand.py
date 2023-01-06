from src.helpers.concatLatex import endsWithLatexCommand

def test_returns_True_for_latex_commands_with_a_slash_and_letters():
    for s in [r'\pi', r'2\pi', r'2\times\pi', r'\sin']:
      assert endsWithLatexCommand(s)

def test_returns_false_for_other_stuff():
    for s in [r'\pi^2', r'\sin6', r'\sin a', '', r'\|', r'\\']:
      assert not endsWithLatexCommand(s)