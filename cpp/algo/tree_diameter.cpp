#include <climits>
#include <algorithm>
#include <iostream>

using namespace std;

struct Node{
    int data;
    Node *left, *right;
    Node(int data) : data(data), left(NULL), right(NULL){}
};

void add_edge(Node *nodes[], int p, int left, int right){
    if (left > 0)  nodes[p-1]->left = nodes[left-1];
    if (right > 0) nodes[p-1]->right = nodes[right-1];
}

int height(Node* root, int& diameter)
{
    if (root == NULL) return 0;
    int left_height = height(root->left, diameter);
    int right_height = height(root->right, diameter);
    diameter = max(diameter, 1 + left_height + right_height);

    return 1 + max(left_height, right_height);
}

/* Computes the diameter of binary tree with given root. */
int diameter(Node* root)
{
    if (root == NULL)
        return 0;
    int diameter = INT_MIN; // This will store the final diameter
    int height_of_tree = height(root, diameter);
    return diameter;
}

void test_1()
{
	const int N = 13;
	Node *nodes[N];
	for (int i=0; i<N; ++i) nodes[i] = new Node(i);

	add_edge(nodes, 1, 2, 3);
	add_edge(nodes, 2, 4, 9);
	add_edge(nodes, 4, 5, 6);
	add_edge(nodes, 6, 7, 0);
	add_edge(nodes, 7, 0, 8);

	add_edge(nodes, 9, 0, 10);
	add_edge(nodes, 10,11,12);
	add_edge(nodes, 12,13, 0);

    printf("Diameter is %d\n", diameter(nodes[0]));
	for (int i=0; i<N; ++i) delete nodes[i];
}

void test_2()
{
	const int N = 5;
	Node *nodes[N];
	for (int i=0; i<N; ++i) nodes[i] = new Node(i);

	add_edge(nodes, 1, 2, 3);
	add_edge(nodes, 2, 4, 5);

    printf("Diameter is %d\n", diameter(nodes[0]));
	for (int i=0; i<N; ++i) delete nodes[i];
}

void test_3()
{
	const int N = 12;
	Node *nodes[N];
	for (int i=0; i<N; ++i) nodes[i] = new Node(i);

	add_edge(nodes, 1, 2, 7);
	add_edge(nodes, 2, 3, 4);
	add_edge(nodes, 4, 5, 6);

	add_edge(nodes, 7, 0, 8);
	add_edge(nodes, 8, 0, 9);
	add_edge(nodes, 9,10,12);
	add_edge(nodes,10, 0,11);

    printf("Diameter is %d\n", diameter(nodes[0]));
	for (int i=0; i<N; ++i) delete nodes[i];
}

void test_4()
{
	const int N = 13;
	Node *nodes[N];
	for (int i=0; i<N; ++i) nodes[i] = new Node(i);

	add_edge(nodes, 1, 2, 3);
	add_edge(nodes, 2, 4, 9);
	add_edge(nodes, 4, 5, 6);
	add_edge(nodes, 6, 7, 0);
	add_edge(nodes, 7, 0, 8);
	add_edge(nodes, 9, 0,10);
	add_edge(nodes,10,11,12);
	add_edge(nodes,12,13, 0);

    printf("Diameter is %d\n", diameter(nodes[0]));
	for (int i=0; i<N; ++i) delete nodes[i];
}

int main(){
	test_1();
	test_2();
	test_3();
	test_4();
    return 0;
}
