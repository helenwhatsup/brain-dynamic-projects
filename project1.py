import numpy as np
import matplotlib.pyplot as plt


x = np.loadtxt('ex2x.csv')
y = np.loadtxt('ex2y.csv')

print (x)
print (y)

def estimate_coef(x, y):
    a = np.size(x)
    mx = np.mean(x)
    my = np.mean(y)
    # calculating cross-deviation and deviation about x

    Sxy = np.sum((y-my)*(x-mx))
    Sxx = np.sum((x-mx)*(x-mx))

    # calculating regression coefficients
    b_1 = Sxy / Sxx
    b_0 = my - b_1 * mx

    return (b_0, b_1)

(b_0,b_1) = estimate_coef(x,y)

# plot
plt.scatter(x,y, color = "m", marker = "o", s = 50)

# predicted response vector
y_pred = b_0 + b_1 * x

# plotting the regression line
plt.plot(x, y_pred, color="g")
plt.xlabel('x')
plt.ylabel('y')

plt.show()

# predicted response vector
    #y_pred = b[0] + b[1] * x

    # plotting the regression line
  #  plt.plot(x, y_pred, color="g")

    # putting labels
   # plt.xlabel('x')
    #plt.ylabel('y')


