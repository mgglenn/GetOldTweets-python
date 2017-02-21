import os
import subprocess
import sys
import csv


program_args = ["python", \
                "newExporter.py", \
                "--querysearch", \
                "\"zika\"", \
                "--since", \
                "", \
                "--until", \
                "" ,\
                "--filename" ,\
                "" ]

since_index = 5
until_index = 7
file_index = 9

year = 2016
may = 5
april = 4

day = 16

while day < 30 :

    year_month = str(year) + "-" + str(april)

    since_date = year_month + "-" + str(day)
    until_date = year_month  + "-" + str(day + 1)
    filename = "tweets_by_date/" + since_date + ".csv"
    
    program_args[since_index] = since_date
    program_args[until_index] = until_date
    program_args[file_index] = filename

    print "--------> collecting tweets on " + since_date
    
    program_output = subprocess.call(program_args)

    day = day + 1

since_date = year_month + "-" + str(day) 
until_date = "2016-5-1" 

filename = "tweets_by_date/" + since_date + ".csv"                                    

program_args[since_index] = since_date
program_args[until_index] = until_date
program_args[file_index] = filename
    
print "--------> collecting tweets on " + since_date
program_output = subprocess.call(program_args)

day = 1

while day < 18 :
    year_month = str(year) + "-" + str(may)

    since_date = year_month + "-" + str(day)
    until_date = year_month  + "-" + str(day + 1)
    filename = "tweets_by_date/" + since_date + ".csv"

    program_args[since_index] = since_date
    program_args[until_index] = until_date
    program_args[file_index] = filename
    
    print "--------> collecting tweets on " + since_date
    program_output = subprocess.call(program_args)

    day = day + 1

