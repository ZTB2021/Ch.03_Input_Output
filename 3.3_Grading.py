'''
Grading PROGRAM
---------------
Create a program that asks the user for their semester grade, final exam grade, 
and final exam worth and then calculates the overall final grade. 
Ask your instructor if you don't know how to calculate weighted averages.
You don't have to print out the letter grade. We will do that in the next chapter.

Test with the following:

Sem Grade: 86   Final Exam: 52   Exam worth: 15%    Overall: 80.9
Sem Grade: 95   Final Exam: 32   Exam worth: 10%    Overall: 88.7
Sem Grade: 72   Final Exam: 100   Exam worth: 20%    Overall: 77.6
'''
semG = float(input("What is the semester grade"))
FE = float(input("what did you get on the Final exam"))
EW = float(input("how much is the exam worth"))
semw = 100-EW
OG = (semG*semw/100)+(FE*EW/100)
print("your overall grade is", OG)