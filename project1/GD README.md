Linear Regression Model using Greatest Descent method:

Gradient descent is an first-order optimization algorithm used to find the values of parameters (coefficients) of a function (f) that minimizes a cost function. It only takes into account the first derivative when performing the updates on the parameters. On each iteration, the parameters are updated. 


Advantages:
1)It does not use much memory and it cannot be optimized.
2)The run time of iteration is typically just O(n). 


Disadvantages:
1) The number of iterations largely depends on the scale of the problem so that may cause inaccuracy. 
2) If the learning rate is too fast, it is possible to skip the local minimum. If the learning rate is too slow, the gradient descent may never converge. Therefore the learning rate may affect the minimum. 
