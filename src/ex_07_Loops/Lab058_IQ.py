for i in range (101): # 0 to 100
   if i % 2 == 0:
        print(i)

# |i | Condition | 0/P
# | 0 | 0%2 == 0 - True |0/P -> 0
# /1/ 1%2 == 0 - False | 0/P -> Nothing will be printed
# /2/ 2%2 == 0 - True | 0/P -> 2
# /3/ 3%2 == 0 - False | 00/P -> Nothing will be printed