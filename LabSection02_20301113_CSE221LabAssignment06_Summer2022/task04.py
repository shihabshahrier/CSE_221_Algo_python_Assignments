def printFunc(mark_sheet, ofile):
    for i in range(len(mark_sheet)):
        #print("Student: ",(i+1))
        ofile.write(f"Student: {i+1}")
        for j in range(len(mark_sheet[i])):
            # print("Course: ",(j+1))
            # print("Marks of Mid and Final: ")
            ofile.write(f"\nCourse: {j+1}")
            ofile.write("\nMarks of Mid and Final: ")
            ofile.write("\n")
            for k in range(len(mark_sheet[i][j])):
                #print(mark_sheet[i][j][k],end=" ")
                ofile.write(f"{mark_sheet[i][j][k]} ")
            #print()
            ofile.write("\n")
        #print()
        ofile.write("\n")
        
if __name__ == "__main__":
    ifile = open("input04.txt")
    ofile = open("output04.txt", "w")
    n = int(ifile.readline())
    m = int(ifile.readline())
    mark_sheet = []
    for i in range(n):
        s = []
        for j in range(m):
            marks = list(map(int, ifile.readline().split()))
            s.append(marks)
        mark_sheet.append(s)

    printFunc(mark_sheet, ofile)

    ofile.close()
    ifile.close()
    #print(mark_sheet)

# grade_sheet = [
#     [
#         [30, 25], [35, 40], [41, 45], [26, 26]
#     ],
#     [
#         [41, 45], [43, 47], [49, 44], [46, 47]
#     ],
#     [
#         [10, 15], [35, 20], [11, 17], [29, 16]
#     ]
# ]