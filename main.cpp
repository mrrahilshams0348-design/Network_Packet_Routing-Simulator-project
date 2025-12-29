#include <iostream>
#include "graph.h"
#include "routing.h"
using namespace std;

int main() {
    Graph graph(5);
    graph.addEdge(0, 1, 2);
    graph.addEdge(0, 2, 4);
    graph.addEdge(1, 2, 1);
    graph.addEdge(1, 3, 7);
    graph.addEdge(2, 4, 3);
    graph.addEdge(3, 4, 1);

    int source = 0, destination = 4;
    int cost;
    vector<int> path = Routing::dijkstra(graph, source, destination, cost);

    cout << "Path: ";
    for(int node: path) cout << node << " ";
    cout << "\nTotal Cost: " << cost << endl;

    return 0;
}
