import requests

import requests
import random

API_KEY = "55439e28e501c0e1e7cfb94915c62d77"  
BASE_URL = "https://api.themoviedb.org/3"

def get_genre_id(genre_name):
    """Fetch genre ID from TMDB based on user input"""
    url = f"{BASE_URL}/genre/movie/list?api_key={API_KEY}&language=en-US"
    response = requests.get(url).json()
    
    for genre in response["genres"]:
        if genre["name"].lower() == genre_name.lower():
            return genre["id"]
    
    return None

def get_movies_by_genre(genre_id):
    """Fetch movies for a given genre ID"""
    url = f"{BASE_URL}/discover/movie?api_key={API_KEY}&with_genres={genre_id}&language=en-US"
    response = requests.get(url).json()
    
    return response.get("results", [])

def recommend_movie():
    """Ask user for a genre and recommend a random movie"""
    genre_name = input("Enter a movie genre: ").strip()
    genre_id = get_genre_id(genre_name)
    
    if not genre_id:
        print("Sorry, genre not found. Try again!")
        return
    
    movies = get_movies_by_genre(genre_id)
    
    if not movies:
        print("No movies found for this genre.")
        return
    
    movie = random.choice(movies)
    print("\n🎬 Movie Recommendation 🎬")
    print(f"Title: {movie['title']}")
    print(f"Overview: {movie['overview']}")
    print(f"Release Date: {movie['release_date']}")
    print(f"TMDB Rating: {movie['vote_average']}/10")

recommend_movie()
