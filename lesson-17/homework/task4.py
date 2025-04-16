import pandas as pd

df_titanic = pd.read_excel('titanic.xlsx')

survived_passengers = df_titanic[df_titanic['Survived'] == 1] 

age_mean = round(survived_passengers['Age'].mean(), 2)
survived_passengers['Age'] = survived_passengers['Age'].fillna(age_mean) 

survived_passengers['Fare_by_age'] = survived_passengers['Fare'] / survived_passengers['Age']
print(survived_passengers) 