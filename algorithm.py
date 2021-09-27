import numpy as np


class MatrixOperations():
    def _add_row(self, mat, i, j):
        mat[i, :] = (mat[i, :] + mat[j, :]) % 2
        return mat

    def _flip_rows(self, mat, i, j):
        mat[[i,j]] = mat[[j,i]] 
        return mat

    def _add_col(self, mat, i, j):
        mat[:, i] = (mat[:, i] + mat[:, j] ) % 2
        return mat  

    def _flip_cols(self, mat, i, j):
        mat[:, [i,j]] = mat[:, [j,i]] 
        return mat

class SmithNormalForm(MatrixOperations):
    def smithify(self, mat, i=0):
        snf = self.do_smithing(mat, i)

        return snf

    def do_smithing(self, mat, i):
        m, n = mat.shape
        
        found_ones = np.where(mat[i:, i:] == 1)


        if found_ones[0].size:
            j,k = found_ones[0][0]+i, found_ones[1][0]+i

            if (j,k) != (i,i):
                mat = self._flip_rows(mat, i, j)
                mat = self._flip_cols(mat, i, k)

            for h in range(i+1, m):
                # Zero out row
                if mat[h,i] == 1:
                    mat = self._add_row(mat, h, i)
        
            for l in range(i+1, n):
                # Zero out column
                if mat[i,l] == 1:
                    mat = self._add_col(mat, l, i)
            mat = self.do_smithing(mat, i+1)
    
        return mat

  