import random
import networkx as nx  # Бібліотека для роботи з графами
import matplotlib.pyplot as plt  # Бібліотека для малювання

# створив гілку тест
# перед пушом в мастер воркаємо тута

class Graph:
    def __init__(self, n):
        self.n = n # кількість вершин графу

        self.adj_list = {} # створюємо список суміжності
        for i in range(n):
            self.adj_list[i] = []

        self.adj_matrix = [] # створюємо матрицю суміжності
        for i in range(n):
            row = []
            for k in range(n):
                row.append(0)
            self.adj_matrix.append(row)

    def add_edge(self, u, v): # функцію для додавання пар в граф
        if v not in self.adj_list[u]:
            self.adj_list[u].append(v)
            self.adj_list[v].append(u)

        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1

    @staticmethod
    def random_graph_erdos_renyi(n, density): # модель Ердеша-Реньї
        g = Graph(n)
        for i in range(n):
            for j in range(i + 1, n):
                if random.random() < density:
                    g.add_edge(i, j)
        return g

    # --- НОВА ФУНКЦІЯ ДЛЯ ВІЗУАЛІЗАЦІЇ ---
    def visualize(self):
        # 1. Створюємо об'єкт графа бібліотеки NetworkX
        nx_graph = nx.Graph()

        # 2. Переносимо дані з вашого списку суміжності в NetworkX
        for u in self.adj_list:
            nx_graph.add_node(u)  # Додаємо вершину
            for v in self.adj_list[u]:
                nx_graph.add_edge(u, v)  # Додаємо ребро

        # 3. Налаштовуємо малювання
        plt.figure(figsize=(8, 6))  # Розмір картинки

        # Вибираємо красиве розташування точок (пружинна модель)
        pos = nx.spring_layout(nx_graph)

        # Малюємо сам граф
        nx.draw(nx_graph, pos,
                with_labels=True,  # Показати номери вершин
                node_color='lightblue',  # Колір кружечків
                edge_color='gray',  # Колір ліній
                node_size=500,  # Розмір кружечків
                font_weight='bold')  # Жирний шрифт

        plt.title("Мій випадковий граф")
        plt.show()


# --- ЗАПУСК ---

# Рекомендую брати менше вершин для малювання (наприклад, 10-15),
# бо 100 вершин перетворяться на "кашу".
g = Graph.random_graph_erdos_renyi(10, 0.4)

# Дивимось текстовий вигляд
print("Список суміжності:", g.adj_list)

# Дивимось картинку
g.visualize()