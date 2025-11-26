from dotenv import load_dotenv
import os


class VWOlogin():
    def __init__(self,email_args,password_args):
        self.email = email_args
        self.password = password_args

    def login_confirmation(self):
        load_dotenv()
        print(os.getenv("USERNAME"))
        print(os.getenv("PASSWORD"))
        if self.email == os.getenv("USERNAME") and self.password == os.getenv("PASSWORD"):
            print("Login Successful")
        else:
            print("Login Failed")

email = input("Enter Email Address : ")
password = input("Enter Password : ")

vwo_login_obj = VWOlogin(email,password)
vwo_login_obj.login_confirmation()