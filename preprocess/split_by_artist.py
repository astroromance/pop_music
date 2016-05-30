#coding=utf-8
import csv
import os
import shutil

artist_dictionary = {}

def writeByArtist(artist,data):
    fileName = artist + '.csv'
    os.chdir('../data/artist')
    if not artist_dictionary.has_key(artist):
        artist_dictionary[artist] = True
        f = open(fileName,'ab')
        write = csv.writer(f)
        write.writerow(['song_id','publish_time','song_init_plays','language','gender'])
        write.writerow(data)
        f.close()
    else:
        f = open(fileName,'ab')
        write = csv.writer(f)
        write.writerow(data)
        f.close()
    os.chdir('../../preprocess')


# song_id, artist_id,publish_time,song_init_plays,language,gender
def splitByArtist():
    if os.path.exists('../data/artist'):
        shutil.rmtree('../data/artist')
    os.mkdir('../data/artist')
    f = open('../data/mars_tianchi_songs.csv')
    rows = csv.reader(f)
    rows.next()
    for row in rows:
        #print row
        artist = row[1]
        del row[1]
        writeByArtist(artist,row)



