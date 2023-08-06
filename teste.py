
file = open("zerar.txt", "r")
og = open("resultado.txt", "w")
og.write(file.read())
file.close()
og.close()

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