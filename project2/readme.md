How neural networks can be seen as an extension of linear regression problem?

In ANN, we can use logistic regression to aproximate data with sigmoid curve because neural network is just a set of functions which approximate input data, and each node's output can be regarded as a function of its forwarded data. 

If we have function f1(i1, i2) = w11 * i1 + w12 * i2 + c. Such model is a linear regression model for multiple inputs and it can be represented as multilinear regression.For different architecture of model, we'll have different kinds of linear regression.

Backpropagation can be expressed as “layer by layer” gradient descent, because we need to compute the derivative of the function represented by the network with respect to each of the weights. We rely on the fact that the derivatives with respect to the weights at a given layer can be expressed as a function of the derivatives with respect to the weights of the next level,and the value that take the neuron during the forward pass.Therefore, we start by computing the forward pass that take the neuron onward. Then we go back to compute the derivatives of the error with repespect of the last layer. Then we'll compute the derivatives with the previous layer and go backward to reach the first layer.
