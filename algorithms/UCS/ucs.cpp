#include <iostream>
#include <vector>
#include <queue>
#include <functional>
#include <limits>

using namespace std;

// Define a structure to represent a node in the graph
struct Node
{
    int id;
    int cost;

    Node(int i, int c) : id(i), cost(c) {}
};

// Custom comparator for the priority queue
struct CompareNodes
{
    bool operator()(const Node &lhs, const Node &rhs) const
    {
        return lhs.cost > rhs.cost;
    }
};

// Uniform Cost Search implementation
vector<int> uniform_cost_search(vector<vector<pair<int, int>>> &graph, int start, int goal)
{
    int numNodes = graph.size();

    priority_queue<Node, vector<Node>, CompareNodes> frontier;
    frontier.push(Node(start, 0));

    vector<bool> visited(numNodes, false);
    vector<int> cameFrom(numNodes, -1);
    vector<int> costSoFar(numNodes, numeric_limits<int>::max());

    costSoFar[start] = 0;

    while (!frontier.empty())
    {
        Node current = frontier.top();
        frontier.pop();

        int currNode = current.id;

        if (currNode == goal)
        {
            // Reconstruct the path by backtracking
            vector<int> path;
            while (currNode != start)
            {
                path.push_back(currNode);
                currNode = cameFrom[currNode];
            }
            path.push_back(start);
            reverse(path.begin(), path.end());
            return path;
        }

        // if visited[currNode]: continue;

        visited[currNode] = true;

        for (const auto &neighbor : graph[currNode])
        {
            int nextNode = neighbor.first;
            int edgeCost = neighbor.second;

            if (!visited[nextNode])
            {
                int newCost = costSoFar[currNode] + edgeCost;
                if (newCost < costSoFar[nextNode])
                {
                    costSoFar[nextNode] = newCost;
                    cameFrom[nextNode] = currNode;
                    frontier.push(Node(nextNode, newCost));
                }
            }
        }
    }

    return vector<int>();
}

int main()
{
    // Example graph represented as an adjacency list of (neighbor, edge cost) pairs
    vector<vector<pair<int, int>>> graph = {
        {{1, 4}, {2, 2}},
        {{3, 5}},
        {{3, 1}},
        {{4, 3}},
        {},
        {{3, 1}}};

    int startNode = 0;
    int goalNode = 4;

    vector<int> path = uniform_cost_search(graph, startNode, goalNode);

    if (!path.empty())
    {
        cout << "Path from " << startNode << " to " << goalNode << ": ";
        for (int node : path)
        {
            cout << node << " ";
        }
        cout << endl;
    }
    else
    {
        cout << "No path found." << endl;
    }

    return 0;
}
