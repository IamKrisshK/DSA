def evaluate(s: str, knowledge: list[list[str]]) -> str:
    lookup = dict(knowledge)
    res = []
    key = []
    inside = False
    for c in s:
        if c == '(':
            inside = True
        elif c == ')':
            res.append(lookup.get(''.join(key), '?'))
            key.clear()
            inside = False
        elif inside:
            key.append(c)
        else:
            res.append(c)
    return ''.join(res)
