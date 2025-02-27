import pytest
import multiply_by_two

def test_multiply_2_expects_4():
  assert multiply_by_two.multiply_by_two(2) == 4

def test_multiply_0():
  assert multiply_by_two.multiply_by_two(0) == 0
