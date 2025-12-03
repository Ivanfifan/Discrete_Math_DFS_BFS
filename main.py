import random
import time
from collections import deque
import networkx as nx  # Бібліотека для роботи з графами
import matplotlib.pyplot as plt  # Бібліотека для малювання

# -------------------------------
# Клас графа
# -------------------------------
class Graph:
    def __init__(self, n):
        self.n = n # Кількість вершин графу

        self.adj_list = {} # Cтворюємо список суміжності
        for i in range(n):
            self.adj_list[i] = []

        self.adj_matrix = [] # Cтворюємо матрицю суміжності
        for i in range(n):
            row = []
            for k in range(n):
                row.append(0)
            self.adj_matrix.append(row)

    def add_edge(self, u, v): # Додає неорієнтоване ребро між вершинами u та v
        if v not in self.adj_list[u]:
            self.adj_list[u].append(v)
            self.adj_list[v].append(u)

        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1

    def adj_list_to_matrix(self):
        """Оновлює матрицю суміжності на основі списку суміжності."""
        self.adj_matrix = [[0] * self.n for _ in range(self.n)]

        for u in self.adj_list:
            for v in self.adj_list[u]:
                self.adj_matrix[u][v] = 1
                self.adj_matrix[v][u] = 1  # бо граф неорієнтований


    def matrix_to_adj_list(self):
        """Оновлює список суміжності на основі матриці суміжності."""
        self.adj_list = {i: [] for i in range(self.n)}

        for u in range(self.n):
            for v in range(self.n):
                if self.adj_matrix[u][v] == 1:
                    self.adj_list[u].append(v)

    # --- 1. DFS (Пошук у глибину) ---

    def dfs_using_list(self):
        """DFS, що використовує список суміжності"""
        r = [[0] * self.n for _ in range(self.n)]
        for start_node in range(self.n):
            stack = [start_node]
            visited = {start_node}
            r[start_node][start_node] = 1

            while stack:
                u = stack.pop()
                for v in self.adj_list[u]:
                    if v not in visited:
                        visited.add(v)
                        r[start_node][v] = 1
                        stack.append(v)
        return r

    def dfs_using_matrix(self):
        """DFS, що використовує матрицю суміжності"""
        r = [[0] * self.n for _ in range(self.n)]
        for start_node in range(self.n):
            stack = [start_node]
            visited = {start_node}
            r[start_node][start_node] = 1

            while stack:
                u = stack.pop()
                for v in range(self.n):
                    if self.adj_matrix[u][v] == 1:
                        if v not in visited:
                            visited.add(v)
                            r[start_node][v] = 1
                            stack.append(v)
        return r

    # --- 2. BFS (Пошук у ширину) ---

    def bfs_using_list(self):
        """BFS, що використовує список суміжності."""
        r = [[0] * self.n for _ in range(self.n)]
        for start_node in range(self.n):
            queue = deque([start_node])
            visited = {start_node}
            r[start_node][start_node] = 1

            while queue:
                u = queue.popleft()
                for v in self.adj_list[u]:
                    if v not in visited:
                        visited.add(v)
                        r[start_node][v] = 1
                        queue.append(v)
        return r

    def bfs_using_matrix(self):
        """BFS, що використовує матрицю суміжності."""
        r = [[0] * self.n for _ in range(self.n)]
        for start_node in range(self.n):
            queue = deque([start_node])
            visited = {start_node}
            r[start_node][start_node] = 1

            while queue:
                u = queue.popleft()
                for v in range(self.n):
                    if self.adj_matrix[u][v] == 1:
                        if v not in visited:
                            visited.add(v)
                            r[start_node][v] = 1
                            queue.append(v)
        return r

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

def print_matrix(matrix):
    print("Матриця досяжності:")
    for row in matrix:
        print(row)
# --- ЗАПУСК ---

# Рекомендую брати менше вершин для малювання (наприклад, 10-15),
# бо 100 вершин перетворяться на "кашу".
g = Graph.random_graph_erdos_renyi(10, 0.2)

print_matrix(g.bfs_using_list())
print_matrix(g.dfs_using_matrix())
# Дивимось картинку
g.visualize()