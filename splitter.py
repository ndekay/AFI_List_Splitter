#!/usr/bin/env python


"""Reads an input text file containing downloaded AFI Top 100 movie data and builds a CSV containing Rank and Title."""


import csv


__author__ = "Nickolaus Dekay"
__version__ = "1.0.1"
__email__ = "Nickolaus.Dekay@gmail.com"


def main():
    # define input/output locations
    dir = '.'
    f_input = csv.reader(open(dir + '\\top_100_list.txt'), delimiter=' ', quotechar='"')
    f_output = dir + '\\top_100_list.csv'

    # iterate through the movie list, discarding unneeded fields at the end and putting rank/title into a dictionary
    movie_list = {}
    for row in f_input:
        if row[-1].upper() == 'N/A':
            movie = row[1:-1]
            movie_list[int(row[0])] = ' '.join(movie)
        else:
            movie = row[1:-2]
            movie_list[int(row[0])] = ' '.join(movie)

    # write the data from the dictionary into a csv format, in order of rank
    with open(f_output, 'w') as f:
        f.write("RANK,FILM\n")
        for i in sorted(movie_list.keys()):
            f.write("{},\"{}\"\n".format(i, movie_list[i]))


if __name__ == "__main__":
    main()