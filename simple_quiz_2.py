import time
ans_a = ["a" , "A"]
ans_b = ["b" , "B"]
true = ["T", "t", "True"]
false = ["F", "f", "False"]
score = 0
Student = input("Please enter your name \n")
print(f"welcome to the quiz {Student} just rember this is scoring quiz the final result gonna affect you" )
time.sleep(2)
#Question1
print("What is the capital of Chile? A.Santiago , B.Mario")
choose = input("Your answer: ")
if choose in ans_a:
    score+=1
else:
    score+=0
#Question2
print("What is the highest mountain in Britain? A.Everest , B.Ben Nevis")
choose = input("Your answer: ")
if choose in ans_b:
    score+=1
else:
    score+=0   
#Question3     
print("Paris is the captial of France True or False")
choose = input("Your answer: ")
if choose in true:
    score+=1
else:
    score+=0 
#Question4     
print("What colour is found on 75% of the world’s flags? A.Green B.Red")
choose = input("Your answer: ")
if choose in ans_b:
    score+=1
else:
    score+=0 
#Question5     
print("What is Queen Elizabeth II's surname? A.Windsor B.Catherine Parr")
choose = input("Your answer: ")
if choose in ans_a:
    score+=1
else:
    score+=0 
#Question6   
print("Northern Ireland isn't part of Great Britian. True or False" )
choose = input("Your answer: ")
if choose in false:
    score+=1
else:
    score+=0     
#Question7
print("Who is the voice of Shrek A.Mike Myers B.Elon Musk")
choose = input("Your answer: ")
if choose in ans_a:
    score+=1
else:
    score+=0     
#Question8
print("What is the tallest building in the world and in which city is it located?  A.statue of liberty,New York B.Burj Khalifa, Dubai")
choose = input("Your answer: ")
if choose in ans_b:
    score+=1
else:
    score+=0     
#Question9
print("Paris is the captial of France")#still nedds question
choose = input("Your answer: ")
if choose in true:
    score+=1
else:
    score+=0     
#Question10
print("Iran use to be part of the Perisan Empire. True or False")
choose = input("Your answer: ")
if choose in true:
    score+=1
else:
    score+=0     
#Question11
print("Turkmenistan isn't a real country. True or False")
choose = input("Your answer: ")
if choose in false:
    score+=1
else:
    score+=0     
#Question12               
print("Turkmenistan isn't a real country. True or False")#still needs qustion
choose = input("Your answer: ")
if choose in false:
    score+=1
else:
    score+=0     
#Question13
print("In what year was the first Playstation console released? A.1996 B.1994")
choose = input("Your answer: ")
if choose in ans_b:
    score+=1
else:
    score+=0     
#Question14
print("Hamlet was the Prince of which country? A.France  or  B.Denmark")
choose = input("Your answer: ")
if choose in ans_b:
    score+=1
else:
    score+=0     
#Question15
print("Andorra is between France and Spain. True or False")
choose = input("Your answer: ")
if choose in true:
    score+=1
else:
    score+=0     
#Question16
print("What is Japanese sake made from? A.Rice  or  B.Beans")
choose = input("Your answer: ")
if choose in ans_a:
    score+=1
else:
    score+=0     
#Question17
print("Vanilla comes from what flowers A.Orchids B.Hyacinth")
choose = input("Your answer: ")
if choose in ans_a:
    score+=1
else:
    score+=0     
#Question18
print("How many fingers do Simpsons characters have? A.12 or B.4")
choose = input("Your answer: ")
if choose in ans_b:
    score+=1
else:
    score+=0     
#Question19
print("Who is Donald Trump's vice president? A.Milner Wlaels or B.Mike Pence")
choose = input("Your answer: ")
if choose in ans_b:
    score+=1
else:
    score+=0 
#Question20
print("Who is the richest man in the world? A.Elon Musk or B.Jeff Bezos")
choose = input("Your answer: ")
if choose in ans_a:
    score+=1
else:
    score+=0 
print (f"\nYou're finished {Student}. You got ---> {score} out of 20 correct.")          

