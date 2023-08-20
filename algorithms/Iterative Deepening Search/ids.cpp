#include <iostream>
#include <vector>

class Node
{
public:
    int value;
    std::vector<Node *> children;

    Node(int val) : value(val) {}
};

int depthLimitedSearch(Node *node, int goalValue, int depthLimit)
{
    if (node->value == goalValue)
    {
        return node->value;
    }
    if (depthLimit == 0)
    {
        return -1; // Indicates not found
    }
    for (Node *child : node->children)
    {
        int result = depthLimitedSearch(child, goalValue, depthLimit - 1);
        if (result != -1)
        {
            return result;
        }
    }
    return -1; // Indicates not found
}

int iterativeDeepeningSearch(Node *root, int goalValue)
{
    int depth = 0;
    while (true)
    {
        int result = depthLimitedSearch(root, goalValue, depth);
        if (result != -1)
        {
            return result;
        }
        depth++;
    }
}

int main()
{
    // Create a sample tree
    Node *root = new Node(1);
    root->children.push_back(new Node(2));
    root->children.push_back(new Node(3));
    root->children[0]->children.push_back(new Node(4));
    root->children[0]->children.push_back(new Node(5));
    root->children[1]->children.push_back(new Node(6));

    int goalValue = 6;
    int result = iterativeDeepeningSearch(root, goalValue);

    if (result != -1)
    {
        std::cout << "Goal value " << goalValue << " found!" << std::endl;
    }
    else
    {
        std::cout << "Goal value " << goalValue << " not found." << std::endl;
    }

    // Clean up memory (deallocate nodes)
    // ...

    return 0;
}
