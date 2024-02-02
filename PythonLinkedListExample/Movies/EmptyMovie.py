from Movie import Movie

class EmptyMovie(Movie):
    def __init__(self):
        super().__init__("", 0, None)
        pass

    def __str__(self):
        return "-|"

