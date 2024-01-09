from collections import Counter
t = int(input())
for _ in range(t):
    s = input()
    
    s4 = "1"
    s5 = "34567928"
    others = "0123456789"
    if len(s) > 14:
        print("NO")
        pass
        
    elif len(s) == 14 and s[0] == '+' and int(s[1]) == 8 and int(s[2]) == 8 and int(s[3]) == 0 and s[4] in s4 and s[5] in s5 and s[6] in others and s[7] in others and s[8] in others and s[9] in others and s[10] in others and s[11] in others and s[12] in others and s[13] in others:
        print("YES")
    else:
        print("NO")