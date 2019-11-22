

1.	What is unsupervised learning? How supervised algorithms are different from unsupervised ones?  
Unsupervised machine learning algorithms can be used to discover the underlying structure and patterns of the data. It is classified into two categories of algorithms: clustering and association. In Supervised learning, you can approximate the mapping function so that you can predict the output data and variables from the input data. While in unsupervised learning, we can not apply it directly to a regression or classification problem since the output is unknown. 

2.	What is Principle Component Analysis (PCA)?  
Principal component analysis (PCA) is a statistical procedure that transform a set of correlated variables into a (smaller) number of uncorrelated variables called principal components. 

Q3 F. What are your conclusions about PCA in terms of dimensionality reduction and principle components?  
After the dimension reduction, we only have the component of the data with the highest variance. We project each data on to the principal component and we discard the information along the shorter direction. 


Auto Encoder:
1.	What is an AutoEncoder?
 An AutoEncoder is a type of artificial neural network used to learn efficient data coding in an unsupervised manner. They work by forcing a compressed knowledge representation of the original input and then reconstructing the output from this representation. The AutoEncoder is composed of encoder and decoder. 
 
2. What are the similarities and differences of PCA and AutoEncoder? 
PCA is restricted to a linear map and linear transformation, while auto encoders can have nonlinear encoder/decoders and auto encoder is more flexible. In PCA, the axes and components are orthogonal and ordered as to the variance of data, but Autoencoders do not have this feature. 

3.	What is data compression?  Why do we need to compress data? 
Data compression is a process of modifying, encoding or converting the bits and result in the reduction in the bits needed to represent data. We need to compress data because compressing data can save storage capacity, speed up file, decrease the cost of storage. 

4.	 How do AutoEncoders form a compression of the data as compared to PCA?  
In autoencoders, it attempts to compress the information of variables into reduced dimensional space and then recreate the input data set. In the “bottleneck” layer, a hidden layer, the information gets compressed. While in PCA, we have dimension reduction by projecting the data onto a lower dimensional space while preserving as much information as possible. 

5. What are Variational AutoEncoders (VAE)? What cost function is used in VAE? What information theoretic quantity is the cost function?  
VAE is a deep learning technique for learning latent representations. It is an autoencoder whose encodings distribution is regularized during the training.  Therefore, its latent space has good properties to generate some new data. The cost function of decoder which generates data from the latent variable, the encoder and distribution function is used. 
