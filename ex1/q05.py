def mult_table(rows,cols):
    print("   | ", end = "")
    for i in cols:
        print(str(i) + "| ", end = "")
    print("\n")
    for j in rows:
        print(str(j) + "| ", end = "")
        for i in cols:
            print(str(j*i) + " | ", end = "")
        print("\n")

rws = [1,2,4,6]
cls = [1,3,5,7]

mult_table(rws,cls)