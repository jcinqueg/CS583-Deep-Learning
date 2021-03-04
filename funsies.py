import numpy as np

x = np.asarray( [3, -10, 9, 0, -2])
a = np.asarray( [0,9,-3,-2,1] )

print( "l 1/2 norm")
print( np.linalg.norm( x, 0.5 ) )
print()

print( "l 1 norm")
print( np.linalg.norm( x, 1) )
print()

print( "Manhattan Distance" )
print( np.linalg.norm( x - a, 1))