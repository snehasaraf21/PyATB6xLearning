"""In automation, you often compare expected and actual outputs.
Write code to check if a test case passed or failed.

expected_title = "Dashboard"
actual_title = "Dashboard "

✅ Test Passed – Title matches


True - why >  Strip and convert them into the lowercase = both of them are equal.
"""
expected_title = str(input(("Enter your expected title: ")))
actual_title = str(input(("Enter your actual title: ")))
if expected_title.lower().strip() == actual_title.lower().strip():
    print("Test Passed - title matches")
else:
    print("Test failed - title does not match")
