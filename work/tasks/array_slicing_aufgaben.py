import numpy as np

b = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
              [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
              [[19, 20, 21], [22, 23, 24], [25, 26, 27]]])
print(b[0,:,:])
print(b[1,1,:])
print(b[:,:,2])
print(b[:2,:,:])
print(b[0,:,:2])
print(b[2,1,1])
print(b[[0, 2], :, :])
print(b[:, :, 1:])
print(b[1, :, 2])
print(b[:2, 1, :])
array = np.random.rand(4, 5, 6)
print(array[[0,2],0,:])
print(array[1,:,1])
print(array[1:3,:,0:2])
print(array[0,1,2:6])
print(array[:2,0:2,0:2 ])
print(array[:,-1:,::-1 ])
print(array[:3,::2,: ])
