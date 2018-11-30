#include <iostream>
using namespace std;

struct Node{
    int _id;
    int data;
    Node *left, *right;
    Node(int id) : _id(id), data(0), left(NULL), right(NULL){
        cout << "Node constructor: " << _id << endl;
    }
    ~Node(){
        cout << "Node destructor: " << _id << endl;
    }
    friend ostream &operator<<(ostream &os, const Node &node);
};

ostream& operator<<(ostream &os, const Node& node){
    os << node._id << " (" << node.data << ")";
    return os;
}

int height(Node* node)
{
    if (node == NULL) return 0;
    int left_height = height(node->left);
    int right_height = height(node->right);
    return node->data = 1 + max(left_height, right_height);
}

typedef Node *NodePointer;
class Tree{
private:
    const int N;
    NodePointer *nodes;
    int height(Node* node);

    void MLR(Node *node);
    void LMR(Node *node);
    Node *BFS(Node *node, int value);
    Node *DFS(Node *node, int value);

    Node *furthest(Node *node);    // Use DFS to find furthest
public:
    Tree(const int N);
    ~Tree();
    void add_edge(int p, int left, int right);
    void height() { height(nodes[0]); }

    void MLR()    { cout << "MLR" << endl; MLR(nodes[0]); }
    void LMR()    { cout << "LMR" << endl; LMR(nodes[0]); }
    Node *BFS(int value) { cout << "BFS" << endl; return BFS(nodes[0], value); }
    Node *DFS(int value) { cout << "DFS" << endl; return DFS(nodes[0], value); }

    Node *furthest() { cout << "furthest" << endl; return furthest(nodes[0]); }
};

Tree::Tree(const int N) : N(N){
    nodes = new NodePointer[N];
    for (int i=0; i<N; ++i)
        nodes[i] = new Node(i+1);
}
Tree::~Tree(){
    cout << "Tree destructor: " << endl;
    for (int i=0; i<N; ++i)
        delete nodes[i];
    delete nodes;
}
void Tree::add_edge(int p, int left, int right)
{
    if (left > 0 && left <= N)  nodes[p-1]->left = nodes[left-1];
    if (right > 0 && left <= N) nodes[p-1]->right = nodes[right-1];
}
int Tree::height(Node* node)
{
    if (node == NULL) return 0;
    int left_height = height(node->left);
    int right_height = height(node->right);
    return node->data = 1 + max(left_height, right_height);
}
void Tree::MLR(Node *node)
{
    if (node == NULL) return;
    cout << *node << endl;
    MLR(node->left);
    MLR(node->right);
}
void Tree::LMR(Node *node)
{
    if (node == NULL) return;
    LMR(node->left);
    cout << *node << endl;
    LMR(node->right);
}
Node *Tree::BFS(Node *node, int value){
    if (node == NULL) return NULL; // Not found

    cout << *node << endl;
    if (node->_id == value) return node; // Found

    Node *n = BFS(node->left, value);
    if (n != NULL) return n;

    n = BFS(node->right, value);
    if (n != NULL) return n;

    return NULL;
}
Node *Tree::DFS(Node *node, int value){
    if (node == NULL) return NULL;

    Node *n = DFS(node->left, value);
    if (n != NULL) return n;

    cout << *node << endl;
    if (node->_id == value) return node; // Found

    n = DFS(node->right, value);
    if (n != NULL) return n;

    return NULL;
}

Node *Tree::furthest(Node *node)
{
    if (node == NULL) return NULL;
    LMR(node->left);
    cout << *node << endl;
    LMR(node->right);
}

void test_1()
{
    Tree tree(5);
    tree.add_edge(1, 2, 3);
    tree.add_edge(2, 4, 5);
    tree.height();
    tree.MLR();
    tree.LMR();

    Node *node = tree.DFS(3);
    if (node) cout << *node << endl;

    node = tree.BFS(4);
    if (node) cout << *node << endl;
}

void test_4()
{
    Tree tree(13);

    tree.add_edge(1, 2, 3);
    tree.add_edge(2, 4, 9);
    tree.add_edge(4, 5, 6);
    tree.add_edge(6, 7, 0);
    tree.add_edge(7, 0, 8);
    tree.add_edge(9, 0,10);
    tree.add_edge(10,11,12);
    tree.add_edge(12,13, 0);

    tree.height();
    tree.LMR();
}

int main()
{
    test_4();
}
