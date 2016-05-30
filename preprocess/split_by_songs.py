
import csv
import os
import shutil

song_dictionary = {}

def writeBySong(song,data):
    fileName = song + '.csv'
    os.chdir('../data/song')
    if not song_dictionary.has_key(song):
        song_dictionary[song] = True
        f = open(fileName,'ab')
        write = csv.writer(f)
        write.writerow(['user_id','gmt_create','action_type','Ds'])
        write.writerow(data)
        f.close()
    else:
        f = open(fileName,'ab')
        write = csv.writer(f)
        write.writerow(data)
        f.close()
    os.chdir('../../preprocess')


# user_id, song_id, gmt_create, action_type,Ds
def splitBySongs():
    if os.path.exists('../data/song'):
        shutil.rmtree('../data/song')
    os.mkdir('../data/song')
    f = open('../data/mars_tianchi_user_actions.csv')
    rows = csv.reader(f)
    rows.next()
    for row in rows:
        song = row[1]
        del row[1]
        writeBySong(song,row)
