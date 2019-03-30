# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 17:46:41 2019

@author: Bharath
"""
import webbrowser


class Movie():
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        """
        Inputs:
            movie_title : Title of the movie as a string input
            movie_storyline : The main storyline of the movie to be displayed
                              type - string input
            poster_image : link to display image of the movie
            trailer_youtube : url link of the youtube trailer
        Operation/Output:
            Constructor function to create an instance of the class Movie
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """
        Inputs:
            None
        Operation/Output:
            Launches the webbrowser to show the youtube trailer of the movie
        """
        webbrowser.open(self.trailer_youtube_url)
