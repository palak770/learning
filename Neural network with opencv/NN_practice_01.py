import math

# Inputs
x = [2, 3]

# Weights
w = [0.5, -0.5]

# Bias
b = 0.1

# Sigmoid activation function
def sigmoid(z):
    return 1 / (1 + math.exp(-z))

# Weighted sum
z = x[0]*w[0] + x[1]*w[1] + b

# Output after activation
output = sigmoid(z)

print("Neuron output:", output)


x = [1, 2]

w1 = [0.5, -0.5]
b1 = 0.1

w2 = [-0.3, 0.8]
b2 = 0.2

def sigmoid(z):
    return 1 / (1 + math.exp(-z))

# First neuron
z1 = x[0]*w1[0] + x[1]*w1[1] + b1
output1 = sigmoid(z1)
# Second neuron
z2 = x[0]*w2[0] + x[1]*w2[1] + b2
output2 = sigmoid(z2)
# Final output
print("Output of neuron 1:", output1)
print("Output of neuron 2:", output2)

