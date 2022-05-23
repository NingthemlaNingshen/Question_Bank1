
def epf_amount():
    epf_principle=int(input("enter your number: "))
    year=int(input("enter the year:"))
    user=input("Did the employee retired or Quits?? ")
    if user=="retired":
        print("The employee retired")
        print("The total epf_amount is: ",1.2*epf_principle*year)
    else:
        print("The employee Quits")
        if year<5:
            print("Cannot withdraw any money")
        elif year>5:
            if year<10:
                print("epf_amount: ",0.9*epf_principle*year)
            elif year<20:
                print("epf_amount: ",1*epf_principle*year)
            else:
                print("The total epf_amount is: ",1.2*epf_principle*year)
epf_amount()




