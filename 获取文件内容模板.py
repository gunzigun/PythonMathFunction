# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

def loaddataTxt(dataFilePath, departChar):
    return np.array(pd.read_csv(dataFilePath,sep=departChar,header=-1)).astype(np.float)

def loaddataExcel(dataFilePath):
    return np.array(pd.read_excel(dataFilePath))

if __name__ == "__main__":

    # 需要读取的文件路径
    dataFilePath = r"C:\Users\Administrator.3DLZQQ2VJC0X4S5\Desktop\PythonTest\PCAdata.txt"
    # 文件每行数据以什么分割
    departChar = "\t"
    # 把每行数据分割后，返回到一个二维数组中
    arrayData = loaddataTxt(dataFilePath, departChar)
    

    # 需要读取的文件路径
    dataFilePath = r"C:\Users\Administrator.3DLZQQ2VJC0X4S5\Desktop\PythonTest\xlsx-train.xlsx"
    # 把每行每列，返回到一个二维数组中
    arrayData = loaddataExcel(dataFilePath)
