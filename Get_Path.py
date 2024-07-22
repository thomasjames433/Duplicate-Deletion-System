def PATH(string):
    i=len(string)-1
    while string[i]!="/":
        i-=1
    m=string[0:i+1]
    return m

# print(PATH(input()))

