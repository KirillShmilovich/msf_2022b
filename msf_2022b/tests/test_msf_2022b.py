"""
Unit and regression test for the msf_2022b package.
"""

# Import package, test suite, and other packages as needed
import sys
import numpy as np
import pytest

import msf_2022b


def test_msf_2022b_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "msf_2022b" in sys.modules


def test_calculate_distance():
    """Sample test for calculating distance between two points."""
    rA = np.array([0, 0, 0])
    rB = np.array([0, 1.0, 0])
    assert msf_2022b.calculate_distance(rA, rB) == 1.0


def test_calculate_angle():
    """Sample test for calculating angle between three points."""
    rA = np.array([0, 0, -1])
    rB = np.array([0, 0, 0])
    rC = np.array([1, 0, 0])
    assert msf_2022b.calculate_angle(rA, rB, rC) == np.pi / 2


def test_calculate_angle_batch():
    """Sample test for calculating angle between three points."""
    rA = np.array([[0, 0, -1], [0, 0, -1]])
    rB = np.array([[0, 0, 0], [0, 0, 0]])
    rC = np.array([[1, 0, 0], [1, 0, 0]])
    assert msf_2022b.calculate_angle_batch(rA, rB, rC) == np.pi / 2


def test_calculate_angle_batch_2():
    """Sample test for calculating angle between three points."""
    rA = np.array([[0, 0, -1], [0, 0, -1]])
    rB = np.array([[0, 0, 0], [0, 0, 0]])
    rC = np.array([[1, 0, 0], [1, 0, 0]])
    assert msf_2022b.calculate_angle_batch(rA, rB, rC) == np.pi / 2

