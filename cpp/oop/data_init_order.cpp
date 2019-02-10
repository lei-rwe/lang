#include <cstddef>
#include <iostream>
#include <vector>
using namespace std;

class C {
	int a1;
	int a2;
public:
	C() : a2(10), a1(a2) {}   // Compile warning: a2 is uninitialized
    void print(){
    	cout << "a1=" << a1 << ", a2=" << a2 << endl;
    }
};
void test_C(){
	C c;
	c.print();
}

//==================================================
class X{
private:
	int x = 0;
public:
	X(){ cout << "X()" << endl; }   // default constructor
	X(int a) : x(a) { cout << "X(int a)" << endl; }
	friend class A;
};

class A{
private:
	X x;   // default initializer
	int a;
public:
	A();
	~A() { cout << "~A(): " << x.x << endl; }
};
A::A() : a(5), x(a) {}   // Compile warning: a is uninitialized
void test_A(){   A a;   }

//==================================================
template<class T>
class Array {
private:
	vector<T> data;     // the array data is stored in a vector object
    int lBound, hBound; // lower bound, higher bound
public:
    Array(int lowBound, int highBound);
    int size() { return data.size(); }
};
template<class T>
Array<T>::Array(int lowBound, int highBound)
: lBound(lowBound), hBound(highBound),
  data(highBound - lowBound + 1)  // Why no compile warning here?
{}

void test_Array(){
	Array<int> a(10, 20);
	cout << a.size() << endl;     // This always prints "11"
}

//======================================================
//==== constructor  initializer supersedes the default
class Y{
private:
	int y = 0;
public:
	Y() { cout << "Y()" << endl; }
	Y(int a) : y(a) {
		cout << "Y(int a)" << endl;
	}
	friend class B;
};

class B{
private:
	Y y;   // default initializer will NOT be used if in I-list
public:
	B();
	~B() { cout << "~B(): " << y.y << endl; }
};
B::B() : y(5) {}
void test_Y(){   B b;   }

int main(){  test_Y();  }
