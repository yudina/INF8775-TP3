# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 13:31:35 2018

@author: kevin
"""
import os

#               'ex2.1', 'ex2.2', 'ex2.3', 'ex2.4', 'ex2.5',
#                'ex3.1', 'ex3.2', 'ex3.3', 'ex3.4', 'ex3.5', 
#                'ex4.1', 'ex4.2', 'ex4.3', 'ex4.4', 'ex4.5', 
#                'ex5.1', 'ex5.2', 'ex5.3', 'ex5.4', 'ex5.5'

for i,j in zip(['ex1.1', 'ex1.2','ex1.3', 'ex1.4', 'ex1.5']
               ['ex1.1', 'ex1.2','ex1.3', 'ex1.4', 'ex1.5']):
    os.system('python conv.py --ex1 %s --ex2 %s' % (i,j))
