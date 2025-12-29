#include "routing.h"
#include <queue>
#include <climits>
#include <algorithm>

vector<int> Routing::dijkstra(const Graph& graph, int source, int destination, int& totalCost) {
    int n = graph.getNumNodes();
    const auto& adj = graph.getAdjList();
    vector<int> dist(n, INT_MAX), parent(n, -1);
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;

    dist[source] = 0;
    pq.push({0, source});

    while(!pq.empty()) {
        int u = pq.top().second; pq.pop();
        for(auto edge: adj[u]) {
            int v = edge.first, w = edge.second;
            if(dist[v] > dist[u] + w) {
                dist[v] = dist[u] + w;
                parent[v] = u;
                pq.push({dist[v], v});
            }
        }
    }

    totalCost = dist[destination];
    vector<int> path;
    for(int v = destination; v != -1; v = parent[v])
        path.push_back(v);
    reverse(path.begin(), path.end());
    return path;
}
