from typing import List

def ObtInfo(archivo):
    i = 0
    list_f = []
    with open(archivo) as file:
        list = ""
        for line in file:
            line = line.strip("\n")
            if line != "Estados":
                if line == "Alfabeto":
                    list += "/"
                    continue
                if line == "Transiciones":
                    list += "/"
                    continue
                list += line
                list += "/"

    list1 = list.split("//")

    while i < len(list1):
        list_f.append(list1[i].split("/"))
        i += 1
    return list_f
    file.close()


def ToDFA(t):
    #Primero haremos la tabla de transición
    trans_states0 = []
    trans_states = []
    trans_states2 = []
    u = 0
    v = 0
    y = 0
    for num in t:
        if num != "":
            state, alpha, end = num[0], num[1], num[3]
            for i in t:
                if alpha == i[1]:
                    if end != i[3] and state == i[0]:
                        new_state = state + " " + alpha + " -> " + end + "," + i[3]
                        new_state2 = state + " " + alpha + " -> " + i[3] + "," + end #Falta alguna lista que restinja los state y alpha, si esta dentro y el que esta dento es mayor no se repita, si es menor se reemplaza por el nuevo.
                        if new_state not in trans_states0 and new_state2 not in trans_states0:
                            trans_states0.append(new_state)
                    elif end == i[3]:
                        new_state = state + " " + alpha + " -> " + end
                        if new_state not in trans_states0:
                            trans_states2.append(new_state)
    while v < len(trans_states2):
        trans_states2[v] = trans_states2[v].split("->")
        v += 1
    while u < len(trans_states0):
        trans_states0[u] = trans_states0[u].split("->")
        u += 1
    for equal in trans_states2:
        for e in trans_states0:
            if equal[0] == e[0] and equal[1] != equal[0] and len(equal[1]) < len(e[1]) and e not in trans_states:
                trans_states.append(e)
            elif len(trans_states[y]) > len(equal):
                trans_states.append(equal)
        y += 1



    print(trans_states0)
    print(trans_states)




trans = []
txt = "nfa4.txt"
file_info = ObtInfo(txt)
states = file_info[0]
alphabet = file_info[1]
var = file_info[2]
x = 0
while(x < len(var)-1):
    trans.append(var[x].split(" "))
    x += 1
#print(trans)
ToDFA(trans)

