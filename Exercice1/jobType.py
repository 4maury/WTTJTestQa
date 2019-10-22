#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 16:29:05 2019

@author: amaury
"""

class JobType:
    """Classe définissant une profession avec:
    - id : entier
    - name : string
    - categoryName : string"""
    
    def __init__(self, id, name, categoryName):
        """Constructeur de JobType"""
        self.id = id
        self.name = name
        self.categoryName = categoryName
