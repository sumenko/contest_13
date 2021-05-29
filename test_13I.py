from test_13 import Sprint13TestCase as test_case
from contest_13I import main as main_13_i

def test_13i():
    tests = (
                (
        'test 1',
        """8
2
peek
push 5
push 2
peek
size
size
push 1
size
""",
        """None
5
2
2
error
2
"""
                ),
    )
    t = test_case()
    for name, inp, res in tests:
        print(f'Test: {name}')
        t._assert_correct_output(name, 'contest_13I', inp.split('\n'), main_13_i,res)


if __name__ == '__main__':
    test_13i()
