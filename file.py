#WAP to enter your name, age, gender, address, contact and email address in the file "info.txt" and display only name and email address.

name = input("ENter your name")
age = input("ENter your age")
gender = input("ENter your gender")
address = input("ENter your address")
contact = input("ENter your contact")
email = input("ENter your email")

f=open('info.txt', 'w')
content = f.write()
