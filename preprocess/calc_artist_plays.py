#coding=utf-8

import os
import csv


artist_dictionary = {}
#def writeArtistPlays():


def calcArtistPlays():
    if os.path.exists('../data/artist') and os.path.exists('../data/song'):
        artistFileList = os.listdir('../data/artist')
        for artistFile in artistFileList:
            f = open('../data/artist/'+artistFile)
            rows = csv.reader(f)
            rows.next()
            print rows
