

A, B = map(int, input().split())
cnt = 1

while A != B :
    cnt += 1
    temp = B
    
    if B % 10 == 1 :
        B //= 10
    
    elif B % 2 == 0 :
        B //= 2
        
    if temp == B :
        cnt = -1
        break

print( cnt )
        
        
    
        