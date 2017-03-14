
n = 17
pit = 0.62992
# dont use side_edge
for i in range(n):
         cubit.cmd('create curve offset curve with name "side_edge4" distance {0} extended'.format(-(2*i+1)*pit) )
         cubit.cmd('create curve offset curve with name "side_edge3" distance {0} extended'.format(-(2*i+1)*pit) )

cubit.cmd('delete free curve all')
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

cubit.cmd('dr curve with length > 5 and z_coord = 1')



