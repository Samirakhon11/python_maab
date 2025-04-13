import pandas as pd

df = pd.read_json("iris.json")
print("Original column names:", df.columns.tolist())

df.columns = df.columns.str.lower()

df.rename(columns={
    'sepallength': 'sepal_length',
    'sepalwidth': 'sepal_width'
}, inplace=True)

df_selected = df[["sepal_length", "sepal_width"]]

print("\nSelected columns:")
print(df_selected) 
print('* ' * 30)

df_titanic = pd.read_excel('titanic.xlsx') 
print(df_titanic[df_titanic['Age'] > 30]) 
print('* ' * 30)

print(df_titanic['Sex'].value_counts()) 
print('* ' * 30)

df_movie = pd.read_csv('movie.csv')
filtered = df_movie[df_movie['duration'] > 120] 
sorted_movie = filtered.sort_values(by = 'director_facebook_likes', ascending = False)
print(sorted_movie)  