s1= ['A','B','C','B','D','A','B']
s2 = ['B','D','C','A','B','A']
count = 0

def lcs(s1,s2) :
    global count
    count += 1
    if (not s1 or not s2) :
        return ""
    if s1[-1] == s2[-1] :
        return lcs(s1[:-1],s2[:-1]) + s1[-1]
    lcs1 = lcs(s1,s2[:-1])
    lcs2 = lcs(s1[:-1],s2)
    return lcs1 if len(lcs1) > len(lcs2) else lcs2

print(lcs(s1,s2), "count:", count) #BCBA count: 152
count = 0
print(lcs(['A','B','C'],['D','E','F','G']), "count:", count) #count: 69

#if both strings the size of n are identical, recursion branching is avoided.
#therefore, the function will be called n times and the lcs will be identical to both strings.