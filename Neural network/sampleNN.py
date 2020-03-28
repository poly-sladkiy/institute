import numpy as np

def sigmoid(x):
  return 1 / (1 + np.exp(-x))

train_inputs = np.array([[0,0,1],
                         [1,1,1],
                         [1,0,1],
                         [0,1,1]])

train_outputs = np.array([[0,1,1,0]]).T

np.random.seed(1)

synapsic_weights = 2 * np.random.random((3,1)) - 1

print("Случайные инициализирующие веса:")
print(synapsic_weights)

for i in range(20000):
  input_layer = train_inputs
  outputs = sigmoid(np.dot(input_layer, synapsic_weights))

  err = train_outputs - outputs
  adjustment = np.dot(input_layer.T, err * (outputs * (1 - outputs)))

  synapsic_weights += adjustment
 
print("Веса после обучения:")
print(synapsic_weights)

print("Результат после обучения:")
print(outputs)

new_inputs = np.array([1,1,0])
outputs = sigmoid(np.dot(new_inputs, synapsic_weights))

print("Новая ситуация:")
print(outputs)

