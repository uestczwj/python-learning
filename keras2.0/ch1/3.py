class MyLayer(layers.Layer):
    def __init__(self, output_dim, **kwargs):
        self.output_dim = output_dim
        super(MyLayer, self).__init__(**kwargs)
        def build(self, input_shape):
            shape = tf.TensorShape((input_shape[1], self.output_dim))
            self.kernel = self.add_weight(name='kernel1', shape=shape, initializer='uniform', trainable=True)
            super(MyLayer, self).build(input_shape)
            def call(self, inputs):
                return tf.matmul(inputs, self.kernel)

            def compute_output_shape(self, input_shape):
                shape = tf.TensorShape(input_shape).as_list()
                shape[-1] = self.output_dim
                return tf.TensorShape(shape)

            def get_config(self):
                base_config = super(MyLayer, self).get_config()
                base_config['output_dim'] = self.output_dim
                return base_config @classmethod

            def from_config(cls, config):
                return cls(**config)

model = tf.keras.Sequential(
[
    MyLayer(10), layers.Activation('softmax')
])

model.compile(optimizer=tf.keras.optimizers.RMSprop(0.001), loss=tf.keras.losses.categorical_crossentropy, metrics=['accuracy'])
model.fit(train_x, train_y, batch_size=16, epochs=5)
