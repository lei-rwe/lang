#include <iostream>
using namespace std;

const int M = 10;
int global_array[M];

class myclass{
private:
	static const int N = 100;
	int array[myclass::N];
public:
	myclass(int N){
		cout << "constructor" << endl;
	}
	~myclass(){
		cout << "destructor" << endl;
	}
};

int main(){
	myclass a(10);
}
