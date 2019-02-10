#include <iostream>
using namespace std;

/**
 * C++ follow the ANSI C in defining integral promotions
 * as “value-preserving”. But many Classic C compilers
 * use “unsigned-preserving” integral promotions, which
 * breaks in the following example
 *
 */
void signed_int(){
	cout << "In signed_int()" << endl;
	int i=-1;
	unsigned short us = 2;
	int k = (i + us) < 42;
	cout << k << endl;
}

/**
 * base class pointer and reference can be used to access
 * derived class object: this is NOT implicit type conversion
 */
class base {
public:
	virtual void foo(){
		cout << "base::foo" << endl;
	}
};

class derived : public base{
public:
	explicit derived(){
		cout << "explicit derived" << endl;
	}
	void foo(){
		cout << "derived::foo" << endl;
	}
};

void cls_conv(base &b){
	b.foo();
}

/**
 * Define implicit type conversion using constructor or type conversion operator
 */

class X{
public:
	explicit X(){ cout << "X" << endl; }
};
class Y{
public:
	explicit Y(X){ cout << "Y(X)" << endl; }
};
class Z{
public:
	Z(X){ cout << "Z(X)" << endl; }
};

int main(){
	signed_int();

	base b;
	derived d;
	cls_conv(d);

	X x;
	// Y y = x;  // This does not compile coz Y(X) is explicit
	Z z = x;
}
