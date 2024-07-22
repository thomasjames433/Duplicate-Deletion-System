
def name(string):
    i=len(string)-1
    while string[i]!="/":
        i-=1
    m=string[i+1:len(string)]
    return m

# print(name(input()))

