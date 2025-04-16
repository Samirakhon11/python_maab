import pandas as pd

df_titanic = pd.read_excel('titanic.xlsx')
group = df_titanic.groupby('Pclass') 

average_age = group['Age'].mean().reset_index(name = 'Average_age')
total_fare = group['Fare'].sum().reset_index(name = 'Total_fare') 

result_df = pd.merge(average_age, total_fare, on = 'Pclass') 
result_df['Passenger_count'] = group.size().values

class1 = group['Pclass'].value_counts() 

print("Average age is: ", average_age) 
print("Total fare is: ", total_fare)
print(result_df) 
print('* ' *50) 


df_movie = pd.read_csv('movie.csv')
grouped = df_movie.groupby(['color', 'director_name']).agg(num_of_critics = ('num_critic_for_reviews', 'sum'), time = ('duration', 'mean')).reset_index() 

print(grouped) 