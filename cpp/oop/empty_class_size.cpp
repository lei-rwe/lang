#include <iostream>
using namespace std;

class Empty {};
class A : public Empty {int a;};
class D : public Empty {};

class Derived1 : public Empty {};
class Derived2 : virtual public Empty {};
class Derived3 : public Empty {
    char c;
};
class Derived4 : virtual public Empty {
    char c;
};
class Dummy {
    char c;
};

int main(){
    cout << "sizeof(Empty) " << sizeof(Empty) << endl;         // 1
    cout << "sizeof(Derived1) " << sizeof(Derived1) << endl;   // 1
    cout << "sizeof(Derived2) " << sizeof(Derived2) << endl;   // 8
    cout << "sizeof(Derived3) " << sizeof(Derived3) << endl;   // 1
    cout << "sizeof(Derived4) " << sizeof(Derived4) << endl;   // 16
    cout << "sizeof(Dummy) " << sizeof(Dummy) << endl;         // 1

	cout << sizeof(A) << endl;      // 4
	cout << sizeof(D) << endl;      // 1

	Empty a, b;
	cout << "&a == &b value: " << (&a == &b) << endl;  // 0

	cout << ((new Empty) == (new Empty)) << endl;      // 0
}
