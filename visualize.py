import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.animation import FuncAnimation
import numpy as np

# Network structure
edges = [
    (0,1,2),(0,2,4),(1,2,1),(1,3,7),
    (2,4,3),(3,4,1)
]

def interpolate_points(p1, p2, steps=25):
    x_vals = np.linspace(p1[0], p2[0], steps)
    y_vals = np.linspace(p1[1], p2[1], steps)
    return list(zip(x_vals, y_vals))

def build_smooth_path(path, pos):
    smooth = []
    for i in range(len(path)-1):
        smooth += interpolate_points(pos[path[i]], pos[path[i+1]])
    return smooth

def animate_multiple_packets(paths):

    G = nx.Graph()
    for u,v,w in edges:
        G.add_edge(u,v,weight=w)

    pos = nx.spring_layout(G, seed=42)

    fig, ax = plt.subplots(figsize=(7,7))

    smooth_paths = [build_smooth_path(p, pos) for p in paths]
    max_frames = max(len(p) for p in smooth_paths)

    colors = ["red", "orange", "magenta", "cyan", "yellow"]

    def update(frame):
        ax.clear()

        nx.draw(G, pos, ax=ax, with_labels=True,
                node_color='lightblue',
                node_size=1200,
                edge_color='gray',
                width=2)

        for i, path in enumerate(paths):
            edges_list = list(zip(path, path[1:]))
            nx.draw_networkx_edges(G, pos,
                                    edgelist=edges_list,
                                    edge_color='green',
                                    width=3,
                                    ax=ax)

        for i, smooth in enumerate(smooth_paths):
            if frame < len(smooth):
                x, y = smooth[frame]
                ax.scatter(x, y, s=200, c=colors[i % len(colors)], zorder=5)

        ax.set_title("Real-Time Packet Routing Simulation", fontsize=14)

    ani = FuncAnimation(fig, update,
                        frames=max_frames,
                        interval=80,
                        repeat=False)

    plt.show()


def animate_routing(path):
    animate_multiple_packets([path])
