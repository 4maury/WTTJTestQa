#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 21:38:05 2019

@author: amaury
"""

import csv
import profession
import jobOffer

DELIMITER = ","
CSV_ROOT = "/home/amaury/Bureau/Test Technique - QA Engineer/appendix/"

def readCsv():
    """Read the CSV
    Return 2 lists with the content of each file"""
    # Read the job offers CSV file and fill a list with all its content
    jobOfferList = [] # Full list of offers
    with open(CSV_ROOT + 'technical-test-jobs.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=DELIMITER)
        header = True
        for row in csv_reader:
            if header: # Do not read the header
                header = False
            else:
                job = jobOffer.JobOffer(row[0], row[1], row[2], row[3], row[4]) # Create a JobOffer object
                jobOfferList += [job] # Add it to the full list
    
    # Read the job types CSV file and fill a list with all its content
    professionList = []
    with open(CSV_ROOT + 'technical-test-professions.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=DELIMITER)
        header = True
        for row in csv_reader:
            if header: # Do not read the header
                header = False
            else:
                job = profession.Profession(row[0], row[1], row[2]) # Create a JobType object
                professionList += [job] # Add it to the list
    
    return ([jobOfferList, professionList])


def dropDuplicates(list):
    """Input : a list
    Output : all the distinct values in the list"""
    uniqueValues = []
    for value in list:
        if value not in uniqueValues:
            uniqueValues += [value]
    return(uniqueValues)

def selectDistinctCategories(professionsList):
    """ Return the distinct categories of the professionList"""
    # Get all the profession categories
    profCategories = []
    for prof in professionsList: # Select all the profession categories
        profCategories += [str(prof.categoryName)]
             
    # Drop duplicates
    distinctCategories = dropDuplicates(profCategories)
            
    # Print them        
    print("\nProfession categories :")
    for cat in distinctCategories:
        print(cat)
    return distinctCategories

def selectDistinctContracts(jobOfferList):
    """ Return the distinct contracts types in the offers"""
    contracts = []
    for job in jobOfferList: # Select all the contract types
        contracts += [str(job.contractType)]
    contracts = dropDuplicates(contracts)
    print("\nContract types :")
    for cType in contracts:
        print(cType)
    return contracts

def createEmpty(jobOfferList, professionsList):
    """Create a tab with the correct first line and column filled with 0"""
     # Get all the contract types
    contractTypes = ["TOTAL"] + selectDistinctContracts(jobOfferList)
    
    # Create the first line (list of profession categories)
    firstLine = ["/", "TOTAL"] + selectDistinctCategories(professionsList)
    
    # Create the tab
    finalTab = [firstLine]
    for i in range(len(contractTypes)): # Go through all the lines of the future tab
        line = [contractTypes[i]] # First column = contract types
        for i in range(len(firstLine)-1): # Create empty fields
            line += [0]
        finalTab += [line]
    return finalTab

def fillTabExceptTotals(jobOfferList, professionsList, finalTab):
    """Count the offers in the jobOfferList and fill the finalTab"""
    for currentJobOffer in jobOfferList:
        
        # Find related profession
        for currentProfession in professionsList:
            if currentProfession.id == currentJobOffer.professionId:
                relatedProfession = currentProfession
                break
        
        # Get related profession column in the final tab
        relatedProfessionColumn=0
        for j in range(2, len(finalTab[0])): # Go through the first line of the final tab
            if finalTab[0][j]==relatedProfession.categoryName:
                relatedProfessionColumn = j
        
        # Fill the tab except totals
        for line in finalTab:
            if line[0]==currentJobOffer.contractType:
                line[relatedProfessionColumn]+=1
    
    return finalTab
    
def fillTotals(finalTab):
    """Count and fill every total of the final tab."""
    
    # 2nd line
    for j in range(2, len(finalTab[0])): # For each total of the 2nd line
        for i in range(2, len(finalTab)): # For all the column
            finalTab[1][j]+=finalTab[i][j] # Increment the total
    
    # 2nd column
    for i in range(2, len(finalTab)): # For each total of the 2nd column
        for j in range(2, len(finalTab[0])): # For all the lines
            finalTab[i][1]+=finalTab[i][j] # Increment the total
    
    # Global
    total = 0
    for i in range(2, len(finalTab)):
        total+=finalTab[i][1]
    finalTab[1][1]=total
    
    return finalTab
    
    