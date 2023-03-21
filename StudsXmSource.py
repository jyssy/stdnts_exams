#!/usr/bin/env python3

# orders and rearragnges 'Enrollment Roster by Proxy' to set up what we need to populate Students and XmCourses, etc

import csv
import pandas as pd
import os
from datetime import datetime
import re

# opening the original text file and adding the comma separations
with open('extract_15410523.txt', 'r') as StXms1:
	StXms2 = csv.reader(StXms1, delimiter='\t')
	with open('StXms.csv', 'w') as StXms:
		StXmswriter = csv.writer(StXms, delimiter=',')
		for line in StXms2:
			StXmswriter.writerow(line)
			
# making sure to convert data types to strings
StXms_src = pd.read_csv(r'StXms.csv', dtype=str)

# Adding new columns needed
StXms_src['SuppressPic'] = 'N'
StXms_src['SuppressRecord'] = 'N'

StXms_src.to_csv('StXms.tsv', index=False, encoding='utf-8', sep='\t')

# selecting the columns from the tsv in order
StXms_src = pd.read_csv(r'StXms.tsv', sep='\t', converters={'University ID': lambda x: str(x), 'Instructor Name': lambda x: str(x), 'University ID': lambda x: str(x)}) [['Term Code', 'Units Taken', 'Primary Program Code', 'Class Number', 'Subject Area', 'Course Catalog Number', 'Course Description', 'Enrollment Status Code', 'Instructor Name', 'Instructor Email', 'University ID', 'Total Term Units', 'Cumulative GPA', 'Units In Progress For GPA', 'Cumulative Units Taken For GPA', 'Total Cumulative Units', 'Preferred Full Name', 'GDS Campus Email Address', 'Network ID', 'FERPA Complete Restriction Indicator', 'SuppressPic', 'SuppressRecord']]

# exams_src = exams_src.astype(str)
# regexxing the comma and adding a space 
StXms_src['Instructor Name'] = StXms_src['Instructor Name'].str.replace(', *', ', ', regex=True)
StXms_src['Preferred Full Name'] = StXms_src['Preferred Full Name'].str.replace(', *', ', ', regex=True)

# converting Units Taken to numeric
print(StXms_src.dtypes)
# StXms_src.to_numeric(['Units Taken'], downcast="float")

# Renaming columns
StXms_src.rename(columns={"Term Code":"Term"}, inplace=True)
StXms_src.rename(columns={"University ID":"UniversityID"}, inplace=True)
StXms_src.rename(columns={"Preferred Full Name":"Primary Full Name"}, inplace=True)

# writing the final tsv text document
filedate = datetime.now().strftime("%Y%m%d")
termcode = str(StXms_src.loc[1].Term)
StXms_src.to_excel('StudsXmsSource' + '-' + filedate + '-' + termcode + '.xlsx', sheet_name='studsxmsource', index=0)

# removing the temp files
os.remove('StXms.csv')
os.remove('StXms.tsv')

print('Students amd ExamSource document ready for upload')