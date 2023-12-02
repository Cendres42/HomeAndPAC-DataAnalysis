# import of fonction files

from Donnees_PAC import *
from Analyses_PAC import *
import os

# cleanup fonction of the data: create a csv file, split the PAC data then concatenate data PAC and temp
# temporary file was needed and them removed so as to concatenate 
def nettoyage_donnees():
    data=ouverture()
    splitData(data)
    data2=concatDonneesPACetTEMP('tempLongue_salon.csv')
    data2.to_csv('C:/Users/Gwen/Desktop/Data/Maison/concat.csv', sep=";",index=False)
    data3=pd.read_csv('C:/Users/Gwen/Desktop/Data/Maison/concat.csv', sep=";")
    data4=groupage(data3)
    #data5.to_csv('C:/Users/Gwen/Desktop/Data/Maison/groupage.csv', sep=";",index=False)
    convertData(data4)
    #nous devrions vérifier si le fichier existe ou non avant de le supprimer.
    if os.path.exists('C:/Users/Gwen/Desktop/Data/Maison/concat.csv'):
        os.remove('C:/Users/Gwen/Desktop/Data/Maison/concat.csv')
    else:
        print("Impossible de supprimer le fichier car il n'existe pas")

# nettoyage_donnees()

# data vizualisation fonctions beetwen many PAC data and temperature of home
def dataviz_PAC():
    courbes2X('time','outletWaterTemp','tempToKeep',' Température eau et température salon ')
    courbes2X('time','PCforHeat','outletWaterTemp','Fonctionnement PAC et température eau ')
    courbes2X('time','PCforHeat','tempToKeep','Fonctionnement PAC et température salon ')
    courbes2X('time','outdoorTemp','tempToKeep','Température extérieure et température salon ')
    courbes2X('time','outdoorTemp','PCforHeat','Température extérieure et fonctionnement PAC')

#dataviz_PAC()