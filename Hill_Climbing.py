graph = {
    'Amravati': [('Dhule', 37), ('Akola', 42), ('Nagpur', 30)],  # 1
    'Akola': [('Jalgaon', 35), ('Parbhani', 25)],  # 2
    'Ahmednagar': [('Pune', 29), ('Latur', 33), ('Bid', 11)],  # 3
    'Aurangabad': [None],  # 4
    'Bid': [('Aurangabad', 60)],  # 5
    'Dhule': [('Nagpur', 7)],  # 6
    'Nagpur': [('Wardha', 15)],  # 7
    'Wardha': [('Amravati', 20), ('Nanded', 39)],  # 8
    'Ratnagiri': [('Mumbai', 47)],  # 9
    'Mumbai': [('Nandurbar', 50), ('Pune', 55), ('Satara', 35)],  # 10
    'Pune': [('Jalgaon', 40)],  # 11
    'Kolhapur': [('Ratnagiri', 20)],  # 12
    'Satara': [('Pune', 31)],  # 13
    'Sangli': [('Satara', 27)],  # 14
    'Solapur': [('Sangli', 39)],  # 15
    'Latur': [('Solapur', 70)],  # 16
    'Nasik': [('Amravati', 50), ('Mumbai', 20), ('Pune', 19)],  # 17
    'Nandurbar': [('Amravati', 40), ('Dhule', 15)],  # 18
    'Jalgaon': [('Nasik', 21), ('Ahmednagar', 32)],  # 19
    'Parbhani': [('Ahmednagar', 60), ('Nanded', 17)],  # 20
    'Nanded': [('Latur', 15), ('Bid', 16)],  # 21
}

start = 'Amravati'  # change start node here, can also change to user input
Closed = list()


def MOVEGEN(N):
    new_list = list()
    if N in graph.keys():
        new_list = graph[N]
    return new_list


def SORT(L):
    L.sort(key=lambda x: x[1])
    return L


def heu(Node):
    return Node[1]


def APPEND(L1, L2):
    new_list = list(L1) + list(L2)
    return new_list


def Hill_Climbing(start):
    global closed
    N = start
    child = MOVEGEN(N)
    SORT(child)
    var = int(input(f"Enter the Value or cost for {start}: "))
    N = [start, var]  # assign a value to the start node, change here, can take user input
    print("\nStart: ", N)
    print("Edges: ", child)
    newnode = child[0]
    closed = [N]

    while heu(newnode) <= heu(N):
        print('\n------------------')
        N = newnode
        print('Next visited node = ', N)
        closed = APPEND(closed, [N])
        child = MOVEGEN(N[0])
        SORT(child)
        print("Edges = ", child)
        newnode = child[0]
    Closed = closed


Hill_Climbing(start)
