t = int(input())
for i in range(1,t+1):
    n = int(input())
    s = str(input())
    f1=""
    for j in range(len(s)):
        if s[j] == "E":
            f1 += "S"
        else:
            f1 += "E"
    print("Case #{0}: {1} ".format(i,f1))