import tensorflow as tf

# 在eager模式下可以直接进行运算
x = [[3.]]
m = tf.matmul(x, x)
print(m.numpy())

a = tf.constant([[1,9],[3,6]])
print(a)

b = tf.add(a, 2)
print(b)
print(a*b)

import numpy as np
s = np.multiply(a,b)
print(s)
