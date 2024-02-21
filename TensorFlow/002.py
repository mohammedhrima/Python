import tensorflow as tf
import os

from tensorflow.python.ops.gen_math_ops import add
os.environ['TF_CPP_MIN_LOG_LEVEL'] ='2'

#initialization of Tensors
x = tf.constant(4,shape=(1,1),dtype=tf.float32)
x = tf.constant([[1,2,3],[4,5,6]])
x = tf.ones((3,3))
x = tf.zeros((3,3))
x = tf.eye(3) # I for the identity matrix
x = tf.random.normal((3,3), mean=0,stddev=1)
x = tf.random.uniform((1,3),minval=0,maxval=1)
x = tf.range(9)
x = tf.range(start=1,limit=10, delta=3)
x = tf.cast(x,dtype=tf.float64)

#Mathematical Operations
x = tf.constant([1,2,3])
y = tf.constant([9,8,7])

z = tf,add(x,y)
z = x+y

z = tf.subtract(x,y)
z = x - y

z = tf.divide(x,y)
z = x/y

z = tf.multiply(x,y)
z=x*y

z = tf.tensordot(x,y,axes = 1)

print(z)
#indexing
#Reshaping
