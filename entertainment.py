import fresh_tomatoes
import movie

# Here, we import the two other .py files/modules: movie and fresh_tomatoes. Movie is where we have created the appropriate classes.
# We can create a new instance of a class by defining a variable as movie.Movie. Movie with the upper-case is the class, and movie with
# the lower case is the module we are importing from. That's the movie.py file. We are giving each movie the necessary attributes as
# defined in our movie file (title, storyline, image URL, youtube URL, release date). At the end, we are using the fresh_tomatoes module,
# which has a function entitled open_movies_page that takes the argument (movies). Movies, being our list of movies.

lionheart = movie.Movie("Lionheart",
                        "A Jean-Claude Van Damme film about never giving up, and fighting for what is right.",
                        "https://upload.wikimedia.org/wikipedia/en/7/72/Lion-Heart-Poster.jpg",
                        "https://www.youtube.com/watch?v=QKqjwvWNnzg",
                        "1990")

uni_sol = movie.Movie("Universal Soldier",
                      "JCVD and Dolph Lundgren fight it out as robots!",
                      "https://upload.wikimedia.org/wikipedia/en/9/93/Universal_soldier_ver1.jpg",
                      "https://www.youtube.com/watch?v=5Y7BWfIEfuo",
                      "1992")

cyborg = movie.Movie("Cyborg",
                     "A post apocolyptic wasteland. Our only hope? Jean-Claude Van Damme.",
                     "https://upload.wikimedia.org/wikipedia/en/e/e4/Cyborgposter.jpg",
                     "https://www.youtube.com/watch?v=NsyjFihG5k8",
                     "1989")

double_team = movie.Movie("Double Team",
                          "Jean-Claude Van Damme and Dennis Rodman. What could go possibly go wrong?",
                          "https://upload.wikimedia.org/wikipedia/en/d/d6/Double_team_ver1.jpg",
                          "https://www.youtube.com/watch?v=36gSLmCHpUQ",
                          "1997")

death_warrant = movie.Movie("Death Warrant",
                            "Van Damme in prison? Don't mess with him!",
                            "https://upload.wikimedia.org/wikipedia/en/1/12/Death_warrant_poster.jpg",
                            "https://www.youtube.com/watch?v=Xngl0GyJubY",
                            "1990")

knock_off = movie.Movie("Knock Off",
                        "Van Damme and Rob Schneider. This movie is not a knock off, but it's about fake foregin goods.",
                        "https://upload.wikimedia.org/wikipedia/en/1/14/Knockoffposter.jpg",
                        "https://www.youtube.com/watch?v=La6MF5EtuNc",
                        "1998")

movies = [lionheart, uni_sol, cyborg, double_team, death_warrant, knock_off]
fresh_tomatoes.open_movies_page(movies)
