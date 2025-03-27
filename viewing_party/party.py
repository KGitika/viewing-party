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
        genre_of_movie = movie["genre"]
        frequency_of_genre[genre_of_movie] = frequency_of_genre.get(genre_of_movie,0) + 1

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

def get_movies_watched_by_friends(user_data):  # return [M,M,M]
    movies_watched_by_friends = []
    for friend in user_data["friends"]:
        movies_watched_by_friends.extend(friend["watched"])
    return movies_watched_by_friends

def get_unique_watched(user_data):
    movies_watched_by_user = user_data["watched"] #[M,M,M]
    movies_watched_by_friends = get_movies_watched_by_friends(user_data)
    
    unique_watched = []
    for movie in movies_watched_by_user:
        if movie not in movies_watched_by_friends:
            unique_watched.append(movie)
    return unique_watched

    # movies_watched_by_user_as_set = set(movies_watched_by_user)
    # movies_watched_by_friends_as_set = set(movies_watched_by_friends)
    # return list(movies_watched_by_user_as_set.difference(movies_watched_by_friends_as_set))

def get_friends_unique_watched(user_data):
    movies_watched_by_user = user_data["watched"]
    movies_watched_by_friends = get_movies_watched_by_friends(user_data)
    
    friends_unique_watched = []
    for movie in movies_watched_by_friends:
        if movie not in movies_watched_by_user and movie not in friends_unique_watched:
            friends_unique_watched.append(movie)
    return friends_unique_watched

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
 

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    '''
        This function gets a movie recommendation based on a user's friend
        and most popular genre.
    '''
    friends_unique_watched = get_friends_unique_watched(user_data)
    if not friends_unique_watched:
        return []
    
    popular_genre = get_most_watched_genre(user_data)
    rec_movies_list = []
    
    for movie in friends_unique_watched:
        if movie["genre"] == popular_genre:
            rec_movies_list.append(movie)
    return rec_movies_list

def get_rec_from_favorites(user_data):
    friends_watched = get_movies_watched_by_friends(user_data)
    recommendations = []
    for favorite_movie in user_data["favorites"]:
        if favorite_movie not in friends_watched:
            recommendations.append(favorite_movie)
    return recommendations

