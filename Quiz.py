name=input("Enter Your Name:")
R=int(input("Enter Your roll Number:2210990"))
print('''Let's start 
      Select One : 1=Python Quiz Game 2=Calculator 3=Invitaion Card Generator''')
x=int(input("You Selected->"))
points=0
list=[]
if x==1:
    print('''Python Quiz
    ->Total of 10 Question will be there
    ->Type only option Letter
    ->Each Question Hold 5 Points
    ->All The best
     
      ''')
elif x==2:
    print('''Your CALCULATOR is ready
    For ADDITION TYPE 1
    FOR SUBTRACTION TYPE 2
    FOR MULTIPLICATION TYPE 3
    FOR DIVISION TYPE 4
    FOR MUDULUS TYPE 5
    FOR FACTORIAL TYPE 6
    FOR AGE CALCULATOR TYPE 7
    
    ''')
elif x==3:
    print('''Welcome to invitation card generator
          ->Write Your Details To Generate the card''')
    print(''' 
          ''')
else :
    print('''Topic Not selected
            Please Start Again''')
if x==1:
    print('''Q1-Who developed Python Programming Language?:
    a) Wick van Rossum
    b) Rasmus Lerdorf
    c) Guido van Rossum
    d) Niene Stom
       ''')
    A1=input("Your Answer:")
    print("Correct Answer:c) Guido van Rossum")
    if A1 == "c":
        list.append(A1)
        print("Well Done! You are awarded 5 points")
        points=points+5
        print("Total Points:",points)
    else:
        list.append(A1)
        print("Incorrect answer")
        print("Total Points:",points)
    print(" ")
    
    print('''Q2-Which type of Programming does Python support?
    a) object-oriented programming
    b) structured programming
    c) functional programming
    d) all of the mentioned
      ''')
    A2=input("Your Answer:")
    print("Correct Answer:d) all of the mentioned")
    if A2 == "d":
        list.append(A2)
        print("Well Done! You are awarded 5 points")
        points=points+5
        print("Total Points:",points)
    else:
        list.append(A2)
        print("Incorrect answer")
        print("Total Points:",points)
    print(" ")
    
    print('''Q3-Is Python case sensitive when dealing with identifiers?
    a) no
    b) yes
    c) machine dependent
    d) none of the mentioned
     ''')
    A3=input("Your Answer:")
    print("Correct Answer:a) no")
    if A3 == "a":
        list.append(A3)
        print("Well Done! You are awarded 5 points")
        points=points+5
        print("Total Points:",points)
    else:
        list.append(A3)
        print("Incorrect answer")
        print("Total Points:",points)
    print(" ")
    print('''Q4-:Which of the following is the correct extension of the Python file?
    a) .python
    b) .pl
    c) .py
    d) .p
     ''')
    A4=input("Your Answer:")
    print("Correct Answer:c) .py")
    if A4 == "c":
        list.append(A4)
        print("Well Done! You are awarded 5 points")
        points=points+5
        print("Total Points:",points)
    else:
        list.append(A4)
        print("Incorrect answer")
        print("Total Points:",points)
    print(" ")
        
    print('''Q5-Which of the following is used to define a block of code in Python language?
    a) Indentation
    b) Key
    c) Brackets
    d) All of the mentioned
     ''')
    A5=input("Your Answer:")
    print("Correct Answer:a) Indentation")
    if A5 == "a":
        list.append(A5)
        print("Well Done! You are awarded 5 points")
        points=points+5
        print("Total Points:",points)
    else:
        list.append(A5)
        print("Incorrect answer")
        print("Total Points:",points)
    print(" ")
        
    print('''Q6-Which keyword is used for function in Python language?
    a) Function
    b) Def
    c) Fun
    d) Define:''')
    A6=input("Your Answer:")
    print("Correct Answer:b) Def")
    if A6 == "b":
        list.append(A6)
        print("Well Done! You are awarded 5 points")
        points=points+5
        print("Total Points:",points)
    else:
        list.append(A6)
        print("Incorrect answer")
        print("Total Points:",points)
    print(" ")
        
    print('''Q7-Which of the following functions is a built-in function in python?
    a) factorial()
    b) print()
    c) seed()
    d) sqrt():''')
    A7=input("Your Answer:")
    print("Correct Answer:b) print()")
    if A7 == "b":
        list.append(A7)
        print("Well Done! You are awarded 5 points")
        points=points+5
        print("Total Points:",points)
    else:
        list.append(A7)
        print("Incorrect answer")
        print("Total Points:",points)
    print(" ")
        
    print('''Q8-Which of the following is the use of id() function in python?
    a) Every object doesn’t have a unique id
    b) Id returns the identity of the object
    c) All of the mentioned
    d) None of the mentioned:
    ''')
    A8=input("Your Answer:")
    print("Correct Answer:b) Id returns the identity of the object")
    if A8 == "b":
        list.append(A8)
        print("Well Done! You are awarded 5 points")
        points=points+5
        print("Total Points:",points)
    else:
        list.append(A8)
        print("Incorrect answer")
        print("Total Points:",points)
    print(" ")
        
        
    print('''Q9- What will be the output of the following Python function?
                            len(["hello",2, 4, 6])
    a) Error
    b) 6
    c) 4
    d) 3
    ''')
    A9=input("Your Answer:")
    print("Correct Answer:c) 4")
    if A9 == "c":
        list.append(A9)
        print("Well Done! You are awarded 5 points")
        points=points+5
        print("Total Points:",points)
    else:
        list.append(A9)
        print("Incorrect answer")
        print("Total Points:",points)
    print(" ")
        
    print('''Q10- What will be the output of the following Python code snippet?
                          for i in [1, 2, 3, 4][::-1]:
                          print (i)
    a) 4 3 2 1
    b) error
    c) 1 2 3 4
    d) none of the mentioned
     ''')
    A10=input("Your Answer:")
    print("Correct Answer:a) 4 3 2 1")
    if A10 == "a":
        list.append(A10)
        print("Well Done! You are awarded 5 points")
        points=points+5
        print("Total Points:",points)
    else:
        list.append(A10)
        print("Incorrect answer")
    print('''
          ''')
    print("Name:",name)
    print("Roll. No.:221099",R)
    print("Total Points:",points)
    print(" ")
    print("Your Selected Answers:",list)
    list2=['c','d','a','c','a','b','b','b','c','a']
    print("Correct Answer are:",list2)
    print(" ")
    
    if points==50:
        print("WOW!!You Are Awesome...You have build up concept of python very strongly ")
    elif 40<=points<50:
        print("Nice!!Good Job .. But more Clearity in Concepts needed")
    elif 30<=points<40:
        print("Need more Focus on Concepts")
    elif 10<=points<30:
        print("Poor Concepts!!")
    else:
        print("Let's Try Again") 
  #CALCULATOR
if x==2:
    OP=int(input("Select the Operation you want to do: "))
    if OP==1:
        g=int(input("Enter Total NUmber Of Quantites: "))
        add=0
        for i in range (g):
            num1=int(input("Enter Number for Addition: "))
            add=add+num1
        print(add)
    if OP==2:
        num1=int(input("Enter Number for Subtraction: "))
        num2=int(input("Enter Number for Subtraction: "))
        sub=num1-num2
        print(sub)
        
    if OP==3:
        g=int(input("Enter Total Number Of Quantites: "))
        mul=1
        for i in range (g):
            num1=int(input("Enter Number for Multiplication: "))
            mul=mul*num1
        print(mul)
    if OP==4:
        num1=int(input("Enter First Number for Division:"))
        num2=int(input("Enter Second Number Division:"))
        div=num1/num2
        print(div)
    if OP==5:
        num1=int(input("Enter First Number (Dividend):"))
        num2=int(input("Enter Second Number(Divisor):"))
        mod=num1%num2
        print("Remainder:",mod)
    if OP==6:
        def factorial(x):
            fact=1
            for i in range(1,x+1):
                fact=fact*i
            print("Factorial =",fact)
                
        x=int(input("Enter a Number To find Factorial: "))
        factorial(x)
        
    if OP==7:
        Y=int(input("Enter Your Birth Year: "))
        T=int(input("Enter Current Year: "))
        diff=T-Y
        print("Your AGE is: ",diff)

            
  if x==3:
    print("Your details:->")
    
    A=input("Enter Reciver Name: ")
    B=input("Enter The reciver's House Address: ")
    C=input("Enter The reciver's City,state: ")
    D=input("Enter Your Name: ")
    E=input("Enter Your House Address: ")
    F=input("Enter Your City,State: ")
    G=input("Enter The occasion: ")
    x=input("Enter Occasion date (dd/mm/yyyy): ")
    H=input("Enter The Venue Of occasion: ")
    print(''' 

             ''')

    print('To-')
    print(A)
    print(B)
    print(C)
    print('''
             ''')
    print('From-')
    print(D)
    print('Address',E,)
    print(F)
    print(''' ''')

    print("Invitation for ",G,)
    print(''' ''')
    print("Dear",A,)
    print('''  ''')
    print( "We are Glad to invite you to" ,G, "on the date",x,)
    print('''
    I have arranged a small party on that day
    I would earnestly request you to join''')
    print("    There will be lots of fun in the party")
    print("    We look forward to your presence along with your family at",H,)
    print( '''  Rest when we meet :)
                               ''')

    print("Your Affectionately")
    print(D)
