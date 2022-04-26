from queue import Queue
from queue import LifoQueue

graph = {
    'Amravati': ['Dhule', 'Akola', 'Nagpur'],  # 1
    'Akola': ['Jalgaon', 'Parbhani'],  # 2
    'Ahmednagar': ['Pune', 'Latur', 'Bid'],  # 3
    'Aurangabad': [None],  # 4
    'Bid': ['Aurangabad'],  # 5
    'Dhule': ['Nagpur'],  # 6
    'Nagpur': ['Wardha'],  # 7
    'Wardha': ['Amravati', 'Nanded'],  # 8
    'Ratnagiri': ['Mumbai'],  # 9
    'Mumbai': ['Nandurbar', 'Pune', 'Satara'],  # 10
    'Pune': ['Jalgaon'],  # 11
    'Kolhapur': ['Ratnagiri'],  # 12
    'Satara': ['Pune'],  # 13
    'Sangli': ['Satara'],  # 14
    'Solapur': ['Sangli'],  # 15
    'Latur': ['Solapur'],  # 16
    'Nasik': ['Amravati', 'Mumbai', 'Pune'],  # 17
    'Nandurbar': ['Amravati', 'Dhule'],  # 18
    'Jalgaon': ['Nasik', 'Ahmednagar'],  # 19
    'Parbhani': ['Ahmednagar', 'Nanded'],  # 20
    'Nanded': ['Latur', 'Bid'],  # 21
}


def ret_value(k):
    for key, value in graph.items():
        if key == k:
            return value


def bfs(graph, start_node, end_node):
    q = Queue()
    path = []
    if start_node in graph:
        q.put(start_node)
        while q.empty() == False:
            visit = q.get()
            path.append(visit)
            if path[-1] != end_node:
                eles = ret_value(visit)
                if eles != None:
                    for i in eles:
                        if i not in path:
                            q.put(i)
            else:
                break
    path = list(dict.fromkeys(path))
    print('\nbfs path = ', path)


start_node = input("Enter the starting node: ")  # 'Amravati'
end_node = input("Enter the ending node: ")  # 'Mumbai'
bfs(graph, start_node, end_node)
#dfs(graph, start_node, end_node)

# In[ ]:
