try:

    num1=int(input("etnter the first number"))
    num2=int(input("etnter the second number"))

    print("CHOOSE OPERATION TO PERFORM: \n",
          "1. ADDITION\n",
          "2. SUBTRACTION\n",
          "3. DIVISION\n",
          "4. MULTIPLICATION\n"
                          )
    
    cal=input().strip().lower()
    
    if cal=="ADDITION":
        ans=num1+num2
    elif cal=="SUBTRACTION":
        ans=num1-num2
    elif cal=="DIVISION":
        if num2==0:
            print("not define:")
        else:
            ans=num1/num2    
    elif cal=="MULTIPLICATION":
        ans=num1*num2  

    else:
        print("invalid number")

        ans=None

    if ans is not None:

       print(f"the answer is: {ans}") 

except ValueErrors:


    print("INVALID INPUT!,please enter valid numbers:")