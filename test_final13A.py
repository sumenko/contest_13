import unittest
from unittest.mock import patch
from io import StringIO
from typing import Callable, List
from final_13a_tests import tests_ready as tests_a
from final_13a_tests import tests_not_ready as tests_a_not

from final_13A import main as main_a
from final_13A import Deque
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

    def test_push_pop_back(self):
        """ Test methods pop_ push_ behavior """
        queue_length = 4
        d = Deque(queue_length)
        
        self.assertEqual(d.queue_length, queue_length)
        self.assertEqual(d.queue, [None, None, None, None])
        
        d.push_back(1)
        d.push_back(3)
        d.push_back(2)
        self.assertEqual(d.size, 3)
        self.assertEqual(d.queue, [1, 3, 2, None])
        
        d.pop_back()
        self.assertEqual(d.is_empty(), False)
        self.assertEqual(d.queue, [1, 3, None, None])
        
        d.pop_back()
        d.pop_back()
        self.assertEqual(d.queue, [None, None, None, None])
        self.assertEqual(d.size, 0)
        self.assertEqual(d.is_empty(), True)

    def test_push_back_front(self):
        """ Test push _front _back behavior """
        queue_length = 4
        d = Deque(queue_length)

        d.push_back(1)
        d.push_front(4)
        self.assertEqual(d.queue, [1, None, None, 4])
        d.push_front(3)
        self.assertEqual(d.queue, [1, None, 3, 4])
        d.push_back(5)
        self.assertEqual(d.queue, [1, 5, 3, 4])
        d.push_back(6) # ERROR raise
        self.assertEqual(d.queue, [1, 5, 3, 4])
        d.pop_back()
        self.assertEqual(d.queue, [1, None, 3, 4])
        

    def test_final_a(self):
        """ Test output for main() """
        for name, data, result in tests_a:
            self.assertEqual(
                self._get_output(name,
                                 'final_13A',
                                 data.split('\n'),
                                 main_a),
                                 result)
    
    def test_final_a_not(self):
        for name, data, result in tests_a_not:
            output = self._get_output(name,
                                 'final_13A',
                                 data.split('\n'),
                                 main_a)
            print('main output:\n', output)
            print('Correct output:\n', result)
            self.assertEqual(output, result)

    
if __name__ == '__main__':
    unittest.main()
