# Module for testing python code
import pytest

# The file name that gets tested
import multiply_by_four

def test_three_expects_12():
  assert multiply_by_four.multiply_by_four(3) == 12

def test_zero_expects_0():
  assert multiply_by_four.multiply_by_four(0) == 0
