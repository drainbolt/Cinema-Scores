#!/usr/bin/env python3
import imdb
import firebase_admin
import google
from firebase_admin import credentials, firestore

#cast, genre, composers, runtime, directors, writers, composers, cineomotaghers
def upload(data, moviesDB):
    db = firestore.client()

    for i in data:
        movie = moviesDB.search_movie(i)
        ID = movie[0].getID()
        m = moviesDB.get_movie(ID)

        '''
        https://firebase.google.com/docs/firestore/query-data/queries


        movie_dict = {
            u'title': m['title'],
            u'cast': m['cast'],
            u'genre': m['genre'],
            u'producers': m['producers'],
            u'runtime': m['runtime'],
            u'directors': m['directors'],
            u'writers': m['writers'],
            u'cinematographers': m['cinematographers'],
            u'rating': m['rating']
        }
        movies_ref = db.collection(u'movies')
        movies_ref.document(m['title']).set(movie_dict)
        '''
        if 'cast' in m.keys():
            for p in m['cast']:
                if 'name' in p.keys():
                    person = p['name']
                else:
                    continue
                actor = {
                    u'movies': [m['title'], m['rating']]
                }
                act_ref = db.collection(u'actors').document(person)

                try:
                    act = act_ref.get()
                    
                    act_ref.update({u'movies': firestore.ArrayUnion([m['title'], m['rating']])})
                except google.cloud.exceptions.NotFound:
                    
                    act_ref.set(actor)

        if 'directors' in m.keys():
            for p in m['directors']:
                if 'name' in p.keys():
                    person = p['name']
                else:
                    continue
                director = {
                    u'movies': [m['title'], m['rating']]
                }
            
            #insert into database
                dir_ref = db.collection(u'directors').document(person)

                try:
                    direct = dir_ref.get()
                    
                    dir_ref.update({u'movies': firestore.ArrayUnion([m['title'], m['rating']])})
                except google.cloud.exceptions.NotFound:
                    
                    dir_ref.set(actor)

        if 'producers' in m.keys():
            for p in m['producers']:
                if 'name' in p.keys():
                    person = p['name']
                else:
                    continue
                producers = {
                    u'movies': [m['title'], m['rating']]
                }
            
                #insert into database
                prod_ref = db.collection(u'producers').document(person)
                try:
                    prod = prod_ref.get()
                    
                    prod_ref.update({u'movies': firestore.ArrayUnion([m['title'], m['rating']])})
                except google.cloud.exceptions.NotFound:
                    prod_ref.set(actor)

        if 'writers' in m.keys():
            for p in m['writers']:

                if 'name' in p.keys():
                    person = p['name']
                else:
                    continue

                writers = {
                    u'movies': [m['title'], m['rating']]
                }

                writ_ref = db.collection(u'writers').document(person)

                try:
                    writer = writ_ref.get()
                    
                    writ_ref.update({u'movies': firestore.ArrayUnion([m['title'], m['rating']])})
                except google.cloud.exceptions.NotFound:
                    
                    writ_ref.set(actor)
        

        #insert into database
        if 'cinematographers' in m.keys():
            for p in m['cinematographers']:  
                if 'name' in p.keys():
                    person = p['name']
                else:
                    continue
                cinematographers = {
                    u'movies': [m['title'], m['rating']]
                }
            
            #insert into database
                cin_ref = db.collection(u'cinematographers').document(person)

                try:
                    cinema = cin_ref.get()
                    
                    cin_ref.update({u'movies': firestore.ArrayUnion([m['title'], m['rating']])})
                except google.cloud.exceptions.NotFound:
                    
                    cin_ref.set(cinematographers)
            

        for p in m['genre']:

            person = p
            genre = {
                u'movies': [m['title'], m['rating']]
            }
        
        #insert into database
            gen_ref = db.collection(u'genres').document(person)

            try:
                genre = gen_ref.get()
                gen_ref.update({u'movies': firestore.ArrayUnion([m['title'], m['rating']])})
            except google.cloud.exceptions.NotFound:
                gen_ref.set(genre)

def main():
    cred = credentials.Certificate('C:/Users/dalan/cs425/CinemaScores/cinscdb_cert.json')
    firebase_admin.initialize_app(cred)

    db = firestore.client()

    moviesDB = imdb.IMDb()
    # print(dir(moviesDB))

    # get a movie
    top_movies = moviesDB.get_top250_movies()
    bottom_movies = moviesDB.get_bottom100_movies()
    top = []
    bottom = []

    for movie in top_movies:
        top.append(movie['title'])
    for movie in bottom_movies:
        bottom.append(movie['title'])

    upload(top, moviesDB)
    upload(bottom, moviesDB)

main()