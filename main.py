#encoding=utf8 
import sys
reload(sys) 
sys.setdefaultencoding('utf8')

from flask import Flask, jsonify, request
import csv

all_movies = []

with open("all_movies.csv") as f:
     reader = csv.reader(f)
     data = list(reader)
     all_movies = data[1:]

liked_movies = []
disliked = []
not_watched = []

App = Flask(__name__)

@App.route("/get-movie")

def get_movie():
     return jsonify({
         "data": all_movies[0],
         "status": "success"
     })

@App.route("/liked_movie", methods = ["POST"])

def liked_movies():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    liked_movies.append(movie)
    return jsonify({
        "status": "success"
    })

@App.route("/disliked_movie", methods = ["POST"])

def disliked_movie():
     movie = all_movies[0]
     all_movies = all_movies[1:]
     disliked.append(movie)
     return jsonify({
         "status": "success"
     }),202

@App.route("/watched_movie", methods = ["POST"])

def watched_movie():
     movie = all_movies[0]
     all_movies = all_movies[1:]
     not_watched.append(movie)
     return jsonify({
         "status": "success"
     }),201

if __name__ == "__main__":
     App.run()