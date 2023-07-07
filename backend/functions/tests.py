from django.test import TestCase
import timeit

# Create your tests here.


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


class FunctionTestCase(TestCase):
    def test_one(self):
        execution_time = timeit.timeit(lambda: fibonacci(20), number=100)
        print(f"Execution time: {execution_time} seconds")
        self.assertEqual(3, 3)
