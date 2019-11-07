# -*- coding: utf-8 -*-
import os
import numpy as np
import pandas as pd
import calendar
import math

days = [31,28,31,30,31,30,31,31,30,31,30,31]

def loaddataExcel(dataFilePath):
    return np.array(pd.read_excel(dataFilePath))

def main(dataFilePath, linebegin):
    
    firstdateline = linebegin

    # 把每行每列，返回到一个二维数组中
    arrayData = loaddataExcel(dataFilePath)
    year = arrayData[linebegin - 2][1]

    nRange = 12
    if year == 2019:
        nRange = 8

    for i in range (0,nRange):
        month = i + 1
        daysnum = days[i]
        if month == 2 and calendar.isleap(year):
            daysnum = 29

        enddateline = firstdateline + daysnum - 1
        
        
        sum1 = 0
        sum2 = 0
        sum3 = 0
        for line in range(firstdateline, enddateline+1):
            dataline = arrayData[line - 2]
            
            avemax = dataline[5]
            if math.isnan(avemax):
                sum1 += 0
            else:
                sum1 += avemax

            avemin = dataline[7]
            if math.isnan(avemin):
                sum2 += 0
            else:
                sum2 += avemin

            aveave = dataline[9]
            if math.isnan(aveave):
                sum3 += 0
            else:
                sum3 += aveave

        ave1 = round(sum1 / daysnum, 1)
        ave2 = round(sum2 / daysnum, 1)
        ave3 = round(sum3 / daysnum, 1)

        print (year, '\t', month, '\t', ave1, '\t', ave2, '\t', ave3)

        firstdateline = enddateline + 1


if __name__ == "__main__":
    for root,dirs,files in os.walk(r"C:\Users\Administrator.3DLZQQ2VJC0X4S5\Desktop\Day\13.Iqaluit-daily"):
        for file in files:
            #获取文件路径
            dataFilePath = os.path.join(root,file)
            linebegin = 26
            main(dataFilePath,linebegin)
    