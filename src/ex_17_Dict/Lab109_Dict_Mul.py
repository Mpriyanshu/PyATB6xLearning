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
student_infor3 = {
    "name": "Shiv",
    #"age": 100,
    "age": 102,
    "address": {
        "home_address": "himalya",
        "office_address": "heart"
    }
}

student_list = [student_infor1, student_infor2, student_infor3]
print(student_list)
print(student_list[2]["address"]["office_address"])