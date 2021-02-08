from constraint import *


vertical_edges = []
horizontal_edges = []
cols = []
rows = []
#enter difficulty level
filename="normal.txt"
file = open(filename, "r")
line_number = 0
for line in file:
    line = line.rstrip("\n")
    if 1 <= line_number < 7:
        char_list = line.rsplit(",")
        for ch in char_list:
            ind = char_list.index(ch)
            char_list[ind] = int(ch)
        vertical_edges.append(char_list)
    elif 9 <= line_number < 15:
        char_list = line.rsplit(",")
        for ch in char_list:
            ind = char_list.index(ch)
            char_list[ind] = int(ch)
        horizontal_edges.append(char_list)
    elif 17 <= line_number < 18:
        char_list = line.rsplit(",")
        for ch in char_list:
            ind = char_list.index(ch)
            char_list[ind] = int(ch)
        cols.append(char_list)
        cols = cols[0]
    elif 20 <= line_number < 21:
        char_list = line.rsplit(",")
        for ch in char_list:
            ind = char_list.index(ch)
            char_list[ind] = int(ch)
        rows.append(char_list)
        rows = rows[0]
    line_number += 1



problem = Problem(BacktrackingSolver())

for i in range(1, 7):
    problem.addVariables(range(i * 10 + 1, i * 10 + 7), range(0, 2))

iterator_col = 1
for col in cols:
    # print(index_col)
    problem.addConstraint(ExactSumConstraint(col), range(10 + iterator_col, 70 + iterator_col, 10))
    iterator_col += 1

iterator_row = 1
for row in rows:
    # print(index_row)
    problem.addConstraint(ExactSumConstraint(row), range(10 * iterator_row + 1, 10 * iterator_row + 7))
    iterator_row += 1



for i in range(len(vertical_edges)):
    for x in range(len(vertical_edges[i])):
        # always checking the left neighbor of the current cell
        # when x is 0, we cant check the left neighbor since it doesnt exist
        if x != 0:
            if vertical_edges[i][x] == 0:
                problem.addConstraint(AllEqualConstraint(), [10 * (i + 1) + (x + 1), 10 * (i + 1) + (x + 1) - 1])

for p in range(len(horizontal_edges)):
    for q in range(len(horizontal_edges)):
        # always checking the down neighbor of the current cell
        # when x is 6, we cant check the down neighbor since it doesnt exist
        if q != 6:
            if horizontal_edges[p][q] == 0:
                # a is the lower column of b
                # if a is not 1, then b can not be 1
                # if a is 0, then b is 0
                # if a is 1, be can be either 0 or 1
                problem.addConstraint(lambda a, b: a >= b, [10 * (q + 1) + (p + 1), 10 * q + (p + 1)])

solution_list = sorted(sorted(x.items()) for x in problem.getSolutions())




#writes lists into files
output_file=filename.rstrip(".txt")+"_solution.txt"
f=open(output_file, "w")

def writing(r,f):
    for element in r:
        element= str(element)
        f.write(element+" ")
    f.write("\n")


#printing solution for the puzzle
print("Solution for the ", filename.rstrip(".txt"), " puzzle:")


r1, r2, r3, r4, r5, r6 = [], [], [], [], [], []
for key in range(len(solution_list[0])):
    if key in range(0, 6):
        r1.append(solution_list[0][key][1])
    elif key in range(6, 12):
        r2.append(solution_list[0][key][1])
    elif key in range(12, 18):
        r3.append(solution_list[0][key][1])
    elif key in range(18, 24):
        r4.append(solution_list[0][key][1])
    elif key in range(24, 30):
        r5.append(solution_list[0][key][1])
    elif key in range(30, 36):
        r6.append(solution_list[0][key][1])

writing(r1,f)
writing(r2,f)
writing(r3,f)
writing(r4,f)
writing(r5,f)
writing(r6,f)
print("\n", r1, "\n", r2, "\n", r3, "\n", r4, "\n", r5, "\n", r6)


