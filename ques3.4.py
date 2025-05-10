friend1_movies = {"Inception", "Interstellar", "The Matrix"}
friend2_movies = {"The Matrix", "Titanic", "Avatar"}
all_movies = friend1_movies.union(friend2_movies)
print("All favorite movies:", all_movies)
common_movies = friend1_movies.intersection(friend2_movies)
print("Common favorite movies:", common_movies)
unique_movies = friend1_movies.difference(friend2_movies)
print("Movies only liked by Friend 1:", unique_movies)
