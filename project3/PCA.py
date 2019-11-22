import numpy as np
import matplotlib.pyplot as plt
from numpy import mean
from numpy import cov
from sklearn.decomposition import PCA
import math as m

pca = PCA(n_components=2)

rng = np.random.RandomState(1)
X = np.dot(rng.rand(2, 2), rng.randn(2, 200)).T
plt.scatter(X[:, 0],X[:, 1], color = "m", marker = "o", s = 100)
#Qa plot data
plt.show()
print(X)
pca.fit(X)


#Qb Plot the principle axes of the data.
a=X[:, 0]
b=X[:, 1]

M = mean(X.T, axis=1)
print(M)
C = X - M
print(C)
V = cov(C.T)
print("covaraince matrix")
print(V)


#cov_mat = np.stack((a, b), axis=0)
#print("coveriance matrix:")
#print(np.cov(cov_mat))
# calculate the mean of each column
# center columns by subtracting column means
# calculate covariance matrix of centered matrix
#q = np.array([[0.68217761,0.23093475],[0.23093475,0.09883179]])
val, vec = np.linalg.eig(V)
print("eigenvalues:")
print(val)
print("eigenvectors:")
print(vec)

print("eigenvectors PCA：")
print(pca.components_)
print("eigenvalues PCA：")
print(pca.explained_variance_)


def draw_vector(v0, v1, ax=0):
    ax = plt.gca()
    arrowprops=dict(arrowstyle='->',linewidth=3, shrinkA=0, shrinkB=0)
    ax.annotate('', v1, v0, arrowprops=arrowprops)

# plot data
plt.scatter(X[:, 0], X[:, 1], alpha=0.2)
for length, vector in zip(pca.explained_variance_, pca.components_):
    p = vector * 3 * np.sqrt(length)
    draw_vector(M, M+ p)
plt.axis('equal');
plt.show()

#transform data using pca
# project data
P = vec.T.dot(C.T)
print("transformed data obtained from PCA")
print(P.T)
P1=P.T[:,0]
P2=P.T[:,1]

plt.scatter(X[:, 0],X[:, 1], color = "m", marker = "o", s = 100)
plt.scatter(P1,P2, color = "g", marker = "x", s = 100)
plt.legend()
plt.show()


#e. Now use PCA to reduce the dimension of the dataset to 1 dimension.
pca = PCA(n_components=1)
pca.fit(X)
Xpca = pca.transform(X)#onedim
print("original shape:   ", X.shape)
print("transformed shape:", Xpca.shape)

Xnew = pca.inverse_transform(Xpca)
plt.scatter(X[:, 0], X[:, 1], alpha=0.2)
plt.scatter(Xnew[:, 0], Xnew[:, 1], alpha=0.8)
plt.axis('equal');
plt.legend()
plt.show()
