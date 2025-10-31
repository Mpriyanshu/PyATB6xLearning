for i in range(0, 10): # 0 to 9, times -> 10
    print(i)
    if(i == 5):
        break

# |i | Condition | 0/P
# |0 | 0 == 5 -> False | 0/P = 0
# |1 | 1 == 5 -> False | 0/P = 1
# |2 | 2 == 5 -> False | 0/P = 2
# |3 | 3 == 5 -> False | 0/P = 3
# |4 | 4 == 5 -> False | 0/P = 4
# |5 | 5 == 5 -> True | 0/P = Break out of For loop
