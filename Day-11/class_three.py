class Customer:
    def __init__(self,name,membership_type):
        self.name=name
        self.membership_type=membership_type

    def update_membership(self,new_membership):
        self.membership_type=new_membership

cus1=Customer("Wasif","Gold")
print("Congrats "+cus1.name+",you have successfully purchased "+cus1.membership_type+" membership")
cus1.update_membership("Platinum")
print("Congrats "+cus1.name+",you have successfully transfered to "+cus1.membership_type+" membership")