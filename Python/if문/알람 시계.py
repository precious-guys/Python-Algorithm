Hour, Minute = map(int, input().split())

if Minute<45 :
    if Hour==0 :
        Hour = 23
        Minute += 60
        Minute -= 45
    elif Hour>0 :
        Hour -= 1
        Minute += 60
        Minute -= 45
else :
    Minute -= 45
print(Hour, Minute)