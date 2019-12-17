import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVE:'] = '2'
# python -m tensorboard.main --logdir="./"
# 变量op
a = tf.constant(3.0, name='a')
b = tf.constant(4.0, name='b')
c = tf.add(a, b, name='add')

var = tf.Variable(tf.random_normal([2, 3], mean=0.0, stddev=1.0, name='variable'))
print(a, var)
# 必须做一部显式的初始化
init_op = tf.global_variables_initializer()
with tf.Session() as sess:
    # 必须运行初始化操作
    sess.run(init_op)
    print(sess.run([c, var]))
    # 把程序写入事件文件
    file_writer = tf.summary.FileWriter("./temp/summary/test", graph=sess.graph)
