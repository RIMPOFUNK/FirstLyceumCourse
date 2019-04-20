words = input().split()
counts = {}

for word in words:
    if word not in counts:
        counts[word] = 1
    else:
        counts[word] += 1
    print(counts[word], end=' ')
    
        
