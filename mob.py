def mobilenumber():
    mobile=input("enter a number" )
    if mobile[0]=="7" or "8" or "9":
        if len(mobile)==10:
            print (mobile + "is valid")
        else:
            print("not valid")
    else:
        print("not valid")
mobilenumber()
