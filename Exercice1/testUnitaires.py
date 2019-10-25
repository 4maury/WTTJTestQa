#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 16:37:28 2019

@author: amaury
"""

import random
import unittest
import usefulFunctions
import csv

class TestUnitaires(unittest.TestCase):
    """Classe implémentant les tests unitaires de mo, programme"""
    
    def testReadingOffers(self):
        """Check if the correct number of lines are read in the offer CSV"""
        nbLines = 0
        with open("/home/amaury/Bureau/Test Technique - QA Engineer/appendix/technical-test-jobs.csv") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            for row in csv_reader:
                nbLines+=1
        jobOfferList, professionsList = usefulFunctions.readCsv()
        self.assertEqual(nbLines, len(jobOfferList)+1) # +1 for the header
        
    def testReadingProfessions(self):
        """Check if the correct number of lines are read in the profession CSV"""
        nbLines = 0
        with open("/home/amaury/Bureau/Test Technique - QA Engineer/appendix/technical-test-professions.csv") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            for row in csv_reader:
                nbLines+=1
        jobOfferList, professionsList = usefulFunctions.readCsv()
        self.assertEqual(nbLines, len(professionsList)+1) # +1 for the header
        
    def testDropDuplicates(self):
        """ Check if no item is forgotten"""
        # Create a list of 100 numbers between 0 and 20
        listTest = []
        for i in range(100):
            listTest += [random.randint(0, 20)]
        
        droppedList = usefulFunctions.dropDuplicates(listTest)
        for item in listTest:
            self.assertIn(item, droppedList) # Check if every item of the initial list is present after the drop duplicate
            
    def testTotal(self):
        """Check if the total of the lines and columns are the same"""
        
        # Create a table and fill the totals
        table = []
        for i in range(10):
            line = []
            for i in range(8):
                line+=[0]
            table+=[line]
        for i in range(2, 10):
            for j in range(2, 8):
                table[i][j]=random.randint(0, 500)
        table = usefulFunctions.fillTotals(table)
        
        # Count the line and columns total
        colTot = 0
        for i in range(2, 10):
            colTot+=table[i][1]
        lineTot=0
        for j in range(2, 8):
            lineTot+=table[1][j]
        self.assertEqual(lineTot, colTot)
        
    def testTotal2(self):
        """Check if the total of the table is the sum of every cells"""
        
        # Create a table and fill the totals
        table = []
        for i in range(10):
            line = []
            for i in range(8):
                line+=[0]
            table+=[line]
        for i in range(2, 10):
            for j in range(2, 8):
                table[i][j]=random.randint(0, 500)
        table = usefulFunctions.fillTotals(table)
        
        # Calculate the total
        total=0
        for i in range(2, 10):
            for j in range(2, 8):
                total+=table[i][j]
        self.assertEqual(total, table[1][1])

        
        