s = input()
n = len(s)
ways = [0]*n

flag = 0
for i in range(n):
    if i == 0:
        if s[i] == '0':
            print(0)
            flag = 1
            break
        else:
            ways[i] = 1
    else:
        if ((s[i-1] == '1' and s[i] != '0') or (s[i-1] == '2' and s[i] <= '6' and s[i] > '0')) and (i == n-1 or s[i+1] != '0'):
            if i == 1:
                ways[i] = 1+ways[i-1]
            else:
                ways[i] = ways[i-2]+ways[i-1]
        elif s[i] == '0' and (s[i-1] == '0' or s[i-1] > '2'):
            print(0)
            flag = 1
            break
        else:
            ways[i] = ways[i-1]

if flag == 0:
    print(ways[n-1])
