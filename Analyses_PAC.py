import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import os
import seaborn as sns
import scipy.stats as st

# fonction to make 2 lineplots of 2 data columns with 2 different axis
def courbes2X(forx,fory1,fory2,titleC):
    data = pd.read_csv('C:/Users/Gwen/Desktop/Data/Maison/PAC/aquareaVSTempSalon.csv',sep=";")
    #data=data.iloc[0:3657,:]
    #data2 = pd.read_csv('C:/Users/Gwen/Desktop/Data/Maison/aquareaBis.csv', low_memory=False, sep=";")
    #data2=data2.iloc[0:3657,:]
    plt.figure()
    # first axis
    x=data[forx]
    y1=data[fory1]
    y2=data[fory2]
    fig, ax = plt.subplots()
    plt.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(40))
    plt.xticks(rotation=90)
    ax.plot(x, y1,'b')
    ax.set_xlabel(forx, fontsize=14)
    ax.set_ylabel(fory1, color="blue", fontsize=14)

    # second axis
    ax2 = ax.twinx()
    ax2.plot(x, y2,'r')
    ax2.set_xlabel(forx, fontsize=14)
    ax2.set_ylabel(fory2, color="red", fontsize=14)
    plt.title(titleC ,loc='center',pad=3,fontsize=15,color="Darkred",fontweight='bold')
   
 # legende from lineplots
    lines = [ax.get_lines()[0], ax2.get_lines()[0]]
    plt.gcf().subplots_adjust(left = 0.125, bottom = 0.414, right = 0.9, top = 0.9, wspace = 0.2, hspace = 0.2)
    plt.legend(lines, [fory1,fory2], loc="upper right")
    plt.savefig('C:/Users/Gwen/Desktop/Data/Maison/PAC'+ fory1 + '_' +fory2 + '.png', dpi=300, format="png")
    plt.show()

#courbes2X('time','outletWaterTemp','tempToKeep','Fonctionnement PAC et température salon ')

# measure of correlation
def calcul_pearson(data):
    
    #data2 = pd.read_csv('C:/Users/Gwen/Desktop/Data/Maison/PremieresDonnees/temp_salon.csv',sep=";")
    coeff_corr_temp_hygro_lissee=st.pearsonr(data['PCforHeat'],data['tempToKeep'])[0]
    print("Le coefficient de corrélation entre fonctionnement de la PAC et température est de : ", coeff_corr_temp_hygro_lissee)
    print("Le coefficient de détermination  entre fonctionnement de la PAC et température est de : ",coeff_corr_temp_hygro_lissee*coeff_corr_temp_hygro_lissee)
    coeff_corr_temp_hygro=st.pearsonr(data['PCforHeat'],data['outletWaterTemp'])[0]
    print("Le coefficient de corrélation entre fonctionnement de la PAC et température de l'eau dans les radiateurs : ", coeff_corr_temp_hygro)
    print("Le coefficient de détermination  entre fonctionnement de la PAC et température de l'eau dans les radiateurs : ",coeff_corr_temp_hygro*coeff_corr_temp_hygro)

#data = pd.read_csv('C:/Users/Gwen/Desktop/Data/Maison/PAC/aquareaVSTempSalon2.csv',sep=";")
#calcul_pearson(data)


# fonction to make a lineplot from differents columns with same axis
def courbesSameX(colx,coly1,coly2,title):
    data = pd.read_csv('C:/Users/Gwen/Desktop/Data/Maison/temptoMM.csv',sep=";")
    data2 = pd.read_csv('C:/Users/Gwen/Desktop/Data/Maison/aquareaBis.csv', low_memory=False, sep=";")
    plt.figure()
    sns.lineplot(data=data,x=colx,y=coly1,color="Blue")
    sns.lineplot(data=data2,x=colx,y=coly2,color="Red")
    plt.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(40))
    plt.title(title,loc='center',pad=3,fontsize=15,color="Darkred",fontweight='bold')
    plt.xlabel(colx)
    plt.ylabel(coly1 + " et " + coly2)
    plt.xticks(rotation=90)
    plt.gcf().subplots_adjust(left = 0.125, bottom = 0.214, right = 0.9, top = 0.9, wspace = 0.2, hspace = 0.2)
    plt.show()
    plt.savefig('C:/Users/Gwen/Desktop/Data/Maison/'+title+".png", dpi=300, format="png")
  
#courbes('heure','temp_lissee','PCforHeat','Fonctionnement PAC \n et température salon ')
#courbes('heure','temp_lissee','outletWaterTemp','Température eau \n et température salon ')