student_infor1 = {
    "name": "Priyanshu",
    #"age": 22,
    "age": 24,
    "address": {
        "home_address": "ND",
        "office_address": "KA"
    }
}
student_infor2 = {
    "name": "aman",
    #"age": 54,
    "age": 57,
    "address": {
        "home_address": "GOA",
        "office_address": "AK"
    }
}


student_list = [student_infor1,student_infor2]
print(student_list)
print(student_list[0])
print(student_list[0]["name"])
print(student_list[0]["address"]["office_address"])