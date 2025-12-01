#t = open('tesdata.txt', 'w')
#t = open('tesdata.txt', 'r+')
#t = open('tesdata.txt', 'r')
#t = open('tesdata.txt', 'w+')
#t = open('tesdata.txt', 'b')
#t.close()
# Automatically close
with open('testdata.txt', 'r') as f:
    data = f.read()

print(data)