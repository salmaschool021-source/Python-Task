import random
import math
print("Choose 1 For Password Generator")
print("Choose 2 for Password strenght checker")
choice=input("Enter your choice: ")
alC="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
als="abcdefghijklmnopqrstuvwxyz"
nms="0123456789"
spc="!@#$%&*?_"
if (choice=="1"):
    rntr1="y"
    while(rntr1 != "n"):
       l=int(input("Enter password length: "))
       while(l<8):
         l=int(input("Enter password length: "))
       u1=random.randint(1,l-3)
       t1=l-u1
       u2=random.randint(1,t1-2)
       t2=t1-u2
       u3=random.randint(1,t2-1)
       u4=l-u3-u1-u2
       p1=random.choices(alC,k=u1)
       p2=random.choices(als,k=u2)
       p3=random.choices(nms,k=u3)
       p4=random.choices(spc,k=u4)
       pss=p1+p2+p3+p4
       random.shuffle(pss)
       password=""
       for i in pss:
         password=password+str(i)
       print(password) 
       rntr1=input("Generate another Password ? (y/n) ")
elif(choice=="2"):
  m=0
  rntr2="y"
  while(rntr2 != "n"):
        tpass=input("Enter your password: ")
        e=[]
        r=0
        if len(tpass)>=8:
           e.append("Increase the length to at least 8 characters")
        for i in tpass:
           if i in alC:
              e.append("Add uppercase letter")
           elif i in als:
               e.append("Add lowercase letters")    
           elif i in nms:
               e.append("Add Numbers")           
           elif str(i) in spc:
              e.append("Add special characters")
        rc=[]
        for i in e:
           if i not in rc:
              rc.append(i)
        r=len(rc)
        if(r==5):
           print("Password Strength: Very strong")
        elif(r==4):
            print("Password Strength: strong")
        elif(r==3):
          print("Password Strength: Medium")
        else:
           print("Password Strength: weak")
        if(m):
           for i in rc:
              print(i)
        m=m+1
        rntr2=input("Enter your password: (y/n) ")
