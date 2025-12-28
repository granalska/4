import networkx as nx

#карта з першого завд
G = nx.Graph()
G.add_edges_from([
    ("Дружківка", "Краматорськ"),
    ("Краматорськ", "Слов'янськ"),
    ("Краматорськ", "Лиман"),
    ("Слов'янськ", "Святогірськ"),
    ("Лиман", "Святогірськ"),
    ("Дружківка", "Костянтинівка")])

#пошук
def find_path(graph, start, end, method):
    
    bag = [[start]]
    
    while bag:
        
        if method == "BFS":
            path = bag.pop(0) #перш щлях
        else:
            path = bag.pop()  #останній

        current_city = path[-1] 

        #результат виводимо в кінці
        if current_city == end:
            return path
        
        for neighbor in graph.neighbors(current_city):
            #якщо це новий шлях
            if neighbor not in path:
                new_path = list(path)
                new_path.append(neighbor)
                bag.append(new_path)

#перевірка
print("Шлях від Дружківки до Святогірська:")

#BFS
result1 = find_path(G,"Дружківка", "Святогірськ", "BFS")
print(f"BFS (Короткий):{result1}")

#DFS
result2 = find_path(G,"Дружківка", "Святогірськ", "DFS")
print(f"DFS (Довгий):{result2}")


