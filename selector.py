"""
use today's date as seed

"""

import numpy as np

from datetime import datetime


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



def main():
    position = 'main'

    seed = int(datetime.today().strftime('%Y%m%d'))

    np.random.seed(seed)

    while True:
        random_idx = np.random.randint(0,len(roster))
        print(roster[random_idx],end='\r')
        choice = input()


if __name__ == "__main__":
    main()
