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
