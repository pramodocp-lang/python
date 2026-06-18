import numpy as np


ma = np.array([
[1,2],
[3,4]

])


mb = np.array([
[5,6],
[7,8]

])


mc = np.array([
[9,10],
[11,12]

])


md = np.array([
[13,14],
[15,16]

])



print("\n\n Matrix A\n")
print("\n\n Matrix A + B \n", ma + mb )
print("\n\n Matrix A - B \n", ma - mb )
print("\n\n Matrix A + B + C \n", ma + mb + mc)
print("\n\n Matrix A + B + C + D \n", ma + mb + mc + md)
print("\n\n Matrix A*B \n", ma * mb)






