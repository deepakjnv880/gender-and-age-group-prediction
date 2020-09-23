# Gender-and-Age-group-prediction
Gender and Age group prediction of human face and also analysis of chained model(chaining age group with gender) using Deep learning.

# Model Results -


![Result 1](/results/r7.jpg)

![Result 2](/results/r6.jpg)

![Result 3](/results/r5.jpg)

![Result 4](/results/r1.jpg)

![Result 5](/results/r2.jpg)

![Result 6](/results/r4.jpg)

![Result 7](/results/r3.jpg)

# Model Accuracy -
==========================<br/>
Gender prediction : 81 %<br/>
Age prediction : 51 %<br/>
Age prediction(Exact 1-off) : 83 %<br/>
==========================<br/>

# Chained Model Accuracy -
==========================<br/>
FOR MALE:<br/>
TEST ACCURACY :  44.120100140571594 %<br/>
TEST ACCURACY(Exact 1-off) :  84.07005838198499 %<br/>
==========================<br/>
FOR FEMALE:<br/>
TEST ACCURACY :  38.74514997005463 %<br/>
TEST ACCURACY(Exact 1-off) :  77.36093143596378 %<br/>
==========================<br/>
FOR CHILD:<br/>
TEST ACCURACY :  100.0 %<br/>
TEST ACCURACY(Exact 1-off) :  100.0 %<br/>
==========================<br/>

# Dateset used -
[Adience data set](https://www.kaggle.com/ttungl/adience-benchmark-gender-and-age-classification) is used.<br/>
Then some preprocessing(basically face alignment and croping) has been done on all data from dataset.<br/>
Dataset contain five fold in it. From which first four fold used for training purpose and from last fifth fold 50% dataset used validation and 50% dataset used for testing.</br>
Model is trained on Google colab with GPU.<br/>


======================================================<br/>
Dimension of training dataset =>  (12969, 227, 227, 3)<br/>
Dimension of validation dataset =>  (1651, 227, 227, 3)<br/>
Dimension of testing dataset =>  (1651, 227, 227, 3)<br/>
======================================================<br/>

# Model architecture -
It is cnn based.
