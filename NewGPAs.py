#!/usr/bin/env python3

# This script uses the IE data to create GPA and unit rows in the STS so exam numbers can be created later on
# Functionally, there are semesters we need the current GPAs and some we don't. Depends on whether the report is run early on the next semester or later on

import csv
import pandas as pd
import numpy as np
from datetime import datetime
import os
import re

with open('extract_14881648-4225.txt', 'r') as newgpa:
# getting term code for the file-naming at the end
	filetxt = str(newgpa)
	termc = re.findall(r'[0-9]{4}', filetxt)
	termcode = (termc[2])
	gpareader = csv.reader(newgpa, delimiter='\t')
	with open('gpaextract.csv', 'w') as gpaextract:
		gpawriter = csv.writer(gpaextract, delimiter=',')
		for line in gpareader:
			gpawriter.writerow(line)
            
# setting up the two types of GPA uploads, one w/ GPAs and one w/o GPAs
yesno = input('Do you want the CumulativeGPA, yes or no?')

if yesno == 'yes':
    
    exec(open('NewGPAyes.py').read())

elif yesno == 'no':
    
    exec(open('NewGPAno.py').read())

else:
    print("Start over, please. The answer must be 'yes' or 'no'")