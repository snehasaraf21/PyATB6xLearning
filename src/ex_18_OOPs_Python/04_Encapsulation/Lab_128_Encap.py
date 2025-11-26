class VWOlogin():
    def __init__(self,email_args,password_args):
        self.email = email_args
        self.password = password_args

    def login_confirmation(self):
        if self.email == "snehasaraf21@gmail.com" and self.password == "pass123":
            print("Login Successful")
        else:
            print("Login Failed")

email = input("Enter Email Address : ")
password = input("Enter Password : ")

vwo_login_obj = VWOlogin(email,password)
vwo_login_obj.login_confirmation()