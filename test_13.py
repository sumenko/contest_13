import unittest
from io import StringIO  # для тестирования вывода
from typing import Callable, List
from unittest.mock import patch  # для тестирования вывода
from contest_13G import main as main_task_g
from contest_13G import run_file

class Sprint13TestCase(unittest.TestCase):
    def _assert_correct_output(
        self,
        subtest_name: str,
        module: str,
        side_effect: List[str],
        test_func: Callable,
        expected_result: str
    ) -> None:
        """Вспомогательный метод для тестирования ввода и вывода
        Тут мы мокаем (mock)
        - функцию ввода input()
        - вывод stdout
        """
        with self.subTest(
            name=subtest_name
        ), patch(  # это Mock для функции ввода, мы "подменяем" функию input
            f'{module}.input',
            side_effect=side_effect  # здесьь передаются входные данные в input()
        ), patch(  # это Mock для вывода stdout, мы "подменяем" вывод
            f'sys.stdout', new=StringIO()
        ) as fake_out:
            test_func()
            self.assertEqual(
                fake_out.getvalue(),  # тестируем наш подменяемый вывод
                expected_result
            )
    def test_task_g(self):
        tests = (
            (
                'Тест 1',
                """10
pop
pop
push 4
push -5
push 7
pop
pop
get_max
pop
get_max""",
                """error
error
4
None
"""
            ), (
                'Тест 2',
                """10
get_max
push -6
pop
pop
get_max
push 2
get_max
pop
push -2
push -6""",
                """None
error
None
2
"""
            ), (
                'Test 7',
            """50
get_max
pop
push -7
pop
get_max
get_max
get_max
get_max
push 1
get_max
get_max
push 3
pop
pop
get_max
get_max
get_max
push -3
get_max
get_max
push 0
push 9
get_max
get_max
pop
get_max
push 4
get_max
get_max
push -3
push -4
get_max
push 9
push 9
pop
pop
push -1
push -4
push 3
push 10
pop
get_max
get_max
pop
push -9
get_max
pop
get_max
pop
pop
""",
        """None
error
None
None
None
None
1
1
None
None
None
-3
-3
9
9
0
4
4
4
4
4
4
4
"""), (
        'My_case',
        """10
push 10000
get_max
pop
get_max
push 10
push -10
push 10
pop
get_max
""", """10000
None
10
""")
        )
        for name, inp, res in tests:
            print('Test:', name)
            self._assert_correct_output(
                name, 'contest_13G', inp.split('\n'), main_task_g, res)
        

if __name__ == '__main__':
    unittest.main()
