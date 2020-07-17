import numpy
import scipy.special
import matplotlib.pyplot

# определение класса нейронной сети
class neuralNetwork:
	""" инициализация, тренировка и запрос нейронной сети """
	
	def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
		# задаётся количесто узлов во входном, скрытом и выходном слое
		self.inodes = inputnodes
		self.hnodes = hiddennodes
		self.onodes = outputnodes
	
		self.wih = numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes))
		self.who = numpy.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes))

		# кф обучения
		self.lr = learningrate

		self.activation_function = lambda x: scipy.special.expit(x)

		pass

	def train(self, inputs_list, targets_list):
		inputs = numpy.array(inputs_list, ndmin=2).T
		targers = numpy.array(targets_list, ndmin=2).T

		hidden_inputs = numpy.dot(self.wih, inputs)
		hidden_outputs = self.activation_function(hidden_inputs)

		final_inputs = numpy.dot(self.who, hidden_outputs)
		final_outputs = self.activation_function(final_inputs)

		output_errors = targers - final_outputs
		hidden_errors = numpy.dot(self.who.T, output_errors)

		self.who += self.lr * numpy.dot((output_errors * final_outputs * (1.0 - final_outputs)), numpy.transpose(hidden_outputs))
		self.wih += self.lr * numpy.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)), numpy.transpose(inputs))

		pass

	def query(self, inputs_list):
		inputs = numpy.array(inputs_list, ndmin=2).T

		hidden_inputs = numpy.dot(self.wih, inputs)
		hidden_outputs = self.activation_function(hidden_inputs)

		hidden_inputs = numpy.dot(self.wih, inputs)
		hidden_outputs = self.activation_function(hidden_inputs)

		final_inputs = numpy.dot(self.who, hidden_outputs)
		final_outputs = self.activation_function(final_inputs)
		
		print(final_outputs)


input_nodes = 784
hidden_nodes = 100
output_nodes = 10

learning_rate = 0.3

n = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)

training_data_file = open("mnist_dataset/mnist_train_100.csv", 'r')
training_data_list = training_data_file.readlines()
training_data_file.close()

for record in training_data_list:
	all_values = record.split(',')
	inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01

	targers = numpy.zeros(output_nodes) + 0.01

	targers[int(all_values[0])] = 0.99
	n.train(inputs, targers)
	pass

test_data_file = open("mnist_dataset/mnist_test_10.csv", 'r')
test_data_list = test_data_file.readlines()
test_data_file.close()

all_values = test_data_list[0].split(',')
n.query((numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01)
