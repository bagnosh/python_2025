def lcs_with_tracking(s1, s2):
    memo = {}
    counter = 0
    table_data = {} 

    def helper(m, n):
        #במקרה וכבר קיים
        nonlocal counter
        if (m, n) in memo:
            return memo[(m, n)]
        
        # חישוב, שמירת פרטים
        if m == 0 or n == 0:
            res = ""
            comp_type = "Base Case"
        elif s1[m-1] == s2[n-1]:
            res = helper(m-1, n-1) + s1[m-1]
            comp_type = f"Match ({s1[m-1]})"
        else:
            res1 = helper(m, n-1)
            res2 = helper(m-1, n)
            if len(res1) >= len(res2):
                res = res1
                comp_type = "Inherit Left"
            else:
                res = res2
                comp_type = "Inherit Top"
        
        # מספר סידורי למעקב אחרי סדר המילוי
        counter += 1
        memo[(m, n)] = res
        table_data[(m, n)] = (counter, res, comp_type)
        return res

    helper(len(s1), len(s2))
    return table_data

def save_lcs_to_html(s1, s2, data, filename="lcs_table.html"):
    rows, cols = len(s1), len(s2)
    
    #פורמט הקובץ העתידי
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{ font-family: 'Segoe UI', Tahoma, sans-serif; background: #f0f2f5; padding: 40px; }}
            table {{ border-collapse: collapse; background: white; margin: auto; box-shadow: 0 10px 30px rgba(0,0,0,0.1); }}
            th, td {{ border: 1px solid #dee2e6; padding: 15px; text-align: center; min-width: 80px; }}
            th {{ background-color: #007bff; color: white; }}
            .header-char {{ font-weight: bold; background-color: #f8f9fa; color: #495057; }}
            .serial {{ color: #adb5bd; font-size: 0.75em; display: block; }}
            .lcs-val {{ color: #28a745; font-weight: bold; font-size: 1.1em; display: block; margin: 5px 0; }}
            .type {{ font-size: 0.7em; color: #6c757d; text-transform: uppercase; letter-spacing: 0.5px; }}
        </style>
    </head>
    <body>
        <h2 style="text-align:center;">LCS Memoization Analysis</h2>
        <table>
            <tr><th></th><th>&Oslash;</th>"""
    
    #פורמט הטבלה
    for char in s2:
        html_content += f"<th>{char}</th>"
    html_content += "</tr>"

    #מילוי
    for i in range(rows + 1):
        char = s1[i-1] if i > 0 else "&Oslash;"
        html_content += f"<tr><td class='header-char'>{char}</td>"
        for j in range(cols + 1):
            cell = data.get((i, j), ("-", "", "Unvisited"))
            html_content += f"""
                <td>
                    <span class="serial">#{cell[0]}</span>
                    <span class="lcs-val">{cell[1] if cell[1] else "&empty;"}</span>
                    <span class="type">{cell[2]}</span>
                </td>"""
        html_content += "</tr>"
        
    html_content += "</table></body></html>"
    
    # כתיבת ושמירת הטבלה לקובץ
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"File saved successfully as {filename}")

# דוגמא לשימוש
# string1 = "HEART"
# string2 = "CHART"
# data = lcs_with_tracking(string1, string2)
# save_lcs_to_html(string1, string2, data)