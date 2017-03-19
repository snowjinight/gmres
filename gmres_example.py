from gmrescrs import Gmres
from crsmatrix import Matrix
import numpy

A = Matrix.from_mm_file('data/bcsstk18.mtx')
b = numpy.ones((A.shape()[0], 1))
gmres = Gmres(A, b, max_iterations=320, restart_after=50)
output_vector, error = gmres.solve()
print error
