#!/usr/bin/env python3

# This script uses the IE data to create GPA and unit rows in the STS so exam numbers can be created later on

import csv
import pandas as pd
import numpy as np
from datetime import datetime
import os

# the csv getting the new column 'ExamNumber' as well as doing the SUMS and stringigying 'University ID'
# missingen = pd.read_csv('gpaextract.csv', dtype = 'str')
missingen = pd.read_csv('~/Downloads/gpahours.csv', converters={'IUID': lambda x: str(x), 'Term': lambda x: str(x)})

missingen['TermUnits'] = missingen['Total Term Units'] + missingen['Units In Progress For GPA']
missingen['CumulativeUnits'] = missingen['Total Cumulative Units'] + missingen['Units In Progress For GPA']
missingen['ExamNumber'] = ""

# writing this new organization to a CSV
missingen.to_csv('gpahours2.csv', index=False)

#opening the CSV and reading all the needed columns
gpahourspd = pd.read_csv('gpahours2.csv', converters={'IUID': lambda x: str(x)}) [['IUID', 'Term', 'ExamNumber', 'TermUnits', 'CumulativeGPA', 'CumulativeUnits']]

# writing all tha data to the XLSX according to the template
filedate = datetime.now().strftime("%Y%m%d%H%M")
# termcode = '4232'
termcode = str(gpahourspd.loc[1].Term)
gpahourspd.to_excel('NewGPAsyes' + '-' + filedate + '-' + termcode + '.xlsx', index=0)
# removing the temporary csv document
os.remove('gpahours2.csv')
# final check is a print if all has run as expected
print('newGPAsyes populated')
