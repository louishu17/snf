import numpy as np
from algorithm import SmithNormalForm
bm =  np.array([[0,0,0,0,0],
                [0,0,0,0,0],
                [],
                [0, 0, 0, 1, 0, 1, 1],
                [0, 0, 0, 0, 1, 0, 1]])


smithers = SmithNormalForm()
bm_snf = smithers.smithify(bm)
print(bm_snf)