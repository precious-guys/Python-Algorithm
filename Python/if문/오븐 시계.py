Hour, Minute = map(int, input().split)

Add = int(input())

if Minute+Add>59 :
    if Hour>0 :
        Hour += Add+Minute//60
        Add+Minute -= Add 

    
