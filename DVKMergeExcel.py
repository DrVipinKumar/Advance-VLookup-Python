# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 22:22:33 2020

@author: lenovo
"""
import os
import pandas as pd

data_location = "excelfile/"
if os.path.exists(data_location) and os.path.exists("mainfile.xlsx"):
    for file in os.listdir(data_location):
        print("...Merging file "+file)
        df= pd.read_excel(data_location + file)
        mainfile = pd.read_excel("mainfile.xlsx");
        all_data = pd.merge(mainfile,df,on="Roll No",how="outer",sort=True);
        all_data.to_excel("mainfile.xlsx", index = False) 
    print("Merging completed succesfully")
else:
    print("\n")
    print("=======================For Your Help=============================")
    print("Create 'excelfile' folder and paste your all excel file in it")
    print("Paste mainfile.xlsx in current directory")
    print("=================================================================")
print("\n")
print("=====================Programmer Information======================")
print("Created By: Dr. Vipin Kumar")
print("Associate Professor, DCA")
print("& Addl. Head (Skill Development), SDFS")
print("KIET Groups of Institutions, Delhi-NCR, INDIA")
print("=================================================================")