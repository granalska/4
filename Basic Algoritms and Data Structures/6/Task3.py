import networkx as nx

G = nx.Graph()

roads = [
    ("Дружківка", "Краматорськ", 12),
    ("Краматорськ", "Слов'янськ", 15),
    ("Краматорськ", "Лиман", 25),      #пряма дорога
    ("Слов'янськ", "Лиман", 20),       #через слов'янськ
    ("Слов'янськ", "Святогірськ", 30),
    ("Лиман", "Святогірськ", 15),      #з лиману ближче до святогірська
    ("Дружківка", "Костянтинівка", 10)]

#додаємо ці дороги в граф
for start, end, distance in roads:
    G.add_edge(start, end, weight=distance)

#запускаємо дейкстру
shortest_paths = nx.single_source_dijkstra(G, source="Краматорськ", weight='weight')

#результат повертається як словн
distances = shortest_paths[0]
paths = shortest_paths[1]

#виводимо результат
print("Найкоротші маршрути з Краматорська:")

for city in distances:
    if city != "Краматорськ": #сам до себе шлях пропускаємо
        km = distances[city]
        route = " -> ".join(paths[city]) 
        print(f"До міста:{city}:")
        print(f"Відстань:{km} км")
        print(f"Маршрут:{route}")
        print("-" * 30)
