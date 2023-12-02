import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import os
import seaborn as sns
import scipy.stats as st

# opening fonction
def ouverture():
    data = pd.read_csv('C:/Users/Gwen/Desktop/Data/Maison/PAC/aquarea.raw',header=None, sep=" " )
    data.rename(columns={0:'date', 1:'heure', 2:'toSplit'},inplace=True)
    return data

# fonction which split the concatenate data into 142 columns and create a csv file
def splitData(data):
    data_len=len(data['toSplit'].axes[0])
    #indice lignes
    i=0
    for j in range(207):
        data[j]=""     
    """
    dict={}
    for j in range(207):
        dict[j]=np.zeros(data_len,dtype=str))pà
    data=pd.concat([data,pd.DataFrame(dict)],axis=1)
    """
    for i in range (data_len) :
        dataToSplit=data.iloc[i,2] 
        #print(dataToSplit)
        #indice colonnes
        w=3
        t=0
        for t in range(0,406,2):
            #print(t,i,w)
            #print(dataToSplit[t:t+2])
            data.iloc[i,w]=dataToSplit[t:t+2]
            #print(data.iloc[i,w])
            w=w+1  
        i=i+1 
        #print(data.iloc[0:10,0:20])          
    del data['toSplit']
    #print(data.iloc[0:10,0:202])    
    data.to_csv('C:/Users/Gwen/Desktop/Data/Maison/PAC/aquarea.csv', sep=";",index=False)

# fonction to concatenate data from PAC and data from sensor (temp) from different datetimes
def concatDonneesPACetTEMP(nomF2):
    data2=pd.read_csv('C:/Users/Gwen/Desktop/Data/Maison/PAC/aquarea.csv',low_memory=False, sep=";")
    data = pd.read_csv('C:/Users/Gwen/Desktop/Data/Maison/PAC/'+ nomF2,sep=";")
    # to compare data we need a same column of datetime
    data2['time']=pd.to_datetime(data2['date']+" " +data2['heure'])
    data['time']=pd.to_datetime(data['time'])
    #print(data.head())
    #print(data2.head())
    #print(data2['time'])
    #print(data2.iloc[0:10,209])
    data2['tempToKeep']=""
    data2['hygroToKeep']=""
    DataLength=data['time'].size
    Data2Length=data2['time'].size
    i=0
    for j in range(5323,Data2Length-1,1) :
        print(j)
        value209=data2.iloc[j,209]
        while i<DataLength:
        #for i in range(DataLength-1 ):
            #print(data2.iloc[j,209],data.iloc[i,0],data2.iloc[j,209],data.iloc[i+1,0])
            if (value209>=data.iloc[i,0]) & (value209 < data.iloc[i+1,0]):
                data2.iloc[j,210]=data.iloc[i,7]
                data2.iloc[j,211]=data.iloc[i,4]
                print('i')
                print(i)
                #print(data.iloc[i,7])
                #print(data2.iloc[j,210:212])
                #print(j)
                break    
            i+=1      
    return data2
    #data2.to_csv('C:/Users/Gwen/Desktop/Data/Maison/testMM.csv', sep=";",index=False)

#concatDonneesPACetTEMP()

# fonction to keep only the commun datas, it meens the data who temp column is not null
def groupage(data):
    #data = pd.read_csv('C:/Users/Gwen/Desktop/Data/Maison/PAC/concat.csv', low_memory=False, sep=";")
    data_tronquee2=data.loc[~data['tempToKeep'].isnull(),:]
    print(data_tronquee2)
    #data_tronquee2.to_csv('C:/Users/Gwen/Desktop/Data/Maison/plop.csv', sep=";",index=False)
    return data_tronquee2

#data = pd.read_csv('C:/Users/Gwen/Desktop/Data/Maison/groupage.csv', low_memory=False, sep=";")
#groupage()
#data.to_csv('C:/Users/Gwen/Desktop/Data/Maison/groupage2.csv', sep=";",index=False)

# fonction to convert raw aquarea data (hexadecimal encoded) to decimal data and rename columns
def convertData(data):
    #chemin_absolu = os.path.abspath('C:/Users/Gwen/Desktop/Data/Maison/testMM.csv')
    #data = pd.read_csv(chemin_absolu,sep=";")
    data=data.rename(columns={'203':'outdoorTemp', '204':'outletWaterTemp', '205':'PCforHeat'},inplace=True)
    data_len=len(data['heure'].axes[0])
    i=0
    for i in range(data_len):
        changeOutdoorTemp=str(data.iloc[i,144])
        data.iloc[i,205]=int(changeOutdoorTemp,16)-128
        changeOutletWaterTemp=str(data.iloc[i,146])
        data.iloc[i,206]=int(changeOutletWaterTemp,16)-128
        changePCforHeat=str(data.iloc[i,195])
        data.iloc[i,207]=(int( changePCforHeat,16)-1)/5        
    data.to_csv('C:/Users/Gwen/Desktop/Data/Maison/PAC/aquareaVSTempSalon2.csv', sep=";",index=False)
#splitData(data)
#convertData()









def moyennes_mobiles():
    data = pd.read_csv('C:/Users/Gwen/Desktop/Data/Maison/temptoMM.csv',sep=";")
    data_len=len(data.axes[0])
    data['temp_tronquee']=""
    j=0
    w=12
    for i in range (17,data_len,25):
        data.iloc[w,10]=data.iloc[j:i,7].mean()
        j+=25
        w+=25
    data.to_csv('C:/Users/Gwen/Desktop/Data/Maison/testMM2.csv', sep=";",index=False)
