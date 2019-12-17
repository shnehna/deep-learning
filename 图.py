import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVE:'] = '2'

# 创建一张图
# op:只要使用tensorflowAPI定义的接口都是OP
# tensor：张量，代表数据
# g = tf.Graph()
# print(g)
# with g.as_default():
#     c = tf.constant(11.0)
#     print(c.graph)

# 实现一个加法运算
# a = tf.constant(5.0)
# b = tf.constant(6.0)
# sum1 = tf.add(a, b)
# print(sum1)
# tf.get_default_graph() 非2.0版本
# graph = tf.compat.v1.get_default_graph()
# print(graph)

# placeholder是一个占位符
with tf.compat.v1.Session(config=tf.compat.v1.ConfigProto(log_device_placement=True)) as sess:
    a = tf.constant(5.0)
    b = tf.constant(6.0)
    sum1 = tf.add(a, b)
    placeholder = tf.compat.v1.placeholder(tf.float32, [None, 3])
    print(sum1)
    print(sess.run(sum1))
    print(sess.run(placeholder, feed_dict={placeholder: [[1, 2, 3], [4, 5, 34], [12, 1234, 112]]}))

# 2.0版本
# with tf.compat.v1.Session()
# 1.14版本
# with tf.Session() as sess:
#     print(sess.run(sum1))
