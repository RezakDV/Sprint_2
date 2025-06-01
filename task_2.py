# Создание супер класса Movies
class Movies:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

# Создание подкласса Comedy с переопределением метода add_movie
class Comedy(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        return f"Комедии: '{self.movies}'"

# Создание подкласса Drama с переопределением метода add_movie
class Drama(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        return f"Драмы: '{self.movies}'"
    
# Вызов методов add_movie для объекта Сomedy()
comedy = Comedy()
print(comedy.add_movie('Большой куш'))

# Вызов методов add_movie для объекта Drama()
drama = Drama()
print(drama.add_movie('Оружейный барон'))