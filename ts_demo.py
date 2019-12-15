import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVE:'] = '2'

# 实现一个加法运算
a = tf.constant(5.0)
b = tf.constant(6.0)
sum1 = tf.add(a, b)
print(sum1)
tf.compat.v1.Session()

# 2.0版本
# with tf.compat.v1.Session()
# 1.14版本
# with tf.Session() as sess:
#     print(sess.run(sum1))
