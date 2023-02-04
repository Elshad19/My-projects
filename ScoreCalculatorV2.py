#pylint:disable=E0001
import time

#What is new(V2): slight delay between calculations, option to redo the proccess are added.

def tc():
    print("This small project will help you to easily calculate total scores of students. \nPlease, write sub summative (SS) 1 score.")
    ksq1 = input()
    print("SS1 score is " + ksq1)
    ksq1 = int(ksq1)
 
    print()

    print("Please, write SS2 score.")
    ksq2 = input()
    print("SS2 score is " + ksq2)
    ksq2 = int(ksq2)

    print()

    print("Please, write SS3 score.")
    ksq3 = input()
    print("SS3 score is " + ksq3)
    ksq3 = int(ksq3)

    print()

    print("Please, write big summative (BS) score.")
    bsq = input()
    print("BS score is " + bsq)
    bsq = int(bsq)

    print("\nCalculating...")

    print()

    time.sleep(1.2)

    sumKSQ = (ksq1 + ksq2 + ksq3) / 3
    sumKSQ = str(sumKSQ)
    print("First, we find numerical average of small summative scores. They are added first and then divided by three. \nNumerical average is " + sumKSQ + ".")
    sumKSQ = float(sumKSQ)

    time.sleep(0.5)
    print()

    sumKSQ = sumKSQ * 0.4
    sumKSQ = str(sumKSQ)
    print("Then, we find 40% of numerical average. \nIt is " + sumKSQ + ".")
    sumKSQ = float(sumKSQ)

    time.sleep(0.5)
    print()

    sumBSQ = bsq * 0.6
    sumBSQ = str(sumBSQ) 
    print("Third, we find 60% value of big summative score. \nIt is " + sumBSQ + ".")
    sumBSQ = float(sumBSQ)

    time.sleep(0.5)
    print()

    totalScore = (sumKSQ + sumBSQ)
    totalScore = str(totalScore)
    print("At last, we combine two values by adding. \nTotal score is " + totalScore + ".")
 
    print("\nWould you like to try again? (1 = Yes or 0 = no)")
    
    def userInput():
        userAnswer = input()  
        if userAnswer == '1':
            tc()
        if userAnswer == '0':
            print("See you next time!")
        else :
            print("Please write either 1 or 0")
            userInput()
    userInput()
tc()