# FSND-Movie-Website

This is a Python project that generates an HTML webpage that serves
movie trailers! And not just any trailers: Jean-Claude Van Damme trailers!
You can edit the entertainment.py file to change the movies/trailers;
but then again, why would you want to?

## Install

In order to get the code running, you must be in the working directory
of the files in terminal while running the following command:

`$ python entertainment.py`

That is all there is to it. When the entertainment.py file is run,
it connects with the other two files, and generates an HTML page
with movie trailers (it looks great, too!)

## Editing the trailers

If you ever want to change the trailers, you can do so by
editing the entertainment.py file. You will see a list of movies
there, in this format:

```
lionheart = movie.Movie("Lionheart",
                        "A Jean-Claude Van Damme film about never giving up,"
                        " and fighting for what is right.",
                        "https://upload.wikimedia.org/wikipedia/en/7/72/Lion-Heart-Poster.jpg",
                        "https://www.youtube.com/watch?v=QKqjwvWNnzg",
                        "1990")
```

If you want to change the movie, change these attributes. As you can see,
it starts with the Title, then a description, then the movie poster image,
followed by the YouTube trailer link, and finally the Release Date.

## Concluding Words

This project was created as part of the Intro to Programming Nanodegree
for Udacity. It is a fantastic course. Build this yourself (along with
many other projects) by enrolling.
