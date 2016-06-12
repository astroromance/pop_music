#coding=utf-8

import os
import csv
import shutil

artist_dictionary = {}
def writeArtistPlays(artist_id,Ds,cnt):
    fileName = artist_id + '.csv'
    if not artist_dictionary.has_key(artist_id):
        artist_dictionary[artist_id] = True
        f = open('../data/artist_plays/'+fileName,'ab')
        write = csv.writer(f)
        write.writerow(['Ds','cnt'])
        write.writerow([Ds,cnt])
        f.close()
    else:
        f = open('../data/artist_plays/'+fileName,'ab')
        write = csv.writer(f)
        write.writerow([Ds,cnt])
        f.close()

def calcArtistPlays():
    if os.path.exists('../data/artist_plays'):
        shutil.rmtree('../data/artist_plays')
    os.mkdir('../data/artist_plays')
    if os.path.exists('../data/artist') and os.path.exists('../data/song'):
        artistFileList = os.listdir('../data/artist')
        for artistFile in artistFileList:
            artist_id = artistFile[0:-4]
            date_dictionary = {}
            f1 = open('../data/artist/'+artistFile)
            rows1 = csv.reader(f1)
            rows1.next()
            for row1 in rows1:
                song_id = row1[0]
                if os.path.exists('../data/song/'+song_id+'.csv'):
                    f2 = open('../data/song/'+song_id+'.csv')
                    rows2 = csv.reader(f2)
                    rows2.next()
                    for row2 in rows2:
                        Ds = row2[3]
                        action_Type = row2[2]
                        if action_Type == '1':
                            if date_dictionary.has_key(Ds):
                                date_dictionary[Ds] = date_dictionary[Ds] + 1
                            else:
                                date_dictionary[Ds] = 1
                    f2.close()
            date_dictionary1 = sorted(date_dictionary.iteritems(), key=lambda d:d[0])
            for Ds,cnt in date_dictionary1:
                writeArtistPlays(artist_id,Ds,cnt)

            f1.close()


