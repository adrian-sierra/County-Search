import random

def randomSixDigits():
    sixDigits = ""
    for i in range(6):
        sixDigits = sixDigits + str(random.randrange(0, 9))

    return sixDigits

def caseNumberGenerator(caseType):
    caseNumber = ""
    caseType = caseType.lower()
    # print(caseType)
    if caseType == "criminal":
        caseNumber = caseNumber + "CR"
    elif caseType == "civil":
        caseNumber = caseNumber + "CV"
    elif caseType == "traffic":
        caseNumber = caseNumber + "TR"
    
    caseNumber = caseNumber + "-2024-"
    
    caseNumber = caseNumber + randomSixDigits()


    # print("hello, world")

    # if criminal: "CR"
    # if civil: "CV"
    # if traffic: "TR"

    # dash between key elements: "-"

    # date filed year: "2024"

    # dash between key elements: "-"

    # six random digits from 000000 to 999999, incrementing

    # example case: CR-2024-023928

    # need to get the case type information of an entry that is about
    # to get pushed into db, to then return a case number for that
    # corresponding entry

    # TODO
    # get entry data + return case number string

    return caseNumber