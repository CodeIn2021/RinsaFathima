n = int(input())
seq = [0, 1]
i = 1
x = 1
if n == 1:
    print(seq)
else:
    while i < n:
        x *= 2
        for num in reversed(seq):
            seq.append(x+num)
        i += 1
    print(seq)
