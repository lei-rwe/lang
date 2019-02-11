#include <iostream>
using namespace std;

class Foo {
public:
  Foo(int a, int b){
	  cout << "Foo()" << endl;
  }
  Foo(const Foo &f){
	  cout << "Foo(const Foo &)" << endl;
	  if (&f == this) return;
  }
  void some_method() {
	  cout << "Foo::some_method()" << endl;
  }
  ~Foo() {
	  cout << "~Foo()" << endl;
  }
};

void do_something_with(Foo& z)
{
	cout << "do_something_with" << endl;
}
Foo rbv()
{
  Foo y = Foo(42, 73);
  y.some_method();
  do_something_with(y);
  return y;
}
int main()
{
  Foo x = rbv();
}
