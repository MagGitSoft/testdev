# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 01:10:50 2015

@author: Magnus
"""
import os
from os.path import dirname, realpath, abspath


with open((os.path.join(dirname(__file__), "text.txt")), "r") as file:
    data = file.readlines()
    for line in data:
        words = line.split()
        print(words)