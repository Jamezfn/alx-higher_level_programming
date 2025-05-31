#!/usr/bin/python3
"""Lazy matrix multiplication
"""
import numpy as np
def lazy_matrix_mul(m_a, m_b):
    """Multiplies 2 matrices"""
    a = np.array(m_a, dtype=float)
    b = np.array(m_b, dtype=float)
    return np.matmul(a, b)
