import tensorflow.compat.v2 as tf
import tensorflow.keras.backend as K
import math
    

def perplexity(y_true, y_pred):
    cross_entropy = K.sparse_categorical_crossentropy(y_true, y_pred)
    _perplexity = K.pow(2.0, cross_entropy)
    return _perplexity


def bpc(y_true, y_pred):
    cross_entropy = K.sparse_categorical_crossentropy(y_true, y_pred)
    _bpc = cross_entropy / 0.69314718056 # ln2
    return _bpc
    
    
class NoamSchedule(tf.keras.optimizers.schedules.LearningRateSchedule):
    def __init__(self, d_model, warmup_steps=4000):
        super(NoamSchedule, self).__init__()
        self.warmup_steps = warmup_steps
        self.k = self.warmup_steps**-1.5
        self.sqrt_d_model = 1/(d_model**0.5)

    def __call__(self, step):
        arg1 = tf.math.rsqrt(step)
        arg2 = step * (self.k)
        return self.sqrt_d_model * tf.math.minimum(arg1, arg2)
    