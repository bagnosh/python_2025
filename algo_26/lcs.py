s1 = "AGGTA"
s2 = "GXTXAY"

def lcs(s1,s2):
    if s1 == "" or s2 == "":
        return ""
    if s1[-1]==s2[-1]:
        return lcs(s1[:-1],s2[:-1])+s1[-1]
    lcs1 = lcs(s1,s2[:-1])
    lcs2 = lcs(s1[:-1],s2)
    if len(lcs1) > len(lcs2):
        return lcs1
    else:
        return lcs2
    
print(lcs(s1,s2))