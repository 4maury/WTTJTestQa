#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 16:08:37 2019

@author: amaury
"""

class JobOffer:
    """Classe définissant une offre d'emploi avec:
    - professionId : entier
    - contractType : entier
    - name : string
    - officeLat : float
    - officeLong :float"""
    
    def __init__(self, profId, contractType, name, offLat, offLong):
        """Constructeur de JobOffer"""
        self.professionId = profId
        self.contractType = contractType
        self.name = name
        self.officeLat = offLat
        self.officeLong = offLong
    
