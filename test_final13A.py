import unittest
from io import StringIO
from typing import Callable, List
from unittest.mock import patch

from final_13A import Deque, QueueIsEmpty, QueueIsFull
from final_13A import main as main_a
from final_13a_tests import tests as tests_a


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
        ), patch(
            'sys.stdout', new=StringIO()
        ) as fake_out:
            test_func()
            return fake_out.getvalue()

    def test_push_pop_back(self):
        """ Test methods pop_ push_ behavior """
        queue_length = 4
        d = Deque(queue_length)

        self.assertEqual(d._queue_length, queue_length)
        self.assertEqual(d._queue, [None, None, None, None])

        d.push_back(1)
        d.push_back(3)
        d.push_back(2)
        self.assertEqual(d.size, 3)
        self.assertEqual(d._queue, [1, 3, 2, None])

        d.pop_back()
        self.assertEqual(d.is_empty(), False)
        self.assertEqual(d._queue, [1, 3, None, None])

        d.pop_back()
        d.pop_back()
        self.assertEqual(d._queue, [None, None, None, None])
        self.assertEqual(d.size, 0)
        self.assertEqual(d.is_empty(), True)

    def test_push_back_front(self):
        """ Test push _front _back behavior """
        queue_length = 4
        d = Deque(queue_length)

        d.push_back(1)
        d.push_front(4)
        self.assertEqual(d._queue, [1, None, None, 4])
        d.push_front(3)
        self.assertEqual(d._queue, [1, None, 3, 4])
        d.push_back(5)
        self.assertEqual(d._queue, [1, 5, 3, 4])
        self.assertEqual(d._queue, [1, 5, 3, 4])
        d.pop_back()
        self.assertEqual(d._queue, [1, None, 3, 4])

    def test_raises_errors_full(self):
        """ Test class raises QueueIsFull """
        d = Deque(2)
        d.push_back(1)
        d.push_front(2)
        with self.assertRaises(QueueIsFull):
            d.push_back(3)

    def test_raises_errors_empty(self):
        """ Test class raises QueueIsEmpty """
        d = Deque(2)
        with self.assertRaises(QueueIsEmpty):
            d.pop_back()
        with self.assertRaises(QueueIsEmpty):
            d.pop_front()

    def test_final_a(self):
        for name, data, result in tests_a:
            output = self._get_output(name,
                                      'final_13A',
                                      data.split('\n'),
                                      main_a)
            print('main() output:\n', output)
            print('Correct output:\n', result)
            self.assertEqual(output, result)


if __name__ == '__main__':
    unittest.main()
