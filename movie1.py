#!/usr/bin/env python3

# list of lists

movies = [['Spotlight', 129, 'Tom McCarthy'],
          ['The Big Short', 130, 'Adam McKay'],
          ['The Martian', 141, 'Ridley Scott']]

look_for = input("Enter movie title: ")

for one_movie in movies:
    if one_movie[0] == look_for:
        print(f"Found {look_for}, {one_movie[1]} min, dir {one_movie[2]}")
        break
else:  # no break encountered in the for loop
    print(f"Sorry, didn't find {look_for}")
