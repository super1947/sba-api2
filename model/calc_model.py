import tensorflow.compat.v1 as tf

class CalculatorModel:
  
  def create_add_model(self):
    w1 = tf.placeholder(tf.float32, name='w1')
    w2 = tf.placeholder(tf.float32, name='w2')
    feed_dict = {'w1': 8.0, 'w2': 2.0}
    r = tf.add(w1, w2, name='op_add')
    sess = tf.Session()
    _ = tf.Variable(initial_value = 'fake_variable')
    sess.run(tf.global_variables_initializer())
    saver = tf.train.Saver()
    print(f"feed_dict['w1'] : {feed_dict['w1']}")
    print(f"feed_dict['w2'] : {feed_dict['w2']}")
    result = sess.run(r, {w1: feed_dict['w1'], w2: feed_dict['w2']})
    print(f'TF add result : {result}')
    saver.save(sess, 'model\calc_add\model', global_step=1000)

  def create_sub_model(self):
    w1 = tf.placeholder(tf.float32, name='w1')
    w2 = tf.placeholder(tf.float32, name='w2')
    feed_dict = {'w1': 8.0, 'w2': 2.0}
    r = tf.subtract(w1, w2, name='op_sub')
    sess = tf.Session()
    _ = tf.Variable(initial_value = 'fake_variable')
    sess.run(tf.global_variables_initializer())
    saver = tf.train.Saver()
    print(f"feed_dict['w1'] : {feed_dict['w1']}")
    print(f"feed_dict['w2'] : {feed_dict['w2']}")
    result = sess.run(r, {w1: feed_dict['w1'], w2: feed_dict['w2']})
    print(f'TF sub result : {result}')
    saver.save(sess, 'model\calc_sub\model', global_step=1000)

  def create_mul_model(self):
    w1 = tf.placeholder(tf.float32, name='w1')
    w2 = tf.placeholder(tf.float32, name='w2')
    feed_dict = {'w1': 8.0, 'w2': 2.0}
    r = tf.multiply(w1, w2, name='op_mul')
    sess = tf.Session()
    _ = tf.Variable(initial_value = 'fake_variable')
    sess.run(tf.global_variables_initializer())
    saver = tf.train.Saver()
    print(f"feed_dict['w1'] : {feed_dict['w1']}")
    print(f"feed_dict['w2'] : {feed_dict['w2']}")
    result = sess.run(r, {w1: feed_dict['w1'], w2: feed_dict['w2']})
    print(f'TF mul result : {result}')
    saver.save(sess, 'model\calc_mul\model', global_step=1000)

  def create_div_model(self):
    w1 = tf.placeholder(tf.float32, name='w1')
    w2 = tf.placeholder(tf.float32, name='w2')
    feed_dict = {'w1': 8.0, 'w2': 2.0}
    r = tf.math.floordiv(w1, w2, name='op_sub')
    sess = tf.Session()
    _ = tf.Variable(initial_value = 'fake_variable')
    sess.run(tf.global_variables_initializer())
    saver = tf.train.Saver()
    print(f"feed_dict['w1'] : {feed_dict['w1']}")
    print(f"feed_dict['w2'] : {feed_dict['w2']}")
    result = sess.run(r, {w1: feed_dict['w1'], w2: feed_dict['w2']})
    print(f'TF div result : {result}')
    saver.save(sess, 'model\calc_div\model', global_step=1000)

if __name__ == "__main__":
    c = CalculatorModel()
    c.create_div_model()

