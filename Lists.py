def commdr(lst, instruct): 
    if instruct[0] == 'insert':
        lst.insert(int(instruct[1]), int(instruct[2]))
    elif instruct[0] == 'print':
        print(lst)
    elif instruct[0] == 'remove':
        lst.remove(int(instruct[1]))
    elif instruct[0] == 'append':
        lst.append(int(instruct[1]))
    elif instruct[0] == 'sort':
        lst.sort()
    elif instruct[0] == 'reverse':
        lst.reverse()
    elif instruct[0] == 'pop':
        lst.pop()
    else: 
        print("Command not recognized!")

if __name__ == '__main__':
    N = int(input())
    lst=[]
    for command in range(N):
        temp = [str(i) for i in input().strip().split()]
        commdr(lst, temp)
