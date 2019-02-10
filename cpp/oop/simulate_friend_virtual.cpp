#include <iostream>
using namespace std;

class base {
public:
    friend ostream& operator << (ostream& o, const base& b);
protected:
    virtual void print(ostream& out) const
    { out << "virtual base::print"; }
};

class derived : public base{
public:
    virtual void print(ostream& out) const
    { out << "virtual derived::print"; }
};

std::ostream& operator<<(std::ostream& os, const base& b ){
     b.print(os);
     return os;
}

int main(){
    derived d;
    std::cout << d << std::endl;

    return 0;
}
