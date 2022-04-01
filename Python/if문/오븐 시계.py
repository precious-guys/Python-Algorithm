Hour, Minute = map(int, input().split())

Add = int(input())

temp = int

Minute += Add

if Minute>59 :

    Hour += (Minute)//60

    Minute -= (Minute//60)*60

    if Hour>23 :
        
        Hour -= 24

print(Hour, Minute)


    
