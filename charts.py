import pandas as pd
import matplotlib.pyplot as plt
import os

# === Завантаження даних ===
file_path = "results.tsv"     # файл у поточній папці
df = pd.read_csv(file_path, sep='\t')

# Папка, де лежить TSV
output_dir = os.path.dirname(os.path.abspath(file_path))

# Нормалізація типів
df['nodes'] = df['nodes'].astype(int)
df['density'] = df['density'].astype(float)

# === 1. BFS list vs matrix ===
plt.figure()
subset = df[df['method'] == 'BFS']
for rep, rep_name in [('list', 'Список суміжності'), ('matrix', 'Матриця суміжності')]:
    sub = subset[subset['representation'] == rep].groupby('nodes')['average_time_sec'].mean()
    plt.plot(sub.index, sub.values, marker='o', label=rep_name)

plt.title("Порівняння BFS: список vs матриця")
plt.xlabel("Кількість вершин")
plt.ylabel("Середній час (секунди)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "BFS_list_vs_matrix.png"))
plt.close()

# === 2. DFS list vs matrix ===
plt.figure()
subset = df[df['method'] == 'DFS']
for rep, rep_name in [('list', 'Список суміжності'), ('matrix', 'Матриця суміжності')]:
    sub = subset[subset['representation'] == rep].groupby('nodes')['average_time_sec'].mean()
    plt.plot(sub.index, sub.values, marker='o', label=rep_name)

plt.title("Порівняння DFS: список vs матриця")
plt.xlabel("Кількість вершин")
plt.ylabel("Середній час (секунди)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "DFS_list_vs_matrix.png"))
plt.close()

# === 3. BFS list — вплив щільності ===
plt.figure()
subset = df[(df['method'] == 'BFS') & (df['representation'] == 'list')]
for d in sorted(subset['density'].unique()):
    sub = subset[subset['density'] == d].groupby('nodes')['average_time_sec'].mean()
    plt.plot(sub.index, sub.values, marker='o', label=f"Щільність = {d}")

plt.title("BFS (список): вплив щільності ребер")
plt.xlabel("Кількість вершин")
plt.ylabel("Середній час (секунди)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "BFS_density_list.png"))
plt.close()

# === 4. DFS list — вплив щільності ===
plt.figure()
subset = df[(df['method'] == 'DFS') & (df['representation'] == 'list')]
for d in sorted(subset['density'].unique()):
    sub = subset[subset['density'] == d].groupby('nodes')['average_time_sec'].mean()
    plt.plot(sub.index, sub.values, marker='o', label=f"Щільність = {d}")

plt.title("DFS (список): вплив щільності ребер")
plt.xlabel("Кількість вершин")
plt.ylabel("Середній час (секунди)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "DFS_density_list.png"))
plt.close()

# === 5. BFS matrix — вплив щільності ===
plt.figure()
subset = df[(df['method'] == 'BFS') & (df['representation'] == 'matrix')]
for d in sorted(subset['density'].unique()):
    sub = subset[subset['density'] == d].groupby('nodes')['average_time_sec'].mean()
    plt.plot(sub.index, sub.values, marker='o', label=f"Щільність = {d}")

plt.title("BFS (матриця): вплив щільності ребер")
plt.xlabel("Кількість вершин")
plt.ylabel("Середній час (секунди)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "BFS_density_matrix.png"))
plt.close()

# === 6. DFS matrix — вплив щільності ===
plt.figure()
subset = df[(df['method'] == 'DFS') & (df['representation'] == 'matrix')]
for d in sorted(subset['density'].unique()):
    sub = subset[subset['density'] == d].groupby('nodes')['average_time_sec'].mean()
    plt.plot(sub.index, sub.values, marker='o', label=f"Щільність = {d}")

plt.title("DFS (матриця): вплив щільності ребер")
plt.xlabel("Кількість вершин")
plt.ylabel("Середній час (секунди)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "DFS_density_matrix.png"))
plt.close()

