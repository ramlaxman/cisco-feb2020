#!/usr/bin/env python3

# dict of dicts

movies = {'Spotlight': {'length': 129, 'director': 'Tom McCarthy'},
          'The Big Short': {'length': 130, 'director': 'Adam McKay'},
          'The Martian': {'length': 141, 'director': 'Ridley Scott'}
          }

look_for = input("Enter movie title: ")

for one_movie in movies:
    if one_movie['name'] == look_for:
        print(
            f"Found {look_for}, {one_movie['length']} min, dir {one_movie['director']}")
        break
else:  # no break encountered in the for loop
    print(f"Sorry, didn't find {look_for}")
