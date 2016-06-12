#coding=utf-8

import time
from split_by_songs import splitBySongs
from split_by_artist import splitByArtist
from calc_artist_plays import calcArtistPlays

if __name__ == "__main__":
    print "="*64
    t0 = time.time()
    splitByArtist()
    t1 = time.time()
    print "cost %f s, split by artist" %(t1-t0)
    splitBySongs()
    t2 = time.time()
    print "cost %f s, split by songs" %(t2-t1)
    calcArtistPlays()
    t3 = time.time()
    print "cost %f s, calc artist plays" %(t3-t2)