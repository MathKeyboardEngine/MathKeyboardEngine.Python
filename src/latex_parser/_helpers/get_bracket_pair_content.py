class BracePairContent:
    def __init__(self, content: str, rest: str) -> None:
        self.content = content
        self.rest = rest


def get_bracket_pair_content(s_with_opening: str, opening: str, closing: str):
    opening_bracket = opening[-1]
    s = s_with_opening[len(opening) :]
    level = 0
    potential_closing_bracket_index = 0
    while potential_closing_bracket_index < len(s):
        if s[potential_closing_bracket_index : potential_closing_bracket_index + len(closing)] == closing:
            if level == 0:
                return BracePairContent(s[:potential_closing_bracket_index], s[(potential_closing_bracket_index + len(closing)) :])
            else:
                level -= 1
                potential_closing_bracket_index += 1
                continue
        to_ignores = ['\\' + opening_bracket, '\\' + closing, r'\left' + opening_bracket, r'\right' + closing]
        s_from_potential_closing_bracket_index = s[potential_closing_bracket_index:]
        ignored = False
        for to_ignore in to_ignores:
            if len(s_from_potential_closing_bracket_index) >= len(to_ignore) and s_from_potential_closing_bracket_index.startswith(to_ignore):
                potential_closing_bracket_index += len(to_ignore)
                ignored = True
        if ignored:
            continue
        if s[potential_closing_bracket_index] == opening_bracket:
            level += 1
        potential_closing_bracket_index += 1
    raise Exception('A closing ' + closing + ' is missing.')
