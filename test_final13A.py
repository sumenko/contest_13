import unittest
from unittest.mock import patch
from io import StringIO
from typing import Callable, List
from final_13a_tests import tests as tests_a

from final_13A import main as main_a

class TestFinal13(unittest.TestCase):
    def _get_output(
        self,
        subtest_name: str,
        module: str,
        side_effect: List[str],
        test_func: Callable,
    ) -> str:
        with self.subTest(
            name=subtest_name,
        ), patch(
            f'{module}.input',
            side_effect=side_effect
        ),patch(
            f'sys.stdout', new=StringIO()
        ) as fake_out:
            test_func()
            return fake_out.getvalue()

    def test_final_a(self):
        for name, data, result in tests_a:
            self.assertEqual(
                self._get_output(name,
                                 'final_13A',
                                 data.split('\n'),
                                 main_a),
                                 result)

    
if __name__ == '__main__':
    unittest.main()
