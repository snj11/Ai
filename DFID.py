def ret_value(k, var1, var=None):
    for key, value in var1.items():
        if var == None and key == k:
            return value
        if var == 'val' and value == k:
            return key


graph = {
    'Amravati': ['Dhule', 'Akola', 'Nagpur'],
    'Akola': ['Jalgaon', 'Parbhani'],
    'Ahmednagar': ['Pune', 'Latur', 'Bid'],
    'Aurangabad': [None],
    'Bid': ['Aurangabad'],
    'Dhule': ['Nagpur'],
    'Nagpur': ['Wardha'],
    'Wardha': ['Amravati', 'Nanded'],
    'Ratnagiri': ['Mumbai'],
    'Mumbai': ['Nandurbar', 'Pune', 'Satara'],
    'Pune': ['Jalgaon'],  # 11
    'Kolhapur': ['Ratnagiri'],
    'Satara': ['Pune'],
    'Sangli': ['Satara'],
    'Solapur': ['Sangli'],
    'Latur': ['Solapur'],
    'Nasik': ['Amravati', 'Mumbai', 'Pune'],
    'Nandurbar': ['Amravati', 'Dhule'],
    'Jalgaon': ['Nasik', 'Ahmednagar'],
    'Parbhani': ['Ahmednagar', 'Nanded'],
    'Nanded': ['Latur', 'Bid'],
}

max_depth = int(input("\nEnter the maximum traversal depth : "))
start_node = input("Enter start node: ")
destn_node = input("Enter destination node: ")

path = list()


def DFS(currentNode, destination, graph, maxDepth, curList):
    print("\n----- Next Iteration -----")
    print("Searching destination", currentNode)
    curList.append(currentNode)
    print(f"Path: {curList}")
    print("Queue: ", ret_value(curList[-1], graph))
    if currentNode == destination:
        return True
    if maxDepth <= 0:
        path.append(curList)
        return False
    for node in graph[currentNode]:
        if DFS(node, destination, graph, maxDepth - 1, curList):
            return True
        else:
            curList.pop()
    return False


def iterativeDDFS(currentNode, destination, graph, maxDepth):
    open_list = list(graph.keys())
    closed_list = []
    for i in range(maxDepth):
        curList = list()
        if DFS(currentNode, destination, graph, i, curList):
            return True
    return False


if not iterativeDDFS(start_node, destn_node, graph, max_depth):
    print("\nPath unavailable!")
else:
    print("\nA path exists!")
