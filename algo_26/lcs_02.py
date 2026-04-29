
# משתנים גלובליים למעקב
call_counter = 0
def draw_lcs_tree(s1, s2):
    global call_counter
    call_counter = 0
    dot = graphviz.Digraph(comment='LCS Recursion Tree')
    dot.attr(rankdir='TB', size='10')
    
    def lcs_recursive(str1, str2, parent_id=None):
        global call_counter
        call_counter += 1
        current_id = str(call_counter)
        my_call_num = call_counter
        
        # יצירת תווית התחלתית (לפני שיודעים את התוצאה)
        label = f"#{my_call_num}\nS1: '{str1}'\nS2: '{str2}'"
        dot.node(current_id, label)
        
        if parent_id:
            dot.edge(parent_id, current_id)
            
        # חישוב ה-LCS
        if str1 == "" or str2 == "":
            result = ""
        elif str1[-1] == str2[-1]:
            result = lcs_recursive(str1[:-1], str2[:-1], current_id) + str1[-1]
        else:
            res1 = lcs_recursive(str1, str2[:-1], current_id)
            res2 = lcs_recursive(str1[:-1], str2, current_id)
            result = res1 if len(res1) > len(res2) else res2
            
        # עדכון הצומת עם התוצאה הסופית
        final_label = f"#{my_call_num}\nIn: '{str1}', '{str2}'\nOut: '{result}'"
        dot.node(current_id, final_label, color='lightblue', style='filled')
        
        return result
    lcs_recursive(s1, s2)
    return dot
# הרצה עבור מחרוזות קצרות (כדי שהעץ יהיה קריא)
s1 = "ABC"
s2 = "AC"
tree = draw_lcs_tree(s1, s2)
# שמירה והצגה
tree.render('lcs_tree', format='png', view=True)
print("העץ נוצר בהצלחה בקובץ lcs_tree.png")