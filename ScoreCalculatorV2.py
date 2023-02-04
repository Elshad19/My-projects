#V1
import time
def tc():
    print("This small project will help you to easily calculate total scores of students. \nPlease, write KSQ1 score.")
    ksq1 = input()
    print("KSQ1 score is " + ksq1)
    ksq1 = int(ksq1)

    print()

    print("Please, write KSQ2 score.")
    ksq2 = input()
    print("KSQ2 score is " + ksq2)
    ksq2 = int(ksq2)

    print()

    print("Please, write KSQ3 score.")
    ksq3 = input()
    print("KSQ3 score is " + ksq3)
    ksq3 = int(ksq3)

    print()

    print("Please, write BSQ score.")
    bsq = input()
    print("BSQ score is " + bsq)
    bsq = int(bsq)

    print()

    sumKSQ = (ksq1 + ksq2 + ksq3) / 3
    beforerounding = sumKSQ
    beforerounding = str(beforerounding)
    print("Before rounding numerical average,  initial score is " + beforerounding + ".")

    print ()

    sumKSQ = round(sumKSQ)
    sumKSQ = str(sumKSQ)
    print("First, we find numerical average of KSQ scores. They are added first and then divided by three. \nRounded up numerical average is " + sumKSQ + ".")
    sumKSQ = int(sumKSQ)

    print()

    sumKSQ = sumKSQ * 40 / 100
    beforerounding2 = sumKSQ
    beforerounding2 = str(beforerounding2)
    print("Before rounding 40% value of numerical average, initial score is " + beforerounding2 + ".")

    print ()

    sumKSQ = round(sumKSQ)
    sumKSQ = str(sumKSQ)
    print("Then, we find 40% of numerical average. \nRounded up value is " + sumKSQ + ".")
    sumKSQ = int(sumKSQ)

    print()

    sumBSQ = bsq * 60 / 100
    beforerounding3 = sumBSQ
    beforerounding3 = str(beforerounding3)
    print("Before rounding 60% value of BSQ score, initial score is " + beforerounding3 + ".")

    print()

    sumBSQ = round(sumBSQ)
    sumBSQ = str(sumBSQ)
    print("Third, we find 60% value of BSQ score. \nRounded up value is " + sumBSQ + ".")
    sumBSQ = int(sumBSQ)

    print()

    totalScore = (sumKSQ + sumBSQ)
    totalScore = str(totalScore)
    print("At last, we combine two values by adding. \nTotal score is " + totalScore + ".")
  
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
