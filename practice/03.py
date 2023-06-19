
N = int(input())
my_list = []
cmds = {
    "insert" :"my_list.insert({},{})",
    "print" : "print(my_list)",
    "remove" : "my_list.remove({})",
    "append" : "my_list.append({})",
    "sort" : "my_list.sort()",
    "pop" : "my_list.pop()",
    "reverse" : "my_list.reverse()"
}

for i in range(N):
    a, *b = input("Enter your operation: ").split()
    b = [eval(i) for i in b]

    if len(b) == 2:
        eval(cmds[a].format(b[0],b[1]))
    elif len(b) == 1:
        eval(cmds[a].format(b[0]))
    else:
        eval(cmds[a])