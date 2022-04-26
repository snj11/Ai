from queue import LifoQueue

graph = {
    "Amravati": ['Dhule', 'Akola', 'Nagpur'],
    "Akola": ['Jalgaon', 'Parbhani'],
    'Ahmednagar': ['Pune', 'Latur', 'Bid'],
    'Aurangabad': [None],
    'Bid': ['Aurangabad'],
    'Dhule': ['Nagpur'],
    'Nagpur': ['Wardha'],
    'Wardha': ['Amravati', 'Nanded'],
    'Ratnagiri': ['Mumbai'],
    'Mumbai': ['Nandurbar', 'Pune', 'Satara'],
    'Pune': ['Jalgaon'],
    'Kolhapur': ['Ratnagiri'],
    'Satara': ['Pune'],
    'Sangli': ['Satara'],
    "Solapur": ['Sangli'],
    'Latur': ['Solapur'],
    'Nasik': ['Amravati', 'Mumbai', 'Pune'],
    'Nandurbar': ['Amravati', 'Dhule'],
    'Jalgaon': ['Nasik', 'Ahmednagar'],
    'Parbhani': ['Ahmednagar', 'Nanded'],
    'Nanded': ["Latur", 'Bid']
}


def ret_value(k):
    for key, value in graph.items():
        if key == k:
            return value


def dfs(graph, start_node, end_node):
    stack = LifoQueue()
    path = []
    if start_node in graph:
        stack.put(start_node)
        while stack.empty() == False:
            visit = stack.get()
            path.append(visit)
            if path[-1] != end_node:
                eles = ret_value(visit)
                eles.reverse()
                if eles != None:
                    for i in eles:
                        if i not in path:
                            stack.put(i)
            else:
                break
    path = list(dict.fromkeys(path))
    print('\ndfs path = ', path)


start_node = input("Enter the starting node: ")
end_node = input("Enter the ending node: ")

dfs(graph, start_node, end_node)
