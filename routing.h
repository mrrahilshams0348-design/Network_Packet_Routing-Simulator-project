#ifndef ROUTING_H
#define ROUTING_H

#include "graph.h"
#include <vector>
using namespace std;

class Routing {
public:
    static vector<int> dijkstra(const Graph& graph, int source, int destination, int& totalCost);
};

#endif
