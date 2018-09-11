#!/usr/bin/python
import numpy as np
class Network:
    def __init__(self, input_d, output_d, hnum_layers):
        self.num_layers = 1 + hnum_layers
        self.layers = [None] * self.num_layers
        self.layers[self.num_layers - 1] = Layer(output_d, 4)
        self.layers[0] = Layer(4, input_d)
        for ii in xrange(1, hnum_layers):
            self.layers[ii] = Layer(4, self.layers[ii - 1].num_layer_nodes) 

    def train(self, matrix, output):
        for ii in xrange(0, len(matrix)):
            self.backprop(matrix[ii], output[ii])
        
    def propagate(self, data):
        data[0] = (data[0] - 5500.0)/9000.0
        data[1] = (data[1] - 110.0)/180.0
        data[2] = float(data[2]) 
        data[3] = float(data[3])
        out = np.array(data)[np.newaxis].T
        for ii in self.layers:
            ii.inp = out
            net = np.dot(ii.weights, out) + ii.biases.T
            out = self.sig(net)
        return out

    def backprop(self, input_data, output_data):
        result = self.propagate(input_data)
        temp = 2 * (np.array(output_data)[np.newaxis].T - result) * self.dsig(result)  
        for ii in reversed(self.layers):
            delta = np.dot(temp, ii.inp.T )
            ii.weights += delta
            ii.biases += temp.T
            temp = np.dot(ii.weights.T, temp) * self.dsig(ii.inp)

    @staticmethod
    def sig(x):
        return 1.0 / (1.0 + np.exp(-x))
    @staticmethod
    def dsig(x):
        return x * (1.0 - np.array(x))

class Layer:
    def __init__(self, num, prior_num):
        self.num_layer_nodes = num
        self.weights = np.random.rand(num, prior_num)
        self.biases = np.array(np.random.rand(num))[np.newaxis]
        self.net = self.out = self.inp = None

nn = Network(4, 3, 1) 
#matrix = [[243, 232],[57, 178],[89, 108],[10, 255],[167, 148]]
#output = [1, 0, 1, 0, 1]
matrix = [[9000, 150, 1, 1], [9500, 180, 1, 0], [8500, 160, 1, 1], [5400, 95, 1, 0], [6000, 90, 1, 0], [5500, 105, 0, 1], [2000, 50, 0, 0], [1500, 35, 0, 1], [2200, 29, 0, 0]]
output =[]
temp = [1, 0, 0]
for ii in xrange(3):
    for jj in xrange(3):
        output.append(temp)
    if ii is 0:
        temp = [0, 1, 0]
    else:
        temp = [0, 0, 1]
for ii in xrange(1000):
    nn.train(matrix, output)
#test = [[123, 156],[43,200],[89,73]]
test = [[10000, 160, 1, 1], [6500, 110, 1, 0], [3000, 50, 0, 0]]
for ii in test:
    print(nn.propagate(ii))
