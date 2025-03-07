"""
use today's date as seed

"""
from collections import OrderedDict
from datetime import datetime

import numpy as np
import os
import json
import copy

roster = [
    "Dylan C Aaron",
    "Addison Horton Armistead",
    "Julian Leon-Adrian Beloiu",
    "Aanya Bhandari (say last name)",
    "Siddharth August Bianchi",
    "Alejandra Casillas",
    "Samuel Castillo",
    "Emily Chacko",
    "Eren Chang",
    "Diana Ciuculin",
    "Reese Friar",
    "Thorin Groth",
    "Turner Hilton",
    "Hristina Kostadinova",
    "Aanya Manvi (say last name)",
    "Victoria Manzato",
    "David Murillo",
    "Sai Naru",
    "Zachary Pipping (say last name)",
    "Chris Ramroth",
    "Vinay Ratnam",
    "Eric Reed",
    "Mayrav Saketkhou",
    "Avi Shah",
    "Aidan Tambling",
    "Tuyen Truong",
    "Luke Unbehagen",
    "George VanVeckhoven",
    "Andrew Wilson",
    "Matthew Wirnowski",
    "Quinn Yuan",
    "Zachary Zeng (say last name)"
]

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(SCRIPT_DIR, 'answers.json')
COUNT = len(roster)

def balance_prob(data):
    """
    Takes in dict.

    Creates a deep copy of the raw amounts students have been called on, 
    then assigns probabilities based on the inverse of the frequency.

    Returns dict.
    """
    prob = copy.deepcopy(data)
    tot = 0
    for name in data.keys():
        prob[name] = (1/(prob[name] + 1))
        tot += prob[name]
    for name in data.keys():
        prob[name] /= tot
    return prob

def dump_to_file(path, data):
    """
    Takes in string to path and dict

    Takes the data and dumps to a specified path as a json file

    Returns None
    """

    with open(path, 'w') as j:
        json.dump(data, j, indent=4)
        return

def read_from_file(path):
    """
    Takes in string to path

    Reads the json file at path for conversion into dict, if it doesn't exist, create empty file

    Returns either None or a dict
    """
    if not os.path.exists(path):
        dump_to_file(path, '')
        return
    else:
        with open(path, 'r') as f:
            data = json.load(f)
            return data

def main():
    answers = read_from_file(PATH)
    if answers is None:
        answers = OrderedDict()
        for name in roster:
            answers[name] = 0

    seed = int(datetime.today().strftime('%Y%m%d'))

    np.random.seed(seed)

    while True:
        choice = input("\nChoose an option:\n"
    "1 - Pseudorandom selection (seeded by date)\n"
    "2 - Weighted probabilities (seeded by date)\n"
    "\nEnter your choice: ")
        prob = list(balance_prob(answers).values())
        if choice == '1':
            random_idx = np.random.randint(0, len(roster))
        elif choice == '2':
            random_idx = np.random.choice(range(0,len(roster)), p=prob)
        answers[roster[random_idx]] += 1
        print("\n" + roster[random_idx],end='\n')
        yn = input("\nDid they answer the question (y/n): ")
        if yn == 'y':
            pass
        elif yn =='n':
            answers[roster[random_idx]] -= 1
        dump_to_file(PATH, answers)
        

if __name__ == "__main__":
    main()
