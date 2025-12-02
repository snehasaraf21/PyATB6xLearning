def VwoLogin(user):
    if user != "admin":
        raise Exception("Unauthorised admin")
    return "Welcome Admin"

print(VwoLogin("admin"))
print(VwoLogin("sneha"))#will print Exception: Unauthorised admin
