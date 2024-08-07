## Problem description:
Employee Attrition is when an employee leaves the company through any method, including voluntary resignations, layoffs, failure to return from a leave of absence, or even illness or death. Every year a lot of companies hire a number of employees. The companies invest time and money in training those employees, not just this but there are training programs within the companies for their existing employees as well. The concept of these programs is to increase the effectiveness of their employees. If there is any model that can predict employee attrition it will be easy to analyze the attrition process and improving the performance of employees.

## DATA: 
"Employee analisis. Attrition report" from kaggle: https://www.kaggle.com/datasets/whenamancodes/hr-employee-attrition

## EDA:
The analysis of categorical feature correlation with the target variable 'attrition' reveals that features 'educationfield', 'environmentsatisfaction', 'worklifebalance', 'jobinvolvement', 'overtime', 'jobrole', 'businesstravel', and 'maritalstatus' have pronounced more effects on attrition then other.
The analysis of numerical feature correlation with the target variable 'attrition' reveals that features 'age', 'joblevel', 'monthlyincome', 'stockoptionlevel', 'totalworkingyears','yearsatcompany', 'yearsincurrentrole', 'yearswithcurrmanager'  have pronounced more effects on attrition then other. 
There are not any missing values in the dataset.

## MODELS: 
In this progect were trained and tuned four models: LogisticRegression, DecisionTreeClassifier, RandomForestClassifier and XGBoost. All models were validated. The quality metric was chousen roc_auc_score. LogisticRegression seemed the best.

## TRAIN SCRIPT: 
the final taining script is in train.py

## REPRODUCABILITY: 
it's possible to reproduce almost everything: dependencies from requirements.txt are for notebook, Pipfile and PIpfile.lock are for deploying the service. The only difficult part is reproducing XGBoost tuning. It was trained several times using the same blocks with different parameteres before plotting

## DEPLOYMENT: 
To reproduse the cloud deployment process:
1) copy all these files to a new folder
2) cd "your_folder with copyes"
3) docker build -t employee-attrition_serv .
4) docker run -it -p 9696:9696 employee-attrition_serv:latest #To run it locally
5) pipenv install awsebcli --dev
6) pipenv shell
7) eb init -p docker -r eu-west-1 attrition-serv
8) eb create attrition-serving-env

Here is assumed, that you already install docker, have account on AWS and correct "credentials" file on your computer.
