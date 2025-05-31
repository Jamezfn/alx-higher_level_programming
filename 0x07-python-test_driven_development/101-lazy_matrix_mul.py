#!/usr/bin/python3
"""Lazy matrix multiplication
"""
import numpy as np
def lazy_matrix_mul(m_a, m_b):
    """Multiplies 2 matrices"""
    return np.matmul(np.array(m_a), np.array(m_b))
