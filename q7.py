n=int(input("Enter number of elements N in fibonacci series:\n[N must be positive Integer]: N="))

if n<=0 :
    print("\nError\nNumber of elements in fibonacci series must be integer and greater than zero.")

else:
   
    if n == 1:
        print("\nThe fibonacci series with 1 element is shown below\n[1]")
        print("\nAverage of given fibonacci series is", 1)

    elif n == 2:
        print("\nThe fibonacci series with 2 element is shown below\n[1,1]")
        print("\nAverage of given fibonacci series is", 1)
    
    else:
        
        list1 = [1, 1]
        
        a = 1
        b = 1
        
        for i in range(n - 2):
            s = a + b
            list1.append(s)
            a = b
            b = s
        
        print(f"\nThe fibonacci series with {n} elements is shown below:")
        print(list1)
        
        sum = 0    #intial sum=0
        
        for num in list1:
            sum = sum + num
        average = (sum / n)
        
        two_decimal = "{:.2f}".format(average)
        
        print(f"\nAverage of given fibonacci series is {two_decimal}")
