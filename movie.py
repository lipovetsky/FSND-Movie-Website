import webbrowser

# This creates a class called Movie. It is the main class
# where we store the information about each title. The __init__ function
# includes the movie title, storyline, poster image,
# youtube trailer, and movie release date. We use these in
# fresh_tomatoes to generate an HTML webpage with the info.
# The show_trailer function allows you to directly open
# the web browser and navigate to the youtube page
# for the specific movie trailer.


class Movie():
    "This class is amazing. It lets us get all the information for our movie."
    MOVIE_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, movie_poster,
                 movie_trailer, release_date):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster
        self.youtube_trailer_url = movie_trailer
        self.release_date = release_date

    def show_trailer(self):
        webbrowser.open(self.youtube_trailer_url)
