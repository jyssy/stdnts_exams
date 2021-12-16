#!/usr/bin/env python3

# rearranging the 'Enrollment Roster by Program Stack' file from IE

import csv
import pandas as pd
import os
import re

# opening the original text file and adding the comma separations
with open('extract_14568132.txt', 'r') as enrollment:
	enrollmentstk = csv.reader(enrollment, delimiter='\t')
	with open('enrollmentroster.csv', 'w') as newenrollment:
		enrollmentwriter = csv.writer(newenrollment, delimiter=',')
		for line in enrollmentstk:
			enrollmentwriter.writerow(line)
			
# making sure to convert data types to strings
enrollment = pd.read_csv(r'enrollmentroster.csv', dtype=str)
enrollment.to_csv('enrollmentroster.tsv', index=False, encoding='utf-8', sep='\t')

# selecting the columns from the tsv in order
#enrollment = pd.read_csv(r'enrollmentroster.tsv', dtype=str, sep='\t')
# OR ...
enrollment = pd.read_csv(r'enrollmentroster.tsv', sep='\t', converters={'University ID': lambda x: str(x)}) [['Class Number', 'Subject Area', 'Course Catalog Number', 'Course Description', 'Units Taken', 
	'Instructor Name', 'Official Grade', 'University ID', 'Preferred Full Name', 
	'Total Cumulative Units', 'Primary Program Code', 'Enrollment Status Code', 
	'Local Address Line 1', 'Local Address Line 2', 'Local Address City', 
	'Local Address State Code', 'Local Address Zip Code', 'Local Address Phone Nbr', 'Home Address Line1', 'Home Address Line2', 'Home Address City', 'Home Address State Code', 
	'Home Address Zip Code', 'Home Address Phone Nbr', 'Network ID', 'GDS Campus Email Address', 
	'FERPA Complete Restriction Indicator', 'FERPA Local Address Restriction Indicator', 
	'FERPA Local Phone Restriction Indicator', 'FERPA Home Address Restriction Indicator', 
	'FERPA Home Phone Restriction Indicator']]

# renaming the 'Preferred Full Name' to 'Primary Full Name'
enrollment.rename(columns={"Preferred Full Name":"Primary Full Name"}, inplace=True)

#regexxing the comma and adding a space 
enrollment['Instructor Name'] = enrollment['Instructor Name'].str.replace(', *', ', ', regex=True)
enrollment['Primary Full Name'] = enrollment['Primary Full Name'].str.replace(', *', ', ', regex=True)

# writing the final tsv text document
enrollment.to_csv('EnrollmentRoster.txt', index=0, sep='\t')

# removing the temp files
os.remove('enrollmentroster.csv')
os.remove('enrollmentroster.tsv')

print('Enrollment Roster Text File Made')
