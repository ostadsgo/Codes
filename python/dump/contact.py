class Contact:
    first_name = ""
    last_name = ""
    phone_number = ""
    email = ""

    def __init__(self, first, phone):
        self.first_name = first
        self.phone_number = phone

    def display(self):
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)
        print("Phone Number:", self.phone_number)
        print("Email:", self.email)

##c1 = Contact()
##c1.first_name = "Peter"
##c1.last_name = "Parker"
##c1.phone_number = "+1 (445) 340 1191"
##c1.email = "peterparker@spiderman.com"
##
##c1.display()
##
##c2 = Contact()
##c2.first_name = "Tony"
##c2.last_name = "Stark"
##c2.phone_number = "+1 (333) 450 3319"
##c2.email = "tonystark@ironman.com"
##
##
##c3 = Contact()
##c3.first_name = "Bruce"
##c3.last_name = "Banner"
##c3.phone_number = "+1 (444) 634 4561"
##c3.email = "brucebanner@hulk.com"

c4 = Contact("Steve", "+1 (340) 870 3419")
c4.display()



