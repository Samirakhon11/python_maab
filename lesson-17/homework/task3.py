import pandas as pd

df_titanic = pd.read_excel('titanic.xlsx')

def classify_age(age):
    if age < 18:
        return 'Child'
    else:
        return 'Adult'
    
df_titanic['Age_Category'] = df_titanic['Age'].apply(classify_age) 
print(df_titanic) 
print('* ' * 50, '\n')

df_employee = pd.read_csv('employee.csv') 

df_employee['Normalized_Salary'] = df_employee.groupby('DEPARTMENT')['BASE_SALARY'].transform(lambda x: (x - x.min()) / (x.max() - x.min())) 

print(df_employee) 
print('* ' * 50, '\n')

df_movie = pd.read_csv('movie.csv')

def classify_time(time):
    if time < 60:
        return 'Short'
    elif 60 < time < 120:
        return 'Medium'
    else:
        return 'Long'
    
df_movie['Duration_Classified'] = df_movie['duration'].apply(classify_time)

print(df_movie) 