# Predicting-term-deposit-subscriptions
This project is about predicting whether a client will subscribe to a term deposit or not.This will predict which clients will likely
subscribe the term deposit before agents make phone calls.It will also help the banks to decide how many clients needs to be
contacted in order to meet their business target,based on which banks can plan the scope,budget and resources of marketing campaign accordingly
The dataset used in this project is obtained from kaggle.
Here is the link to the dataset: https://www.kaggle.com/janiobachmann/bank-marketing-dataset

The features used in the data are as follows:
#### bank client data:
- age (numeric)
- job : type of job (categorical: 'admin.','blue-collar','entrepreneur','housemaid','management','retired','self-employed','services','student','technician','unemployed','unknown')
- marital : marital status (categorical: 'divorced','married','single','unknown'; note: 'divorced' means divorced or widowed)
- education (categorical: 'basic.4y','basic.6y','basic.9y','high.school','illiterate','professional.course','university.degree','unknown')
- default: has credit in default? (categorical: 'no','yes','unknown')
- housing: has housing loan? (categorical: 'no','yes','unknown')
- loan: has personal loan? (categorical: 'no','yes','unknown')
#### related with the last contact of the current campaign:
- contact: contact communication type (categorical: 'cellular','telephone')
- month: last contact month of year (categorical: 'jan', 'feb', 'mar', ..., 'nov', 'dec')
- day_of_week: last contact day of the week (categorical: 'mon','tue','wed','thu','fri')
- duration: last contact duration, in seconds (numeric). Important note: this attribute highly affects the output target (e.g., if duration=0 then y='no').
#### other attributes:
- campaign: number of contacts performed during this campaign and for this client (numeric, includes last contact)
- pdays: number of days that passed by after the client was last contacted from a previous campaign (numeric; 999 means client was not previously contacted)
- previous: number of contacts performed before this campaign and for this client (numeric)
- poutcome: outcome of the previous marketing campaign (categorical: 'failure','nonexistent','success')
Output variable (desired target):
- has the client subscribed a term deposit? (binary: 'yes','no')

## Exploratory data analysis

Exploring categorical features
 
![eda1](https://user-images.githubusercontent.com/62187533/121782182-f38c8300-cbc5-11eb-9769-f5bb8ce31d2c.png)

From the above plots we can conclude that:
- In the dataset most of the clients have management as their job type.
- Clients who are married have more number of records in the given dataset.
- Most of the clients have secondary education.
- Default does not seems to be an important feature so it can be dropped.

## Exploring numerical features

![eda3](https://user-images.githubusercontent.com/62187533/121784957-9ea43900-cbd4-11eb-9932-cff16a596897.png)


From the above plots we can conclude that:
- Features like age and day are distributed normally.
- Features like balance,duration,campaign,pdays and previous are highly skewed towards left and seems to have some outliers.


## Finding Outliers in numerical features
![eda4](https://user-images.githubusercontent.com/62187533/121785115-7ff27200-cbd5-11eb-9aab-d8ff74e5ab8c.png)

It can be seen that age,balance,duration,pdays,previous have some outliers.

![eda5](https://user-images.githubusercontent.com/62187533/121785137-aca68980-cbd5-11eb-950f-82d4a2b61ee8.png)

It can be seen that no feature is heavily correlated with any other feature.

## Performance by different models:

## Random forest classifier

Random forest classifier gives 0.85 accuracy score and 0.85 precision score
Confusion matrix:

![eda7](https://user-images.githubusercontent.com/62187533/121785293-a238bf80-cbd6-11eb-97df-893a75d83f88.png)

## SVM's

SVM classifier gives 0.72 accuracy score and 0.74 precision score.

Confusion matrix:

![eda8](https://user-images.githubusercontent.com/62187533/121785307-b2e93580-cbd6-11eb-94ec-9f0bdf8127b4.png)

## XGBoost classifier

XGBoost classifier gives 0.85 accuracy score and 0.85 precision score

Confusion matrix:

![eda6](https://user-images.githubusercontent.com/62187533/121785301-a9f86400-cbd6-11eb-891b-1a9f6b7b0e8b.png)


The model was deployed on heroku.
Here is the heroku link to the project: https://predicttermdeposits.herokuapp.com





