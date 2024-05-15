#!/usr/bin/env python3

# This script uses the IE data to create GPA and unit rows in the STS so exam numbers can be created later on
# Functionally, there are semesters we need the current GPAs and some we don't. Depends on whether the report is run early on the next semester or later on
            
# setting up the two types of GPA uploads, one w/ GPAs and one w/o GPAs
yesno = input('Do you want the CumulativeGPA, yes or no? ')

if yesno == 'yes':
    
    exec(open('NewGPAyes2.py').read())

elif yesno == 'no':
    
    exec(open('NewGPAno2.py').read())

else:
    print("Start over, please. The answer must be 'yes' or 'no'")
