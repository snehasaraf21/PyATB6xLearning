"""You want to check whether a web page loads within 3 seconds (performance test condition).

load_time = 4.2
⚠️ Page load too slow: 4.2 seconds
"""
#i/p-->load time in flaot
#or #o/p--> pass or fail as per condition
#rough logic
#if response_time <= 3 then pass if not fail

load_time = float(input("Enter the load time: \n"))
if load_time <= 3:
    print("performance test passed")
else:
    print("performance test failed")

