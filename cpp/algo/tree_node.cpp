#include <iostream>
using namespace std;

struct Node{
    int _id;
    int data;
    Node *left;
    Node *right;

    Node(int id) : _id(id), data(0), left(NULL), right(NULL){
        cout << "Node constructor: " << _id << endl;
    }
    ~Node(){ // Just to show destructor is called
        cout << "Node destructor: " << _id << endl;
    }
};

void add_edge(Node *nodes[], int p, int left, int right)
{
    if (left > 0)  nodes[p-1]->left = nodes[left-1];
    if (right > 0) nodes[p-1]->right = nodes[right-1];
}

int height(Node* node)
{
    if (node == NULL) return 0;
    int left_height = height(node->left);
    int right_height = height(node->right);
    return node->data = 1 + max(left_height, right_height);
}

void calc_height(Node* node)
{
    if (node == NULL) return;
    int x = 0;
    if (node->left != NULL){
    	calc_height(node->left);
    	x = node->left->data;
    }
    if (node->right != NULL){
    	calc_height(node->right);
    	if (node->right->data > x) x = node->right->data;
    }
    node->data = x + 1;
}

void MLR(Node *node)
{
    if (node == NULL) return;
    cout << node->_id << " (" << node->data << ")" << endl;
    MLR(node->left);
    MLR(node->right);
}

void test_0()
{
	const int N = 5;
	Node *nodes[N];
	for (int i=0; i<N; ++i)
		nodes[i] = new Node(i);

	add_edge(nodes, 1, 2, 3);
	add_edge(nodes, 2, 4, 5);

	calc_height(nodes[0]);
    MLR(nodes[0]);

	for (int i=0; i<N; ++i)
		delete nodes[i];
}

void test_1()
{
    auto_ptr<Node> root( new Node(1) );
    auto_ptr<Node> n2  ( new Node(2) );
    auto_ptr<Node> n3  ( new Node(3) );
    auto_ptr<Node> n4  ( new Node(4) );
    auto_ptr<Node> n5  ( new Node(5) );

    root->left = n2.get();
    root->right = n3.get();

    n2->left = n4.get();
    n2->right = n5.get();

	height(root.get());
    MLR(root.get());
}

int main(){
	test_0();
	test_1();
}
