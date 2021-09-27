import numpy as np
from algorithm import SmithNormalForm
d2 =  np.array([[0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,1,1],
                [0,0,1,0,1],
                [0,1,0,0,1],
                [1,0,0,0,1],
                [1,1,1,0,0],
                [1,1,0,0,0],
                [0,1,0,1,0],
                [0,0,1,1,0]])

d1 = np.array([[1,1,0,0,0,0,0,0,0,0],
              [1,0,1,1,0,0,0,0,0,1],
              [0,1,1,0,1,0,0,0,1,0],
              [0,0,0,1,0,1,1,0,0,0],
              [0,0,0,1,0,1,1,0,0,0],
              [0,0,0,0,0,0,1,1,1,1]])


smith = SmithNormalForm()
d2_snf = smith.smithify(d2)
d1_snf = smith.smithify(d1)
print(d2_snf)
print(d1_snf)