# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None
    new_movie = {}
    new_movie["title"] = title
    new_movie["genre"] = genre
    new_movie["rating"] = rating
    return new_movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    watched_movie = user_data["watched"] # [{}, {}]
    watchlist = user_data["watchlist"] 
    for movie in watchlist:
        if movie["title"] == title:
            watched_movie.append(movie)
            watchlist.remove(movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    watched_movies = user_data["watched"]
    total_rating = 0.0
    for movie in watched_movies:
        total_rating += movie["rating"]
    try:
        return total_rating/len(watched_movies)
    except ZeroDivisionError:
        return total_rating

def get_most_watched_genre(user_data):
    watched_movies = user_data["watched"]
    
    frequency_of_genre = {} # element as genre:occurence
    for movie in watched_movies:
        genre_of_movie = movie["genre"]
        frequency_of_genre[genre_of_movie] = frequency_of_genre.get(genre_of_movie,0) + 1

    popular_genre = None
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
def get_available_recs(user_data):
    friends_unique_watched = get_friends_unique_watched(user_data)
    user_subscriptions = user_data["subscriptions"]
    recommended_movies = []
    for movie in friends_unique_watched:
        if movie["host"] in user_subscriptions:
            recommended_movies.append(movie)
    return recommended_movies

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

