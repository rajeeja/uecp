## This python script is created by the RGG AssyGen program in MeshKit ##
# Here the RGG AssyGen program creates the assembly geometry and mesh
#
import cubit
cubit.cmd('import \'in3.sat\'')
## ***** manual volume numbers ****
cubit.cmd('create brick x 3.78 y 3.78  z 1')
cubit.cmd('create brick x 3.9 y 3.9  z 1')
cubit.cmd('move vol 48 z 0.5')
cubit.cmd('move vol 49 z 0.5')
cubit.cmd('subtract vol 48 from vol 49 ')

# deleting inner control assemblies
cubit.cmd('#')
cubit.cmd('####')
cubit.cmd('group \'tmpgrp\' add body with name \'extramat\'')
cubit.cmd('delete body in tmpgrp')
cubit.cmd('####')


## ***** manual pitch/2 as pit and number rings ****
n = 3
pit = 0.63
# dont use side_edge

## ***** manual used of edge ****
for i in range(n):
         cubit.cmd('create curve offset curve 286 distance {0} extended'.format((2*i+1)*pit) )
         cubit.cmd('create curve offset curve 290 distance {0} extended'.format((2*i+1)*pit) )

cubit.cmd('create curve location {0} {0} 1.0 location -{0} -{0} 1.0'.format(n*pit) )
cubit.cmd('create curve location {0} -{0} 1.0 location -{0} {0} 1.0'.format(n*pit) )

for i in range((n-1)/2):
       cubit.cmd('create curve location {0} {1} 1.0  location {1} {0} 1.0'.format(-(2*i+1)*pit ,-n*pit) )
       cubit.cmd('create curve location {0} {1} 1.0  location {1} {0} 1.0'.format(n*pit,-(2*i+1)*pit) )
##
       cubit.cmd('create curve location {0} {1} 1.0  location {1} {0} 1.0'.format((2*i+1)*pit ,-n*pit) )
       cubit.cmd('create curve location {0} {1} 1.0  location {1} {0} 1.0'.format(n*pit,(2*i+1)*pit) )
####
####
       cubit.cmd('create curve location {0} {1} 1.0  location {2} {3} 1.0'.format(-(2*i+1)*pit ,-n*pit, n*pit,  (2*i+1)*pit) )
       cubit.cmd('create curve location {0} {1} 1.0  location {2} {3} 1.0'.format(n*pit,-(2*i+1)*pit,  (2*i+1)*pit, -n*pit) )
##
       cubit.cmd('create curve location {0} {1} 1.0  location {2} {3} 1.0'.format(-n*pit, (2*i+1)*pit , -(2*i+1)*pit, n*pit) )
       cubit.cmd('create curve location {0} {1} 1.0  location {2} {3} 1.0'.format(-n*pit, -(2*i+1)*pit, (2*i+1)*pit, n*pit) )
### 

cubit.cmd('export acis "geom_3x3.sat" over')
exit()
