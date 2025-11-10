response_time =[1200,1600,2300]

def response_time_ms(x):
    return x/1000


reponse_time_r = list(map(response_time_ms,response_time))
print(reponse_time_r)