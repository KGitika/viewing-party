# ------------- WAVE 1 --------------------

# something just for testing
def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None
    new_movie = {}
    new_movie["title"] = title
    new_movie["genre"] = genre
    new_movie["rating"] = rating
    return new_movie

def add_to_watched(user_data, movie):
    # add move to user data
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    watched_movie = user_data["watched"] # [{}, {}]
    watchlist = user_data["watchlist"] # [{}, {}]
    for movie in watchlist:
        if movie["title"] == title:
            watched_movie.append(movie)
            watchlist.remove(movie)
    return user_data



'''
- take two parameters: `user_data`, `title`
  - the value of `user_data` will be a dictionary with a `"watchlist"` and a `"watched"`
    - This represents that the user has a watchlist and a list of watched movies
  - the value of `title` will be a string
    - This represents the title of the movie the user has watched
- If the title is in a movie in the user's watchlist:
  - remove that movie from the watchlist
  - add that movie to watched
  - return the `user_data`
- If the title is not a movie in the user's watchlist:
  - return the `user_data`
'''

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    watched_movies = user_data["watched"]
    length_of_wathced = len(watched_movies)

    if length_of_wathced == 0:
        return 0.0
    
    total_rating = 0.0
    for movie in watched_movies:
        total_rating += movie["rating"]
    return total_rating/length_of_wathced

def get_most_watched_genre(user_data):
    watched_movies = user_data["watched"]

    if len(watched_movies) == 0:
        return None
    
    frequency_of_genre = {} # element as genre:occurence
    for movie in watched_movies:
        genre = movie["genre"]
        frequency_of_genre[genre] = frequency_of_genre.get(genre,0) + 1

    popular_genre = ""
    highest_frequency = 0
    for genre, frequency in frequency_of_genre.items():
        if frequency > highest_frequency:
            popular_genre = genre
            highest_frequency = frequency
    return popular_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

