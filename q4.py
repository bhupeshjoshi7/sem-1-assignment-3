a=float(input("Enter Grade points to be evaluated: "))

if 9<a<=10:
    print("Your Grade is 'A+' and Outstanding performance")
elif 8<a<=9:
    print("Your Grade is 'A' and Excellent performance")
elif 7<a<=8:
    print("Your Grade is 'B+' and Very Good performance")
elif 6<a<=7:
    print("Your Grade is 'B' and Good performance")    
elif 5<a<=6:
    print("Your Grade is 'C+' and Average performance")
elif 4<a<=5:
    print("Your Grade is 'C' and Below Average performance")
elif a==4:
    print("Your Grade is 'D' and Poor performance")
if a<4 or a>10:
    print("Error Enter a Grade between 0-10 only")
    exit()