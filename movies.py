import random

how_many_views = 0
movie_and_series_title_list = []
movie_title_list = []
series_title_list = []

class movies:
    movie_and_series_title_list = []
    movie_title_list = []

    def __init__(self, movie_title, year_of_publishment: int, kind_of_movie, how_many_views = 0):
        self.movie_title = movie_title
        self.year_of_publishment = year_of_publishment
        assert year_of_publishment >= 1888, 'First movie had been recorded on 14 October 1888'
        self.kind_of_movie = kind_of_movie
        self.how_many_views = how_many_views
        assert how_many_views >= 0
        # hmmm.. czy tak jest ok czy tylko self w ()?
        movies.movie_and_series_title_list.append(self.movie_title, self.series_title)
        movies.movie_title_list.append(self.movie_title)

class TV_series(movies):
    # czy super() tez to przenosi?
    series_title_list = []
    def __init__(self, series_title, season_number: int,episode_number: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.series_title = series_title
        self.season_number = season_number
        assert season_number >= 0
        self.episode_number = episode_number
        assert episode_number >= 0
        # i tu tez?
        TV_series.series_title_list.append(self.series_title)


    def play(self):
        if self.movie_title:
            how_many_views = how_many_views + 1
            return self.how_many_views
    
    def episode_count(self):
        if self.series_title:
            return f'{self.series_title} + str(S) + {self.season_number} + str(E) + {self.episode_number}'
    
    def movie_name(self):
        if self.movie_title:
            return f'str(") + {self.movie_title} + str(() + {self.year_of_publishment} + str()) + str(")'

    def lis_of_all(self):
        for i in movies and TV_series:
            movie_and_series_title_list.append(self.movie_title, self.series_title)
            return movie_and_series_title_list

    def get_series(self):
        for i in movie_and_series_title_list:
            if i is self.series_title:
                series_title_list.append()
                return series_title_list

    def get_movies(self):
        for i in movie_and_series_title_list:
            if i is self.movie_title:
                movie_title_list.append()
                return movie_title_list

    def search(self):
        for i in movie_and_series_title_list:
            a = input(self.movie_title, self.series_title)
            if a is movie_and_series_title_list:
                return a
    
    # tego nie było jako polecenie, ale cotam. hmmm.. czy tak mozna w return?
    def __repr__(self):
        return f"movies('{self.movie_title}', '{self.kind_of_movie}', '{self.year_of_publishment}', '{self.how_many_views},)", f"Tv_series('{self.series_title}', '{self.season_number}', '{self.episode_number}','{self.year_of_publishment}', '{self.how_many_views})"

    # czy da sie to polaczyc z episode_count?
    def generate_views(self):
        play_by_chance = random.choice(movie_and_series_title_list)
        if play_by_chance:
            self.how_many_views += 1
            for movie in random.choice(range(1,101)):
                return play_by_chance
    
    def repeat_10(generate_views):
        repeat = generate_views * 10
        return repeat

    def top_titles():
        for i in how_many_views:
            return