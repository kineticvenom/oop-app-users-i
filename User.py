# your User class goes here
class Users: 
    def __init__(self, first_name=None, last_name=None, email_address=None, drivers_license_number=None, social_security_number=None,) :
        
        self.name = first_name + " " + last_name
        self.email = email_address
        self.license = drivers_license_number
        self.social = social_security_number
    
    def __str__(self):
        return f"Name:{self.name} Email:{self.email} DL:{self.license} Social:{self.social}"

linda = Users("linda","armstrong","linda@gmail","DL234Fz","574-25-5463" )
bob = Users()
print(linda)