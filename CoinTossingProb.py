from itertools import product
import numpy as np
def coinTossingWinProb(n):
  possibleOutcomes = list(product(range(2), repeat = n))
  totalWin = 0

  groupNumber = int(n/2)
  for i in possibleOutcomes:
    A = None
    B = None

    k = 0
    while k < groupNumber:
      if i[2*k] == 0:
        A = i[2*k+1]
        break
      else:
        k += 1

    if k == groupNumber:
      A = i[-1]

    j = 0
    while j < groupNumber:
      if i[2*j+1] == 0:
        B = i[2*j]
        break
      else:
        j += 1

    if j == groupNumber:
      B = i[-2]

    if A == B:
      totalWin += 1

  return totalWin/2**n
