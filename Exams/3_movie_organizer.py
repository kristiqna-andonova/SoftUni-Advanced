def movie_organizer(*args):
    movie_dict = {}
    for movie, genre in args:
        if genre not in movie_dict:
            movie_dict[genre] = []
        movie_dict[genre].append(movie)

    sorted_film_genres = sorted(movie_dict.items(), key=lambda x: (-len(x[1]), x[0]))

    result = ''
    for genre, movie_name in sorted_film_genres:
        sorted_movies = sorted(movie_name)
        result += f"{genre} - {len(sorted_movies)}\n"
        for name in sorted_movies:
            result += f"* {name}\n"
    return result.strip()