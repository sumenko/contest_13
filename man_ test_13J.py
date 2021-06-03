from test_13 import Sprint13TestCase as test_case
from contest_13J import main

def test_13J():
    tests = (
                (
                        'Smoke test',
                        """4
size
get
size
get
""",
                        """0
error
0
error
"""
                ),
                (
                        'test 1',
                        """10
put -34
put -23
get
size
get
size
get
get
put 80
size""",
        """-34
1
-23
0
error
error
1
"""
                ),
    )
    t = test_case()
    for name, inp, res in tests:
        print(f'Test: {name}')
        t._assert_correct_output(name, 'contest_13J', inp.split('\n'), main,res)


if __name__ == '__main__':
    test_13J()
