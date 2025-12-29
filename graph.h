#ifndef GRAPH_H
#define GRAPH_H

#include <vector>
#include <utility>
using namespace std;

class Graph {
private:
    int numNodes;
    vector<vector<pair<int, int>>> adjList;

public:
    Graph(int n);
    void addEdge(int u, int v, int weight);
    int getNumNodes() const;
    const vector<vector<pair<int, int>>>& getAdjList() const;
};

#endif
