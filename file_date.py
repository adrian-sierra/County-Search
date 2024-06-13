import random
from datetime import date

def fileDateGenerator(offenseDate):
    fileDateMonth = offenseDate.month
    fileDateDay = offenseDate.day
    fileDateYear = offenseDate.year

    randomFileDateMonth = random.randrange(1, 12)
    randomFileDateDay = random.randrange(1, 31)
    randomFileDateYear = random.randrange(fileDateYear, 2024)
    while (randomFileDateYear == fileDateYear and  randomFileDateMonth <= fileDateMonth and  randomFileDateDay <= fileDateDay):
        randomFileDateMonth = random.randrange(1, 12)
        randomFileDateDay = random.randrange(1, 31)
        randomFileDateYear = random.randrange(fileDateYear, 2024)

    return date(randomFileDateYear, randomFileDateMonth, randomFileDateDay)