# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 17:57:20 2019

@author: Bharath
"""
# Import Media file to access the Class Movie
import media
import fresh_tomatoes

"""
Creating instance of class Movie with movie_title as Toy story &
its storyline, poster image & a link to its trailer
"""
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # noqa
                        "https://youtu.be/rNk1Wi8SvNc")

"""
Creating instance of class Movie with movie_title as Inside Out &
its storyline, poster image & a link to its trailer
"""
Inside_Out = media.Movie("Inside Out",
                         "A story of a girl and her personified emoitions",
                         "https://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_%282015_film%29_poster.jpg",  # noqa
                         "https://youtu.be/seMwpP0yeu4")


"""
Creating instance of class Movie with movie_title as Lors of the Rings &
its storyline, poster image & a link to its trailer
"""
The_Lord_Of_the_Rings = media.Movie("The Lord of the Rings - Fellowship",
                                    "Frodo, aided by his fellowship, \
                                     begins his journey to destroy the \
                                     evil ring of the Dark Lord Sauron",
                                    "https://upload.wikimedia.org/wikipedia/en/9/9d/The_Lord_of_the_Rings_The_Fellowship_of_the_Ring_%282001%29_theatrical_poster.jpg",  # noqa
                                    "https://youtu.be/V75dMMIW2B4")


"""
Creating instance of class Movie with movie_title as Home Alone &
its storyline, poster image & a link to its trailer
"""
Home_Alone = media.Movie("Home Alone: A family comedy without the family",
                         "After being left behind at home accidentally, \
                         a young boy has to defend his home from burglarls",
                         "https://upload.wikimedia.org/wikipedia/en/7/76/Home_alone_poster.jpg",  # noqa
                         "https://youtu.be/dzdpqRGA1qc")

"""
Creating instance of class Movie with movie_title as The Lion King &
its storyline, poster image & a link to its trailer
"""
The_Lion_King = media.Movie("The Lion King",
                            "A lion cub in exile learns about his true past\
                            & comes back to avenge his father",
                            "https://upload.wikimedia.org/wikipedia/en/3/3d/The_Lion_King_poster.jpg",  # noqa
                            "https://youtu.be/4sj1MT05lAA?t=7")

movies = [toy_story, Inside_Out, The_Lord_Of_the_Rings,
          Home_Alone, The_Lion_King]
fresh_tomatoes.open_movies_page(movies)
