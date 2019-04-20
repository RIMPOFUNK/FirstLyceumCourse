n = int(input())

way = 0
h_minmax = 0

for i in range(1, n + 1):
    m = int(input()) 
    height = -1
    
    for j in range(m):
        inp_height = int(input())
        if height < 0:
            height = inp_height
        else:
            if inp_height < height:
                height = inp_height
    if height > h_minmax:
        h_minmax = height
        way = i
print(way, h_minmax)
   