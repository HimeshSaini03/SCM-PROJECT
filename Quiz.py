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
