def validate_status_code(response_code):
    if response_code == 200:
        return print("Response code successfull")
    else:
        return print("Response code unsuccessfull")

validate_status_code(200)
validate_status_code(404)

