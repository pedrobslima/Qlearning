def prints(state: int):
    x = state%4
    if(x == 0): way = 'N'
    elif(x == 1): way = 'L'
    elif(x == 2): way = 'S'
    elif(x == 3): way = 'O'
    return str(state//4) + way

q_table = []

table_file = open("resultado.txt", "r")
for line in table_file:
    left = float(line.split(' ')[0])
    right = float(line.split(' ')[1])
    jump = float(line.split(' ')[2])
    q_table.append([left, right, jump])
table_file.close()

for i in range(len(q_table)):
    print(f"{prints(i)}:\n{q_table[i][0]} | {q_table[i][1]} | {q_table[i][2]}")