import networkx as nx
import matplotlib.pyplot as plt

#створюємо карту сполучень (граф)
Karta = nx.Graph()

#додаємо дороги та міста
Karta.add_edge("Дружківка", "Краматорськ", weight=12)
Karta.add_edge("Краматорськ", "Слов'янськ", weight=15)
Karta.add_edge("Слов'янськ", "Лиман", weight=20)
Karta.add_edge("Краматорськ", "Лиман", weight=25)


print("Малюю зелені міста та сірі дороги...")
pos = nx.spring_layout(Karta)

plt.figure(figsize=(8, 6)) #розмір мал

nx.draw(Karta, pos, 
        with_labels=True,
        node_color='lightgreen', #колір міст
        node_size=3500,          #розмір міст
        edge_color='gray',       #колір доріг
        width=4,                 #розмір доріг
        font_size=12)            #щрифт

#відстань на дорогах
labels = nx.get_edge_attributes(Karta, 'weight')
nx.draw_networkx_edge_labels(Karta, pos, edge_labels=labels, font_color='black')

plt.show() #показати малюнок

print("\n Аналіз карти сполучень між містами:")
print(f"Всього міст (зелених кружечків):{Karta.number_of_nodes()}")
print(f"Всього доріг (сірих ліній):{Karta.number_of_edges()}")

print("\n Центральне місто?")
#сортуємо
sorted_cities = sorted(Karta.degree(), key=lambda x: x[1], reverse=True)

for city, roads in sorted_cities:
    print(f"{city}: має {roads} виїзди")
