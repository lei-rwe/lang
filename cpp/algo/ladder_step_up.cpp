#include <iostream>
using namespace std;

/**
void p(int n)
{
    if ( n==0 ) { cout << endl; return; }
    if ( n==1 ) { cout << 1 << endl; return; }

    cout << 1 << ' ';
    p(n-1);

    cout << 2 << ' ';
    p(n-2);
}
*/

void p(int n, int level, int A[])
{
    if ( n==0 ) {
        for (int i=0; i<level; ++i) cout << A[i] << ' ';
        cout << endl;
        return;
    }
    if ( n==1 ) {
        for (int i=0; i<level; ++i) cout << A[i] << ' ';
        cout << 1 << endl;
        return;
    }

    A[level] = 1;
    p(n-1, level+1, A);

    A[level] = 2;
    p(n-2, level+1, A);
}

int main(){
	const int N=4;
	int A[N];
	p(N, 0, A);
}
