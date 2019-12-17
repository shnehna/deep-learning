import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVE:'] = '2'

with tf.compat.v1.Session() as sess:
    a = tf.constant("身份证再这")
    print(sess.run(a).decode("utf8"))
    print(a.name)
    # print(a.shape)
    # print(a.op)
    # print(a.dtype)
    # 形状的改变
    # 对于静态形状来说，形状一旦固定就不能更改
    plt = tf.compat.v1.placeholder(tf.float32, [None, 2])
    print(plt)
    plt.set_shape([3, 2])
    print(plt)
    # 动态形状 创建新的形状
    reshape = tf.reshape(plt, [2, 3])
    print(reshape)
