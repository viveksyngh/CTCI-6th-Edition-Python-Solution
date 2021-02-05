"""
A child is running up a staircase with n steps and can hop either 1 step, 2 steps or 3 steps at at time.
Implement a method to count how many possible ways the child can run up the stairs.
"""
import unittest

def total_steps(n):
    memo = {}
    return total_setps_helper(n, memo)


def total_setps_helper(n, memo):
    if n in memo:
        return memo[n]
        
    if n < 0:
        return 0
    if n == 0:
        return 1
   
    value = total_setps_helper(n-1, memo) + \
            total_setps_helper(n-2, memo) + \
            total_setps_helper(n-3, memo)
    memo[n] = value
    return value


class TestTotalSteps(unittest.TestCase):
    def setUp(self):
        pass

    def test_positive(self):
        self.assertEqual(total_steps(1), 1)
        self.assertEqual(total_steps(2), 2)
        self.assertEqual(total_steps(3), 4)
        self.assertEqual(total_steps(5), 13)


if __name__ == '__main__':
    unittest.main()