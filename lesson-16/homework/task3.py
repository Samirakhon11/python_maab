import pandas as pd

df_iris = pd.read_json('iris.json')
numerical_columns = df_iris.select_dtypes(include = 'number') 

mean = numerical_columns.mean()
median = numerical_columns.median()
st_deviation = numerical_columns.std()

print("MEAN:\n", round(mean, 2))
print("MEDIAN:\n", round(median, 2))
print("STANDART DEVIATION:\n", round(st_deviation, 2))  

df_titanic = pd.read_excel('titanic.xlsx')

min_age = df_titanic['Age'].min()
max_age = df_titanic['Age'].max()
sum_of_ages = df_titanic['Age'].sum()

print("Minimum age is ", min_age)
print("Maximum age is ", max_age)
print("Sum of all ages is ", sum_of_ages) 
print('* ' * 50) 

df_movie = pd.read_csv('movie.csv')
dir_likes = df_movie['director_facebook_likes'].max()
dir_name = df_movie[df_movie['director_facebook_likes'] == dir_likes]['director_name'] 
print("Director with the highest likes on Facebook is ", dir_name)   

sorted_movies = df_movie.sort_values(by = 'duration', ascending = False) 
sorted_movies = sorted_movies[:5]

directors = sorted_movies['director_name'] 

for row, index in sorted_movies.iterrows(): 
    print(f"Director name: {index['director_name']}, Duration: {index['duration']} minutes") 