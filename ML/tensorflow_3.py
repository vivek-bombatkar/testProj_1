import tensorflow as tf

# creates nodes in a graph
# "construction phase"
x1 = tf.constant([5,3])
x2 = tf.constant([6,4])

print(tf.multiply(x1,x2))