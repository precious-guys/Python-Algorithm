a = int(input())

for i in range(a) :
    for j in range(i+1) :
        print('*', end="") # end="" : 줄바꿈 없애는 법
    print()