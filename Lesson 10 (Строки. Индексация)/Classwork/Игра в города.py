word1 = input()
word2 = input()

while word2[0] == word1[-1]:
    word1 = word2
    word2 = input()
print(word2)