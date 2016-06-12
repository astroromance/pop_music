#coding=utf-8

import os
import shutil
import csv
import pandas as pd

dataPrefix = '../data/artist_plays/'
resultPrefix = '../result/'

def calc_mean_of_last_week(write,artistFile):
    artist_id = artistFile[0:-4]
    data = pd.read_csv(dataPrefix+artistFile)
    data = data.cnt
    last_week_data = data[-7:-1]
    Play = int(pd.Series.mean(last_week_data))
    dateRange = pd.date_range('20150901','20151030')
    for Ds in dateRange:
        write.writerow([artist_id,Play,Ds.strftime('%Y%m%d')])

def prediction():

    if os.path.exists(resultPrefix):
        shutil.rmtree(resultPrefix)
    os.mkdir(resultPrefix)
    f1 = open(resultPrefix+'mean_of_last_week.csv','ab')
    write = csv.writer(f1)
    if os.path.exists(dataPrefix):
        artistFileList = os.listdir(dataPrefix)
        for artistFile in artistFileList:
            calc_mean_of_last_week(write,artistFile)
    f1.close()

if __name__ == '__main__':
    prediction()