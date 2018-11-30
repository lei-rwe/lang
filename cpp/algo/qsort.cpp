#include <iostream>
#include <algorithm>
using namespace std;

int partition(int A[], int p, int r)
{
    int x = A[r];
    int i = p - 1;
    for (int j = p; j < r; ++j){
        if (A[j] < x){
            ++i;
            swap(A[i], A[j]);
        }
    }
    ++i;
    swap(A[i], A[r]);
    return i;
}

void qsort(int A[], int p, int r)
{
    if ( p < r ){
        int q = partition(A, p, r);
        qsort(A, p, q - 1);
        qsort(A, q + 1, r);
    }
}

int main(int argc, char *argv[])
{
    cout << "Hello world!" << endl;
    int A[] = {3, 1, 4, 7, 4, 3, 10, 9, 4};
    qsort(A, 0, 8);
    for (int i=0; i<9; ++i){
        cout << A[i] << ", ";
    }
    cout << endl;
}

