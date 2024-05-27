# solution1
n1,n2 = len(word1), len(word2)
n12 = ""
if n1 == n2:
    for i in range(n1):
        n12+= word1[i]
        n12+=word2[i]

elif n1 > n2:
    for i in range(n2):
        n12+=word1[i]
        n12+=word2[i]
    
    for i in range(n2,n1):
        n12+=word1[i]

else:
    for i in range(n1):
        n12+=word1[i]
        n12+=word2[i]

    for i in range(n1,n2):
        n12+=word2[i]

return(n12)

# solution2

s = ""
n = min(len(word1),len(word2))
for i in range(n):
    s = s + word1[i] + word2[i]
if len(word1) > len(word2):
    s = s + word1[n:]
else:
    s = s + word2[n:]
return s 
