# function that returns the maximum value from a dictionary
# {"a": 10, "b": 20, "c": 30}


def min_value_dict(dictionary):
#def max_value_dict(dictionary):
    #return max(dictionary.values())
     return min(dictionary.values())

def min_key_dict(dictionary):
#def max_key_dict(dictionary):
    #return max(dictionary.keys())
     return min(dictionary.keys())

#print(max_value_dict({"a": 10, "b": 20, "c": 30}))
print(min_value_dict({"a": 10, "b": 20, "c": 30}))
print(min_key_dict({"a": 10, "b": 20, "c": 30}))