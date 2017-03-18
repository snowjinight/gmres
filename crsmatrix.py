import numpy

class Matrix:
    # m x n matrix -- row major, 0 index
    def __init__(self, m, n, a, ia, ja):
        self.m = m
        self.n = n
        self.a = a
        self.ia = ia
        self.ja = ja

    # Length returns # of nonzero elements
    def __len__(self):
        return len(self.a)

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.m == other.m and \
            self.n == other.n and self.a == other.a and self.ia == other.ia and \
            self.ja == other.ja

    def __ne__(self, other):
        return not self.__eq__(other)


    def shape(self):
        return (self.m, self.n)

    # def transpose(self):
    #     m = self.n
    #     n = self.m
    #     a = []
    #     ia = []
    #     ja = []
    #     # lets build up a row
    #     for l in range(0, m):
    #         row_start = ia[m]
    #         row_end   = ia[m+1]
    #         if row_start == row_end:
    #             continue # no data in this row
    #         for k in range(row_start, row_end):     # not actually traversing
    #
    #     go by row
    #     check column of self accumulate row
    #         then adjust ia
    #         then set jas too on each (== to old row)

    # e.g. self * some_other
    def mult_left(self, other):
        print "who the f knows"

    @staticmethod
    def from_mm_file():
        print "who the f knows"

    # Vector should come in as numpy matrix
    # e.g. mat * vect
    def mult_left_vector(self, v):
        # a  -> nnz
        # ia -> m + 1
        # ja -> nnz
        vals = []
        for row in range(0, self.m):   # row
            summation = 0
            for l in range(self.ia[row], self.ia[row + 1]):  # j is used to fetch item and determine col
                col = self.ja[l]
                val = self.a[l]
                summation += float(v[col, 0]) * val
            vals.append(summation)
        return numpy.matrix(vals).T


    @staticmethod
    # Generate a useful, invertable tridiagonal matrix like:
    #   [ [  2, -1,  0 ],
    #     [ -1,  2, -1 ],
    #     [  0, -1,  2 ] ]
    # of any size.
    def tridiagonal(size = 10):
        sequence = [-1, 2, -1]
        a = sequence[1:]
        ia = [0, 2]
        ja = [0, 1]
        ia_sum = 2
        ja_ptr = 0  # what column are we inserting on?
        for i in range(1, size-1):
            print i
            ia_sum += 3
            ia.append(ia_sum)
            ja.append(ja_ptr)
            ja.append(ja_ptr + 1)
            ja.append(ja_ptr + 2)
            ja_ptr += 1
            a += sequence
        a += sequence[:-1]
        ia.append(len(a))
        ja += [size - 2, size - 1]
        return Matrix(size, size, a, ia, ja)
