def simple_interest(p,t,senior):
    rate=12 if senior else 10
    return(p*rate*t)/100
p=float(input("Principal:"))
t=float(input("Time(years):"))
senior=input("Senior citizen(yes/no):").lower()=="yes"
print("Simple Interest=",simple_interest(p,t,senior))
