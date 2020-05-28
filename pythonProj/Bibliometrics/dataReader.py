import pandas as pd
import os
fileDir=os.path.abspath(os.path.dirname('__file__'))
dataDir=os.path.join(fileDir,'dataset')
def readData(datafile):
    fileData=os.path.join(dataDir,datafile)
    if fileData.endswith('xlsx'):
        return pd.read_excel(fileData)
    else:
        return pd.read_csv(fileData)