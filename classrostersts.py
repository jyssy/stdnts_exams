# new student rosters script for STS new student upload each semester as Upload Roster in STS

import csv
import pandas as pd
from datetime import datetime
import os
import re
import glob

# Globbing the file extension 
file_type = ".txt"
iuieExtract = glob.glob("*" + file_type)

# opening the 'globbed' text file and adding the comma separations
# opening the original extracted text file (renamed with the term added), using regex, and writing that new data to a temp csv file that will be deleted at the end of the script by running os.remove()
for file in iuieExtract:	
	with open(file, 'r') as extracted:
		extractreader = csv.reader(extracted, delimiter='\t')
		with open('newextract.csv', 'w') as newextract:
			extractwriter = csv.writer(newextract, delimiter=',')
			for line in extractreader:
				extractwriter.writerow(line)
# the section in which pandas selects the necessary columns from the csv
#newextractpd = pd.read_csv('newextract.csv', dtype = str) 
#OR -- if we apply the dtype=str ONLY to specific columns and not ao ALL the columns as the line does above:
newextractpd = pd.read_csv('newextract.csv', converters={'University ID': lambda x: str(x)}) [['Term Code', 'Units Taken', 'Primary Program Code',
	'Class Number', 'Subject Area', 'Course Catalog Number',
	'Course Description', 'Official Grade', 'University ID',
	'Enrollment Status Code', 'Instructor Name', 'Preferred Full Name']]
# 'Preferred Full Name' needs to be 'Primary Full Name' in the final document
newextractpd.rename(columns={"Preferred Full Name":"Primary Full Name"}, inplace=True)
newextractpd.rename(columns={"Term Code":"Term"}, inplace=True)
# adding a space after the comma
newextractpd['Primary Full Name'] = newextractpd['Primary Full Name'].str.replace(', *', ', ', regex=True)
newextractpd['Instructor Name'] = newextractpd['Instructor Name'].str.replace(', *', ', ', regex=True)
# writing all tha data to the XLSX according to the template
filedate = datetime.now().strftime("%Y%m%d")
termcode = str(newextractpd.loc[1].Term)
newextractpd.rename(columns={"Term":"Term Code"}, inplace=True)
newextractpd.to_excel('ClassRosterUpload' + '-' + filedate + '-' + termcode + '.xlsx', index=0)
# removing the temporary csv document
os.remove('newextract.csv')
# final check is a print if all has run as expected
print('Class Roster populated')



