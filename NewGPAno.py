#!/usr/bin/env python3

# This script uses the IE data to create GPA and unit rows in the STS so exam numbers can be created later on

import csv
import pandas as pd
import numpy as np
from datetime import datetime
import os
import re

# the csv getting the new column 'ExamNumber':
missingen = pd.read_csv('gpaextract.csv', dtype = 'str')
missingen = pd.read_csv('gpaextract.csv', converters={'University ID': lambda x: str(x)})

missingen['TermUnits'] = missingen['Total Term Units'] + missingen['Units In Progress For GPA']
missingen['CumulativeUnits'] = missingen['Total Cumulative Units'] + missingen['Units In Progress For GPA']
missingen['ExamNumber'] = ""
missingen['CumulativeGPA'] = ""

# writing this new organization to a CSV
missingen.to_csv('gpaextract.csv', index=False)

# opening the CSV and reading all the needed columns
gpaextractpd = pd.read_csv('gpaextract.csv', converters={'University ID': lambda x: str(x)}) [['University ID', 'Term Code', 'ExamNumber', 'CumulativeGPA', 'TermUnits', 'CumulativeUnits']]

# renaming the two columns that are still with the old name from the IUIE pull
gpaextractpd.rename(columns={"University ID":"IUID"}, inplace=True)
gpaextractpd.rename(columns={"Term Code":"Term"}, inplace=True)

# writing all tha data to the XLSX according to the template
filedate = datetime.now().strftime("%Y%m%d")
gpaextractpd.to_excel('NewGPAs' + '-' + filedate + '-' + termcode + '.xlsx', index=0)
# removing the temporary csv document
os.remove('gpaextract.csv')
# final check is a print if all has run as expected
print('newGPAs populated')
            

