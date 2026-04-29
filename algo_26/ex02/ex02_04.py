def lcs_iterative(s1, s2):
    m, n = len(s1), len(s2)
    # table[(i, j)] = (serial, lcs_string, type)
    table = {}
    counter = 0

    # Initialize the base cases (empty string boundaries)
    for i in range(m + 1):
        counter += 1
        table[(i, 0)] = (counter, "", "Base Case")
    for j in range(1, n + 1):
        counter += 1
        table[(0, j)] = (counter, "", "Base Case")

    # Fill the rest of the table row-by-row
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            counter += 1
            
            if s1[i-1] == s2[j-1]:
                # Diagonal move: Add current char to the LCS of previous prefixes
                prev_lcs = table[(i-1, j-1)][1]
                table[(i, j)] = (counter, prev_lcs + s1[i-1], f"Match ({s1[i-1]})")
            else:
                # Compare Top vs Left
                left_lcs = table[(i, j-1)][1]
                top_lcs = table[(i-1, j)][1]
                
                if len(left_lcs) >= len(top_lcs):
                    table[(i, j)] = (counter, left_lcs, "Inherit Left")
                else:
                    table[(i, j)] = (counter, top_lcs, "Inherit Top")
                    
    return table