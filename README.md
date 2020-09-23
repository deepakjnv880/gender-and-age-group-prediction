# Gender-and-Age-group-prediction
Gender and Age group prediction of human face and also analysis of chained model(chaining age group with gender) using Deep learning.


# Model Accuracy -
==========================<br/>
Gender prediction : 81 %<br/>
Age prediction : 51 %<br/>
Age prediction(Exact 1-off) : 83 %<br/>
==========================<br/>

# Dateset used -
[Adience data set](https://www.kaggle.com/ttungl/adience-benchmark-gender-and-age-classification) is used.<br/>
Then some preprocessing(basically face alignment and croping) has been done on all data from dataset.<br/>
Dataset contain five fold in it. From which first four fold used for training purpose and from last fifth fold 50% dataset used validation and 50% dataset used for testing.</br>
Model is trained on Google colab with GPU. Weights corresponding to best validation accuracy has been taken.<br/>


======================================================<br/>
Dimension of training dataset =>  (12969, 227, 227, 3)<br/>
Dimension of validation dataset =>  (1651, 227, 227, 3)<br/>
Dimension of testing dataset =>  (1651, 227, 227, 3)<br/>
======================================================<br/>

# Model architecture -
It is cnn based having four conv layer and two fully connected layer. In last layer softmax is used as activation function and in other layer relu has been used. Last fully connected layer have 2 or 8 neurons. Droupout of 60% has also been used to avoid overrfitting.

# Model Results -


![Result 1](/results/r7.png)

![Result 2](/results/r6.png)

![Result 3](/results/r5.png)

![Result 4](/results/r1.png)

![Result 5](/results/r4.png)

![Result 6](/results/r3.png)


# Chained Model Accuracy -
==========================<br/>
FOR MALE:<br/>
TEST ACCURACY :  42 %<br/>
TEST ACCURACY(Exact 1-off) :  80 %<br/>
==========================<br/>
FOR FEMALE:<br/>
TEST ACCURACY :  38 %<br/>
TEST ACCURACY(Exact 1-off) :  77 %<br/>
==========================<br/>
FOR CHILD:<br/>
TEST ACCURACY :  98 %<br/>
TEST ACCURACY(Exact 1-off) :  98 %<br/>
==========================<br/>

# Conclusion -
After chaining age prediction over gender, one can see male age prediction is better than female age accuracy. Author of one research paper was also stating the same that women are more good in hiding age :).<br/>
Also dataset age group level does not contain all age like age group 20-25. One can also estimate actual age value by taking weighted sum of mean of age range and its probability.
