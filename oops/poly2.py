class Mom:
    def dance(self):
        print("Mom is dancing")
    def cook(self):
        print("Mom is cooking")    

#Child class
class Daughter(Mom):
        pass
   
d = Daughter()
d.dance()
d.cook() 