#coding=utf-8

import os
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import dateutil

def genModelAndForecast(artistFile):
    data = pd.read_csv(artistFile)
    cnt = data.cnt
    Ds = data.Ds
    startDate = '%d' %Ds[0]
    endDate = '%d' %Ds[len(Ds)-1]
    #sm.tsa.datetools.date_parser()
    #idx = sm.tsa.datetools.dates_from_range(startDate,endDate)

    dateRange = pd.date_range(startDate,endDate)
    cnt.index = pd.date_range(startDate,endDate)
    l1 = len(dateRange)
    l2 = len(cnt)
    dta = cnt.diff(1)
    dta = dta.dropna()
    ar_model = sm.tsa.AR(dta)
    order = ar_model.select_order(40,'aic')
    arma_mod31 = sm.tsa.ARMA(dta,(order,0)).fit()

    resid = arma_mod31.resid

    predict_data = arma_mod31.predict('20150701','20150830',dynamic=True)
    print(predict_data)
    fig, ax = plt.subplots(figsize=(12,8))
    ax = dta.ix['20150301':].plot(ax=ax)
    predict_data.plot(ax=ax)

    plt.show(block=True)

if __name__ == "__main__":
    artistFileList = os.listdir('../data/artist_plays')
    os.chdir('../data/artist_plays/')
    for artistFile in artistFileList:
        genModelAndForecast(artistFile)