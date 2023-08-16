import connection_teste as cn

def convert_action(action):
    if(type(action) == int):
        if(action == 0): return "left"
        elif(action == 1): return "right"
        elif(action == 2): return "jump"
    elif(type(action) == str):
        if(action == "left"): return 0
        elif(action == "right"): return 1
        elif(action == "jump"): return 2

def prints(state: int):
    x = state%4
    if(x == 0): way = 'N'
    elif(x == 1): way = 'L'
    elif(x == 2): way = 'S'
    elif(x == 3): way = 'O'
    return str(state//4) + way

skt = cn.connect(2037)
q_table = []

table_file = open("resultado copy.txt", "r")
for line in table_file:
    left = float(line.split(' ')[0])
    right = float(line.split(' ')[1])
    jump = float(line.split(' ')[2])
    q_table.append([left, right, jump])
table_file.close()

count = 1
recompensa = -1
state = 0
while(recompensa <= 0):
    acao = q_table[state].index(max(q_table[state]))
    state, recompensa = cn.get_state_reward(skt, convert_action(acao))
    state = int(state, 2)
    print(str(count)+':', prints(state), convert_action(acao), recompensa)

'''
for i in range(len(q_table)):
    print(f"{prints(i)}:\n{q_table[i][0]} | {q_table[i][1]} | {q_table[i][2]}")
'''
'''recompensa = -1
curr_state = 0
rept = 1
while(recompensa <= 0):
    acao = q_table[curr_state].index(max(q_table[curr_state]))
    curr_state, recompensa = cn.get_state_reward(skt, convert_action(acao))
    curr_state = int(curr_state, 2)
    print(str(rept)+':', convert_action(acao), prints(curr_state), recompensa, q_table[curr_state][acao])
    rept += 1'''

'''
file = open("zerar.txt", "r")
og = open("resultado.txt", "w")
og.write(file.read())
file.close()
og.close()
'''
'''
import connection as cn
skt = cn.connect(2037)

def prints(state: str):
    state = int(state, 2)
    x = state%4
    if(x == 0): way = 'N'
    elif(x == 1): way = 'L'
    elif(x == 2): way = 'S'
    elif(x == 3): way = 'O'
    return str(state//4) + way

new_state, recompensa = cn.get_state_reward(skt, 'jump')
print(prints(new_state), recompensa)
new_state, recompensa = cn.get_state_reward(skt, 'left')
print(prints(new_state), recompensa)
new_state, recompensa = cn.get_state_reward(skt, 'jump')
print(prints(new_state), recompensa)
new_state, recompensa = cn.get_state_reward(skt, 'jump')
print(prints(new_state), recompensa)
new_state, recompensa = cn.get_state_reward(skt, 'jump')
print(prints(new_state), recompensa)
new_state, recompensa = cn.get_state_reward(skt, 'jump')
print(prints(new_state), recompensa)
new_state, recompensa = cn.get_state_reward(skt, 'jump')
print(prints(new_state), recompensa)
new_state, recompensa = cn.get_state_reward(skt, 'right')
print(prints(new_state), recompensa)
new_state, recompensa = cn.get_state_reward(skt, 'jump')
print(prints(new_state), recompensa)
new_state, recompensa = cn.get_state_reward(skt, 'jump')
print(prints(new_state), recompensa)
new_state, recompensa = cn.get_state_reward(skt, 'left')
print(prints(new_state), recompensa)
new_state, recompensa = cn.get_state_reward(skt, 'jump')
print(prints(new_state), recompensa)'''