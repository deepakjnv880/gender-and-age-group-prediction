# gender-and-age-group-prediction
Gender and Age group prediction of human face and also analysis of chained model(chaining age group with gender).

# Results -

![Result 1](/results/r2.png)

![Result 2](/results/r4.png)

![Result 3](/results/r3.png)

# Model Accuracy -
==========================<br/>
Gender prediction : 81.566 %<br/>
Age prediction : 50.65835118293762 %<br/>
==========================<br/>

# Chained Model Accuracy -
==========================<br/>
FOR MALE:<br/>
TEST ACCURACY :  44.120100140571594%<br/>
TEST ACCURACY(Exact 1-off) :  84.07005838198499 %<br/>
==========================<br/>
FOR FEMALE:<br/>
TEST ACCURACY :  38.74514997005463%<br/>
TEST ACCURACY(Exact 1-off) :  77.36093143596378 %<br/>
==========================<br/>
FOR CHILD:<br/>
TEST ACCURACY :  100.0%<br/>
TEST ACCURACY(Exact 1-off) :  100.0 %<br/>
==========================<br/>

# Dateset used :
[Adience data set](https://www.kaggle.com/ttungl/adience-benchmark-gender-and-age-classification)<br/>
There were 5 fold last one is used for testing purpose.<br/>
From all other fold 90% is used for training and 10% is used for validating.<br/>
