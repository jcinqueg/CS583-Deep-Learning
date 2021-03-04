import numpy as np

x = np.asarray( [-1,0,1,2,3,4] )

a = np.array( [-2, -1, 0, 1, 2])
b = a * a
c = np.sum(b)
print( c )

x = np.asarray( [-3,-1,0,2] )
y = np.asarray( [4,-2,-4,-1] )

print( np.inner( x, y ) )

print( np.dot(x, y) )

print( np.dot( np.transpose(x), y ))