import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf

# Build and compile the simple linear regression model
def build_model(learning_rate):
    """Create and compile a simple linear regression model."""
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Dense(units=1, input_shape=(1,)))
    model.compile(optimizer=tf.keras.optimizers.RMSprop(lr=learning_rate), 
                  loss="mean_squared_error", 
                  metrics=[tf.keras.metrics.RootMeanSquaredError()])
    return model

# Train the model on the feature and label data
def train_model(model, feature, label, epochs, batch_size):
    """Train the model by feeding it data."""
    history = model.fit(feature, label, batch_size=batch_size, epochs=epochs)
    trained_weight = model.get_weights()[0][0][0]
    trained_bias = model.get_weights()[1][0]
    rmse = pd.DataFrame(history.history)["root_mean_squared_error"]
    return trained_weight, trained_bias, history.epoch, rmse

# Plot the trained model against the training feature and label
def plot_model(trained_weight, trained_bias, feature, label):
    """Plot the trained model against the training feature and label."""
    plt.scatter(feature, label, label="Training Data")
    plt.xlabel("Feature")
    plt.ylabel("Label")
    x_start = 0
    y_start = trained_bias
    x_end = feature[-1]
    y_end = trained_bias + (trained_weight * x_end)
    plt.plot([x_start, x_end], [y_start, y_end], color='red', label="Trained Model")
    plt.legend()
    plt.show()

# Plot the root mean squared error during training
def plot_loss_curve(epochs, rmse):
    """Plot the loss curve, which shows loss vs. epoch."""
    plt.plot(epochs, rmse, label="Root Mean Squared Error")
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.legend()
    plt.ylim([rmse.min() * 0.97, rmse.max()])
    plt.show()

# Define the feature and label data

feature = ([1.0, 2.0,  3.0,  4.0,  5.0,  6.0,  7.0,  8.0,  9.0, 10.0, 11.0, 12.0])
label   = ([5.0, 8.8,  9.6, 14.2, 18.8, 19.5, 21.4, 26.8, 28.9, 32.0, 33.8, 38.2])

learning_rate=.5
epochs=10
my_batch_size=12

my_model = build_model(learning_rate)
trained_weight, trained_bias, epochs, rmse = train_model(my_model, feature, 
                                                         label, epochs,
                                                         my_batch_size)
plot_model(trained_weight, trained_bias, feature, label)
plot_loss_curve(epochs, rmse)