/*
 * Believe it or not, when Der1::foo() calls this->bar(),
 * it ends up calling Der2::bar().
 * Yes, that's right: a class that Der1 knows nothing about
 * will supply the override of a virtual function invoked by Der1::foo().
 * This "cross delegation" can be a powerful technique
 * for customizing the behavior of polymorphic classes.
 */
#include <iostream>
using namespace std;

class Base {
public:
    virtual void foo() = 0;
    virtual void bar() = 0;
};

class Der1: public virtual Base {
public:
    void foo(){ bar(); }
};

class Der2: public virtual Base {
public:
    void bar(){ cout << "Der2::bar" << endl;}
};

class Join: public Der1, public Der2 {};

int main()
{
    Join* p1 = new Join();
    Der1* p2 = p1;
    Base* p3 = p1;

    p1->foo();
    p2->foo();
    p3->foo();
}
