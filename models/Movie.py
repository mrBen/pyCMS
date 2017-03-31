class Movie:

    filename = 'films/{title} ({year})'

    def __init__(self, title, year):
        self.title = title
        self.year = year

    @property
    def path(self):
        return self.filename.format_map(self.__dict__)
