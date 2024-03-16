#create a cls ticket which will be the abstract cls inside that create a fun bookticket which will be the abstract method as ntg in its.
#create a cls make my trip  which will use the bookticket fun from ticket to take details such as  name phno emailid jounarydate and displays some msg saying thank you for booking make my trip
#create a cls IRCTC which  uses the bookticket cls and takes the same details aas make my trip but in the end it will give an option to user to select one way or round trip .if user option round trip  it again ask the user to enter return date aswelland print msg thank you choose irctc
#else
#create a cls indigo which takes all the details as irctc and just ask which modwe transport u want going it and print thanks choose
from abc import ABC , abstractmethod
class Ticket(ABC):
    @abstractmethod
    def Bookticket(self):
        pass
class Makemytrip(Ticket):
    def Bookticket(self):
        name=input("enter the name:")
        
        phno=int(input("enter the number: "))
        
        emailid=input("enter the email :")
        
        jounarydate= input("enter the date: ")
        
        print("thank you for booking from make my trip ")
class IRCTC(Ticket):
    def Bookticket(self):
    
        name=input("enter the name:")
        
        phno=int(input("enter the number: "))
    
        emailid=input("enter the email :")
        
        jounarydate= input("enter the date: ")
        print("enter one way or round trip")
        userchoice=input("enter the choice:")
        
        if(userchoice == "round trip" ):
            return_date=input("enter return date")
            print("thank you for choosing IRCTC")
        else:
            print("thank you for choosing IRCTC")
class indigo(Ticket):
    def Bookticket(self):
        name=input("enter the name:")
        
        phno=int(input("enter the number: "))
    
        emailid=input("enter the email :")
        
        jounarydate= input("enter the date: ")
        mode=input("enter the mode of transport")
        print("thank you choosing indigo")
obj=indigo()
obj1=IRCTC()
obj2=Makemytrip()
obj.Bookticket()
obj1.Bookticket()
obj2.Bookticket()
            
            
    
    
