name = input ("ENter your name: ")
roll = int (input ("ENter your symbol number: "))
batch = input ("ENter your batch: ")
sub1 = int (input("Enter your score for first subject: "))
sub2 = int (input("Enter your score for second subject: "))
sub3 = int (input("Enter your score for third subject: "))
score = (sub1+sub2+sub3)/3

print ("The name of the student is", name)
print ("The symbol number of", name, "is", roll)
print ("The batch of", name, "is", batch)
print ("The percentage of", name, "is", score)

if sub1 < 40 or sub2 < 40 or sub3 < 40:
     print ("Fail")
elif score >= 70:
    print ("First class")
elif score >= 60 and score <70:
    print ("Upper Second class")
elif score >= 50 and score < 60:
    print ("Lower second class")
elif score >= 40 and score < 50:
    print ("Third class")
# else:
#     print("fail") 



