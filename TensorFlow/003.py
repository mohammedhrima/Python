import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] ='2'
import tensorflow as tf
#the next 2 lines for errors
"""physical_devices = tf.config.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(physical_devices[0],True)"""



#Initialization of tensors
x = tf.constant(4,shape=(1,1),dtype=tf.float32) #tf.Tensor([[4.]], shape=(1, 1), dtype=float32)
x = tf.constant([[1,2,3],[4,5,6]]) #tf.Tensor([[1 2 3][4 5 6]], shape=(2, 3), dtype=int32)
x = tf.ones((3,3)) #tf.Tensor([[1 2 3][4 5 6]], shape=(2, 3), dtype=int32)
x = tf.zeros((2,3)) #tf.Tensor([[0. 0. 0.][0. 0. 0.]], shape=(2, 3), dtype=float32)
x = tf.eye(3) #tf.Tensor([[1. 0. 0.][0. 1. 0.][0. 0. 1.]], shape=(3, 3), dtype=float32)
x = tf.random.normal((3,3),mean=0,stddev=1)
x = tf.random.uniform((2,2),minval=0,maxval=1)
x = tf.range(9) #tf.Tensor([0 1 2 3 4 5 6 7 8], shape=(9,), dtype=int32)
x = tf.range(start=1,limit=10,delta=2) #tf.Tensor([1 3 5 7 9], shape=(5,), dtype=int32)
x = tf.cast(x,dtype=tf.float64) 
"tf.float(16,32,64), tf.int(8,16,32,64, tf.bool"
##print(x)

#Mathematical Operations
x = tf.constant([1,2,3])
y = tf.constant([9,8,7])

z = tf.add(x,y) #tf.Tensor([10 10 10], shape=(3,), dtype=int32)
z = x + y #tf.Tensor([10 10 10], shape=(3,), dtype=int32)

z = tf.subtract(x,y) #tf.Tensor([-8 -6 -4], shape=(3,), dtype=int32)
z = x-y #tf.Tensor([-8 -6 -4], shape=(3,), dtype=int32)

z = tf.divide(x,y) #tf.Tensor([0.11111111 0.25       0.42857143], shape=(3,), dtype=float64)
z = x/y #tf.Tensor([0.11111111 0.25       0.42857143], shape=(3,), dtype=float64)

z = tf.multiply(x,y) #tf.Tensor([ 9 16 21], shape=(3,), dtype=int32)
z = x*y #tf.Tensor([ 9 16 21], shape=(3,), dtype=int32)

z = tf.tensordot(x,y,axes=1) #tf.Tensor(46, shape=(), dtype=int32)
z = tf.reduce_sum(x*y,axis=0) #tf.Tensor(46, shape=(), dtype=int32)

z = x**5 #tf.Tensor([  1  32 243], shape=(3,), dtype=int32)

x = tf.random.normal((2,3))
y = tf.random.normal((3,4))
z = tf.matmul(x,y)
##print(z)

#Indexing
x = tf.constant([0,1,1,2,3,1,2,3])
#print(x[:]) #tf.Tensor([0 1 1 2 3 1 2 3], shape=(8,), dtype=int32)
#print(x[1:]) #f.Tensor([1 1 2 3 1 2 3], shape=(7,), dtype=int32)
#print(x[1:3]) #tf.Tensor([1 1], shape=(2,), dtype=int32)
#print(x[::2]) #tf.Tensor([0 1 3 2], shape=(4,), dtype=int32)
#print(x[::-1]) #tf.Tensor([3 2 1 3 2 1 1 0], shape=(8,), dtype=int32)
indices = tf.constant([0,3])
x_ind = tf.gather(x,indices)
#print(x_ind) #tf.Tensor([0 2], shape=(2,), dtype=int32)
x = tf.constant([[1,2],[3,4],[5,6]]) 
#print(x[0,:]) #tf.Tensor([1 2], shape=(2,), dtype=int32)
#print(x[0:2,:]) #tf.Tensor([[1 2][3 4]], shape=(2, 2), dtype=int32)

#Reshaping
x = tf.range(9) #tf.Tensor([0 1 2 3 4 5 6 7 8], shape=(9,), dtype=int32)
x = tf.reshape(x,(3,3)) #tf.Tensor([[0 1 2][3 4 5][6 7 8]], shape=(3, 3), dtype=int32)
x = tf.transpose(x,perm=[1,0]) #tf.Tensor([[0 3 6][1 4 7][2 5 8]], shape=(3, 3), dtype=int32)

print(x) 























