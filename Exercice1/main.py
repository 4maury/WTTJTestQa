#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 16:35:15 2019

@author: amaury
"""
import csv
import jobType
import jobOffer
def main():
    """Main function :
    No input
    Output : the desired tab"""

    # Read the job offers CSV file and fill a list with it
    jobOfferList = []
    with open('/home/amaury/Bureau/Test Technique - QA Engineer/appendix/technical-test-jobs.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        header = True
        for row in csv_reader:
            if header:
                print(f'Job offers column names are {", ".join(row)}')
                header = False
            else:
                job = jobOffer.JobOffer(row[0], row[1], row[2], row[3], row[4])
                jobOfferList += [job]
        print("Number of imported offers : " + str(len(jobOfferList)) + "\n")
    
    # Read the job types CSV file and fill a list with it
    jobTypeList = []
    with open('/home/amaury/Bureau/Test Technique - QA Engineer/appendix/technical-test-professions.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        header = True
        for row in csv_reader:
            if header:
                print(f'Job types column names are {", ".join(row)}')
                header = False
            else:
                job = jobType.JobType(row[0], row[1], row[2])
                jobTypeList += [job]
        print("Number of imported types : " + str(len(jobTypeList)))
    
    #Create an empty output tab with all the lines and columns
    
    #Update the output tab
    
    #Show the tab
    

main()  