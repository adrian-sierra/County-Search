import random

def randomSixDigits():
    sixDigits = ""
    for i in range(6):
        sixDigits = sixDigits + str(random.randrange(0, 9))

    return sixDigits

def caseNumberGenerator(caseType, caseFileYear):
    caseNumber = ""
    caseType = caseType.lower()
    # print(caseType)
    if caseType == "criminal":
        caseNumber = caseNumber + "CR"
    elif caseType == "civil":
        caseNumber = caseNumber + "CV"
    elif caseType == "traffic":
        caseNumber = caseNumber + "TR"
    
    caseNumber = caseNumber + "-" + caseFileYear + "-"
    caseNumber = caseNumber + randomSixDigits()

    return caseNumber