import pandas as pd
from molmass import Formula
from functools import reduce
import os
import numpy as np
from fuzzywuzzy import fuzz
def save_value_counts(data, column):
    vc = data[column].value_counts().rename_axis('unique_values').to_frame('counts')
    vc.index.name = 'unique_values'
    vc.reset_index(inplace=True)
    return(vc)

def find_files(base, pattern):
    # print('i am in new')
    score = []
    for filename in os.listdir(base):
        score.append(fuzz.partial_ratio(filename,pattern))
    return(os.listdir(base)[np.argmax(score)])
def specify_column(keyword, column_name):
    score = []
    for name in column_name:
        score.append(fuzz.token_sort_ratio(keyword,name))
    return(column_name[np.argmax(score)])
def find_different_items(columns):
    if len(columns[0])<=len(columns[0]):
        temp1 = set(columns[0])
        temp2 = set(columns[1])
    else:
        temp1 = set(columns[1])
        temp2 = set(columns[0])
    # s = set(temp2)
    temp3 = [x for x in temp1 if x not in temp2]
    return(temp3)

def get_mono_mass(data, formula_column = "Formula"):
    mass = []
    for index, row in data.iterrows():
        mass.append(Formula(row[formula_column]).isotope.mass)
    data.insert(data.columns.get_loc(formula_column)+1, "Monoisotopic mass", mass)
    return(data)
def get_unique_list(list1):
    list_set = set(list1)
    unique_list = (list(list_set))
    return(unique_list)
def find_common_items(columns):
    return (list(reduce(set.intersection, map(set, columns))))




