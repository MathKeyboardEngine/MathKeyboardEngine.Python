class BracePairContent:
        def __init__(self, content: str, rest: str) -> None:
            self.content = content
            self.rest = rest

def get_bracket_pair_content(s_with_opening: str, opening: str, closing: str):
    print()
    opening_bracket = opening[-1]
    s = s_with_opening[len(opening):]
    print ("s: " + s)
    level = 0
    closing_bracket_index = 0
    while closing_bracket_index < len(s):
        if s[closing_bracket_index: closing_bracket_index + len(closing)] == closing:
            if level == 0:
                return BracePairContent(s[:closing_bracket_index], s[(closing_bracket_index + len(closing)):])
            else:
                level -= 1
                closing_bracket_index += 1
                continue
        to_ignores = ['\\' + opening_bracket, '\\' + closing, r'\left' + opening_bracket, r'\right' + closing ]
        current_position = s[closing_bracket_index:]
        for to_ignore in to_ignores:
            if len(current_position) >= len(to_ignore) and current_position.startswith(to_ignore):
                closing_bracket_index += len(to_ignore)
                closing_bracket_index += 1
                continue
        if s[closing_bracket_index] == opening_bracket:
            level += 1
        closing_bracket_index += 1
    raise Exception('A closing ' + closing + ' is missing.')