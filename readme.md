# Predicting the survival of Titanic passengers

## Objective
This project uses machine learning models to predict the survival of Titanic passengers and explores the factors that influenced the passengers' survival in an catastrophic event. I also created a webapp and hosted on Heroku for users to predict survival rate based on the information of passengers.


## Findings
- Female passengers had significantly higher chances of survival than male passengers, and married female passengers had higher survival rate than those who were not married. 
- Young passengers who were less than 12 years old had the highest chance of survival.
- Passengers who embarked from Cherbourg had the highest rate of survival while passengers who embarked from Southampton had the lowest rate of survival.
- First class passengers had higher survival rate than second and third class passengers.
- Passengers who were traveling alone had lower chances of survival.

## Methodology
### Features engineering
The original dataset has following features for each passenger:
- survival status
- passenger class
- name
- sex
- age
- number of siblings/spouses aboard
- number of parents/children aboard
- ticket number
- fare
- cabin
- port of embarkation
- lifeboat number
- body identification number
- home/destination  

Lifeboat number is removed from dataset as most of the passengers who didn't survive didn't have a lifeboat number, so it's not meaningful in predicting survival. Body identification number is also removed since it only the Titanic victims had it. Home/destination and cabin are removed due to a large amount of missing values. From passengers' names, *titles* are extracted and then name column is dropped afterwards. Age is binned into 6 *age groups*. *Family size* is generated from adding up number of siblings/spouses/parents/children. The fare column represents the sum of fares for passengers traveling together, who had the same ticket numbers. From these two columns, *group size* and *individual fare* are generated as new features.  


### Models
- Logistic Regression
- KNN
- Random Forest
- XGBoost
- SVM


### Technologies/Python Packages used 
- pandas
- numpy
- sklearn
- seaborn
- matplotlib
- re
- imlearn
- pickle
- yellowbrick
- html/css
- Flask
- PostgreSQL


## Deliverables
- Jupyter notebook for EDA and feature engineering
- Jupyter notebook for models
- Pickle File for data used in modeling
- Folder for web app (hosted on Heroku: https://titanic-survival-predictor1128.herokuapp.com/)
- Presentation deck
- Video for web app demo used in presentation