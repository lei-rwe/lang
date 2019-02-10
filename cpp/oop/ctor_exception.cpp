#include <iostream>
#include <exception>
using namespace std;

class X{
public:
    X(){ cout << "X" << endl; }
   ~X(){ cout << "~X" << endl; }
};
class Y{
public:
    Y(){ cout << "Y" << endl; }
   ~Y(){ cout << "~Y" << endl; }
};
class Z{
public:
    Z(){ throw 20; }
   ~Z(){ cout << "~Z" << endl; }
};

class A{
	X x;
	Z z;
	Y y;
};
int main()
{
	try{
		A a;
	}catch(...){}
}
