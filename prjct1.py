fullname=input("enter full name")
email=input("enter email id")
mobileno=input("enter mobile number")
age=int(input("enter age"))
i=1
if fullname.count(" ")>=1 and fullname[0]!=" " and fullname[len(fullname)-1]!=" ":
    if(email.count("@")>=1 and email.count(".")>=1 and email[0]!="@"):
        if(len(mobileno)==10 and mobileno.isdigit() and mobileno[0]!="0"):
            if(18<age<=60):
                print("User Profile is VALID")
            else:
               print("User Profile is INVALID")
        else:
            print("User Profile is INVALID")
    else:
        print("User Profile is INVALID")
else:
    print("User Profile is INVALID")

