# gender-and-age-group-prediction
Gender and Age group prediction of human face and also analysis of chained model(chaining age group with gender).

# Results on some photo -

![Result 1](/results/r2.png)

![Result 2](/results/r4.png)

![Result 3](/results/r3.png)

# Model Accuracy -
*********************
Gender prediction : 81.566 %
Age prediction : 50.65835118293762 %
Age prediction(Exact 1-off) : 81.70478170478171 %
*********************

# Chained Model Accuracy -
*********************
FOR MALE:
TEST ACCURACY :  44.120100140571594
TEST ACCURACY(Exact 1-off) :  84.07005838198499 %
*********************
FOR FEMALE:
TEST ACCURACY :  38.74514997005463
TEST ACCURACY(Exact 1-off) :  77.36093143596378 %
*********************
FOR CHILD:
TEST ACCURACY :  100.0
TEST ACCURACY(Exact 1-off) :  100.0 %
*********************

# Dateset used for training/testing/validating :
[Adience data set](https://www.kaggle.com/ttungl/adience-benchmark-gender-and-age-classification)
There were 5 fold last one is used for testing purpose.
From all other fold 90% is used for training and 10% is used for validating.
