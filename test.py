import ctypes
import numpy as np
import glob
import time
# find the shared library, the path depends on the platform and Python version
libfile = glob.glob('build/*/mysum*.so')[0]

# 1. open the shared library
mylib = ctypes.CDLL(libfile)

#input n
#output array
# t1=time.time()
# mylib.create_array.restype=np.ctypeslib.ndpointer(dtype=np.int32,shape=(11,))
# mylib.create_array.argtypes=[ctypes.c_int32]

# array = mylib.create_array(11)
# print(time.time()-t1)

# print(array)



#---------------------------------------------------------------------------------
# input int , array
# output int 
array=list(range(0,1000000000))
array = np.array(array,dtype=np.int32)

t1=time.time()
array.sum()
print(time.time()-t1)

t1=time.time()
mylib.mysum.restype = ctypes.c_longlong
mylib.mysum.argtypes = [ctypes.c_int, 
                        np.ctypeslib.ndpointer(dtype=np.int32)]



array_sum = mylib.mysum(len(array), array)

print(time.time()-t1)


#----------------------------------------------------------------------------------------------
#string
# hao="hao"
# mutable_string = ctypes.create_string_buffer(str.encode(hao))

# print("Before:", mutable_string.value)
# mylib.add_one_to_string(mutable_string)  # Works!
# print("After: ", mutable_string.value)