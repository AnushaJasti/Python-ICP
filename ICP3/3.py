import numpy as np

a=np.random.randint(0,high=20,size=15,dtype=np.int32)
print(a)
print(np.bincount(a).argmax())