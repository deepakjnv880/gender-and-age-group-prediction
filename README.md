# Gender-and-Age-group-prediction
Gender and Age group prediction of human face and also analysis of chained model(chaining age group with gender) using Deep learning.

# Model Results -

![Result 1](/results/r2.png)

![Result 2](/results/r4.png)

![Result 3](/results/r3.png)

# Model Accuracy -
==========================<br/>
Gender prediction : 84.33515429496765 %<br/>
Age prediction : 50.65835118293762 %<br/>
Age prediction(Exact 1-off) : 81.70478170478171 %<br/>
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
Then some preprocessing(basically face alignment) has been done on all data from dataset.<br/>
Dataset contain five fold in it. From which first four fold used for training purpose and from last fifth fold 40% dataset used validation and 60% dataset used for testing.</br>
Model is trained on Google colab with GPU.<br/>


======================================================<br/>
Dimension of training dataset =>  (10988, 227, 227, 3)<br/>
Dimension of validation dataset =>  (1098, 227, 227, 3)<br/>
Dimension of testing dataset =>  (1647, 227, 227, 3)<br/>
======================================================<br/>

# Model architecture -
It is cnn based.
