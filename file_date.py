import random

def fileDateGenerator(offenseDate):
    fileDate = ""
    offenseDateSplit = offenseDate.split("/")

    fileDateMonth = int(offenseDateSplit[0])
    fileDateDay = int(offenseDateSplit[1])
    fileDateYear = int(offenseDateSplit[2])

    randomFileDateMonth = random.randrange(1, 12)
    randomFileDateDay = random.randrange(1, 31)
    randomFileDateYear = random.randrange(fileDateYear, 2024)
    while (randomFileDateYear == fileDateYear and  randomFileDateMonth <= fileDateMonth and  randomFileDateDay <= fileDateDay):
        randomFileDateMonth = random.randrange(1, 12)
        randomFileDateDay = random.randrange(1, 31)
        randomFileDateYear = random.randrange(fileDateYear, 2024)

    fileDate = fileDate + str(randomFileDateMonth) + "/" + str(randomFileDateDay) + "/" + str(randomFileDateYear)

    return fileDate