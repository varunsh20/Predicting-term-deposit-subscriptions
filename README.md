# Predicting-term-deposit-subscriptions
This project is about predicting whether a client will subscribe to a term deposit or not.
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













