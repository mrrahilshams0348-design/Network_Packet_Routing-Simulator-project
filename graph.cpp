#include "graph.h"

Graph::Graph(int n) {
    numNodes = n;
    adjList.resize(n);
}

void Graph::addEdge(int u, int v, int weight) {
    adjList[u].push_back({v, weight});
    adjList[v].push_back({u, weight});
}

int Graph::getNumNodes() const {
    return numNodes;
}

const vector<vector<pair<int, int>>>& Graph::getAdjList() const {
    return adjList;
}
