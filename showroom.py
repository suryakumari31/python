class showroom:
    def __init__(self):
        print('1.Tech Mahindra,2.Toyota,3.Mercedes')
        com=(input("enter the company name one of above display:"))
        if com== "Tech Mahindra" or "Toyota" or "Mercedes":
            self.com=com
        else:
            print("enter valid company car")
            
            
        
    def companyname(self):
    
        if (self.com=="Tech Mahindra" ):
            model=input(("enter the modelof 1.Thar or 2.XUV300:"))
            self.model=model 
                
        elif (self.com=="Toyota" ):
           model=input(("enter the model 1.Glanza or 2.Urban Cruiser:"))
           self.model=model 
        elif (self.com=="Mercedes"):
           model=input(("enter the model 1.GLE LWB or 2.E-Class:"))
           self.model=model
        else:
            print("enter valid input")
    def varient(self):
         var=input(("enter the specific of 1.petrol or 2.diesel "))
         self.var=var
    def display(self):
        if (self.com=="Tech Mahindra") and (self.model=="Thar" ):
            
            if (self.var=="diesel" ):
                exshowprice=400000
                tax=exshowprice*(25/100)
            else:
                 exshowprice=500000
                 tax=exshowprice*(25/100)
        elif self.com=="Tech Mahindra"  and self.model=="XUV300"  :
            if (self.var=="diesel" or 2):
                exshowprice=600000
                tax=exshowprice*(25/100)
            else:
                 exshowprice=700000
                 tax=exshowprice*(25/100)
        elif self.com=="Toyota" and self.model=="Glanza" :
            if (self.var=="diesel" or 2):
                exshowprice=750000
                tax=exshowprice*(25/100)
            else:
                 exshowprice=800000
                 tax=exshowprice*(25/100)
        elif self.com=="Toyota"  and self.model=="Urban Cruiser" :
            if self.var=="diesel":
                
                exshowprice=850000
                tax=exshowprice*(25/100)
            else:
                 exshowprice=900000
                 tax=exshowprice*(25/100)
        elif self.com=="Mercedes"  and self.model=="GLE LWB":
            if self.var=="diesel" :
                exshowprice=9500300
                tax=exshowprice*(25/100)
            else:
                 exshowprice=960000
                 tax=exshowprice*(25/100)
            
            
        elif self.com=="Mercedes"  and self.model=="E-Class":
            if self.var=="diesel":
                exshowprice=500000
                tax=exshowprice*(25/100)
            else:
                 exshowprice=400000
                 tax=exshowprice*(25/100)
        
        on_roadprice=exshowprice+(3*tax)
        print("onroadprice of car company",self.com,"of model",self.model,"and varient",on_roadprice)
show =showroom()
show.companyname()
show.varient()
show.display()
