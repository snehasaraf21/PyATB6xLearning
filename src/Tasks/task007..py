#Q - You receive an API response code from your test script.
#Write an if-else block to check whether the response is successful (status code 200) or not.
#I/P response = 404 , O/P ❌ Failed API Request
#I/P response = 200 , O/P ✅ Passed API Request
#logic building formula
#I/P response = 404 , O/P ❌ Failed API Request
#I/P response = 200 , O/P ✅ Passed API Request
#rough logic
#if response code = 200  then passed api requiest else fail

Api_Responce = int(input("enter your response code from your test script:\n" ))
if Api_Responce == 200:
    print("✅ Passed API Request" , 200)
elif Api_Responce == 404:
    print("❌ Failed API Request", 404)
else:
    print("Please enter valid test response")


