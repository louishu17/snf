import numpy as np
from algorithm import SmithNormalForm

d1 = np.array([[0,0,0,1,1,0,0,0],
               [1,0,1,1,0,1,0,0],
               [0,1,1,0,1,0,0,1],
               [1,1,0,0,0,0,1,0],
               [0,0,0,0,0,1,1,1]])
d2 = np.array([[1,0,0,1],
                [0,0,1,1],
                [0,1,0,1],
                [0,0,0,0],
                [0,0,0,0],
                [1,1,0,0],
                [1,0,1,0],\
                [0,1,1,0]])

smith = SmithNormalForm()
d1_snf = smith.smithify(d1)
d2_snf = smith.smithify(d2)
print(d1_snf)
print(d2_snf)