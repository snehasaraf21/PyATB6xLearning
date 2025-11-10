test_result = [ "PASS","FAIL","SKIP","PASS","FAIL","SKIP","PASS","FAIL","SKIP","PASS"]

def test_only_pass(x):
    return x == "PASS"

result_r = list(filter(test_only_pass , test_result))
print(result_r)