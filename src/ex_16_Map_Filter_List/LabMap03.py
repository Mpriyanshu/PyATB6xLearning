response_time_ms = [1200 , 1500, 1800]

def mil_sec(x):
    return x/1000

#response_time_ms = list(map(mil_sec, response_time_ms))
response_time_ms = list(map(lambda x : x/1000, response_time_ms))
print(response_time_ms)