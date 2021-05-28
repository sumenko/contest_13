


def is_correct_bracket_seq(seq: str) -> bool:
    closed_bracket = {
        '(': ')',
        '[': ']',
        '{': '}',
    }
    stack = []
    if seq == '': return True
    if not seq[0] in closed_bracket.keys(): return False
    stack.append(seq[0])
    for c in seq[1:]:
        if (stack != [] and
            stack[-1] in closed_bracket.keys() 
            and closed_bracket[stack[-1]] == c):
            stack.pop()
            continue
        stack.append(c)
    return stack == []
if __name__ == '__main__':
    
    assert is_correct_bracket_seq('') == True
    assert is_correct_bracket_seq('()') == True
    assert is_correct_bracket_seq('{[()]}') == True
    assert is_correct_bracket_seq('[]') == True

    assert is_correct_bracket_seq('{}') == True
    assert is_correct_bracket_seq('{}{}') == True
    assert is_correct_bracket_seq('{}{})') == False
    assert is_correct_bracket_seq('{}}') == False
    assert is_correct_bracket_seq('(){[]{}}') == True
    assert is_correct_bracket_seq('(){[]{}}') == True
    assert is_correct_bracket_seq('((}}))') == False
    assert is_correct_bracket_seq('}{') == False
    print(is_correct_bracket_seq(input()))
    
  