# write a program to acept maarks 6 students and display them in a shorted manmer
import msilib


markS1=int(input("enter the nuber : "))
markS2=int(input("enter the nuber : "))
markS3=int(input("enter the nuber : "))
markS4=int(input("enter the nuber : "))
markS5=int(input("enter the nuber : "))
markS6=int(input("enter the nuber : "))

markStudent=[markS1,markS2,markS3,markS4,markS5,markS6]

markStudent.sort()
print(markStudent)
 

