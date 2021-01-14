a='abcdefghijklmnopqrstuvwxyz'
password=input("enter a password ")
new_password=""
for i in password:
    x=ord(i)//2
    y=ord(i)%2
    new_password=new_password+str(x)+str(y)+"."
print("your encrypted password is: ", new_password)