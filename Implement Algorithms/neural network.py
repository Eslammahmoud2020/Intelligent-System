import numpy as np

# Step Function
def step_function(x):
    return np.where(x >= 0, 1, 0)

# Training data for OR Gate
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # Input data
y = np.array([0, 1, 1, 1])  # OR Gate output

# Initialize weights and bias
weights = np.random.rand(2)
bias = np.random.rand()

# Learning rate
lr = 0.1

# Training the network
epochs = 100
for epoch in range(epochs):
    total_error = 0
    for i in range(len(X)):
        # Compute weighted sum
        z = np.dot(X[i], weights) + bias
        # Apply activation function
        output = step_function(z)
        # Compute error
        error = y[i] - output
        total_error += abs(error)
        # Update weights and bias manually
        weights += lr * error * X[i]
        bias += lr * error
    # If the network learns the OR gate early, stop
    if total_error == 0:
        print(f"Training completed in {epoch + 1} epochs.")
        break
else:
    print("Training completed.")

# Testing the model
print("Testing OR Gate predictions:")
for i in range(len(X)):
    z = np.dot(X[i], weights) + bias
    output = step_function(z)
    print(f"Input: {X[i]}, Predicted Output: {output}, Expected Output: {y[i]}")
