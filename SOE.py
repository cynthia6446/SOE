# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import sys 
A = np.array([[2,3,-4],
              [1,-2,3],
              [3,-1,-1]])

print(A)
type(A)
A.shape

'''
system of equations:
suppose x1 =5, and x2 =1 then
  1*x1 + 2*x2 = 9
  3*x1 + 4*x2 = 19

A@x = b
A.inv @ A @x =  A.inv @ b
'''

b =np.array([[-4],
             [6],
             [-2]])

print(f"\nb = {b}")

## solve equations

detA = np.linalg.det(A)
print(f"determinant of matrix A is {detA: 0.3f}")
if detA == 0:
    print("/ndet A = 0; no solution\n")
    sys.exit()

Ainv = np.linalg.inv(A)
print(f"A- inverse = \n{Ainv}")

print(Ainv @ A)

x = Ainv @ b
print(f"\nunknowns are: \n{x}")

#check
print(f"\ncheck: \n{A@x}")