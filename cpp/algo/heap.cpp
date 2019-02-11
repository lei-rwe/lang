#include <iostream>
#include <algorithm>
#include <vector>
#include <random>
using namespace std;

template<class T>
class heap{
private:
	vector<T> &A;
public:
	heap(vector<T> &v) : A(v) {
		cout << "in heap" << endl;
	}
	int left(int n){ return 2*n + 1; }
	int right(int n){ return 2*n + 2; }
	int parent(int n){ return n > 0 ? (n-1)/2 : 0; }

	// Assume that the binary trees rooted at LEFT(i) and RIGHT(i)
	// are max-heaps, but A[i] might be smaller than its children
	// and thus violating the heap property
	// Time complexity: O(lgn)
	void max_heapify(int i, int heap_size){
	    int l = left(i);
	    int r = right(i);
	    int largest;
	    if (l < heap_size && A[l] > A[i])
	        largest = l;
	    else
	        largest = i;

	    if (r < heap_size && A[r] > A[largest])
	        largest = r;

	    if (largest != i){
	        swap(A[largest], A[i]);
	        max_heapify(largest, heap_size);
        }
	}

    // Time complexity: O(n)
    // Note here that O(nlgn) is not tight
    void build_max_heap(int heap_size){
        // Note leaves are already heapified
        for (int i=parent(A.size()-1); i>=0; --i){
            max_heapify(i, heap_size);
        }
    }

    void heapsort(){
        build_max_heap(A.size());
        for (int i=0; i<A.size(); ++i){
            swap(A[0], A[A.size()-1-i]);
            max_heapify(0, A.size()-1-i);
        }
    }


};

int main(int argc, char *argv[])
{
    // First create an instance of an engine.
    random_device rnd_device;

    // Specify the engine and distribution.
    mt19937 mersenne_engine {rnd_device()};  // Generates random integers
    uniform_int_distribution<int> dist {1, 52};

    auto gen = [&dist, &mersenne_engine](){
                   return dist(mersenne_engine);
               };

    vector<int> vec(10);
    generate(begin(vec), end(vec), gen);

    copy(vec.begin(), vec.end(), ostream_iterator<int>(cout, " "));
    cout << endl;

    (heap<int>(vec)).heapsort();

    copy(vec.begin(), vec.end(), ostream_iterator<int>(cout, " "));
    cout << endl;

}
