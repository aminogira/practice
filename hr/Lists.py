if __name__ == '__main__':
    N = 12

    cmdList = ["insert 0 5", "insert 1 10", "insert 0 6", "print", "remove 6", "append 9",
            "append 1", "sort", "print", "pop", "reverse", "print"]

    list = []

    for lin in cmdList :
        cmd = lin.split()
        if cmd[0] == "insert":
            list.insert(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == "print":
            print(list)
        elif cmd[0] == "remove":
            list.remove(int(cmd[1]))
        elif cmd[0] == "append":
            list.append(int(cmd[1]))
        elif cmd[0] == "sort":
            list.sort()
        elif cmd[0] == "pop":
            list.pop()
        elif cmd[0] == "reverse":
            list.reverse()







