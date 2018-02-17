
# coding: utf-8

# In[11]:


import numpy as np
import tensorflow as tf


# In[33]:


coefficients = np.array([[1.],[-20.],[100.]])

w = tf.Variable(0,dtype=tf.float32)
x = tf.placeholder(tf.float32, [3,1])
cost = x[0][0]*w**2 + x[1][0]*w + x[2][0]
train = tf.train.GradientDescentOptimizer(0.01).minimize(cost)

init = tf.global_variables_initializer()
session = tf.Session()
session.run(init)
print(session.run(w))


# In[34]:


session.run(train, feed_dict={x:coefficients})
print(session.run(w))


# In[35]:


for i in range(1000):
    session.run(train, feed_dict={x:coefficients})
print(session.run(w))

