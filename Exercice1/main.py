#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 16:35:15 2019

@author: amaury
"""

import usefulFunctions

def main():
    """Main function
    Returned the desired tab of the exercise"""

    # Read the CSV and get its content
    jobOfferList, professionsList = usefulFunctions.readCsv()
    
    # Create an empty output tab with the right number of lines and columns
    finalTab = usefulFunctions.createEmpty(jobOfferList, professionsList)
    
    # Fill the tab
    finalTab = usefulFunctions.fillTabExceptTotals(jobOfferList, professionsList, finalTab)
    
    # Update the totals 
    finalTab = usefulFunctions.fillTotals(finalTab)
 
main()  