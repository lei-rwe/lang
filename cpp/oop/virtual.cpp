/**
 * Basics about virtual functions
 * 1. A virtual function is a member function that you expect to be redefined (overridden) in derived classes.
 *    (https://docs.microsoft.com/en-us/cpp/cpp/virtual-functions?view=vs-2017)
 * 2. Declared with "virtual" keyword in base class
 * 3. Mainly to achieve "runtime polymorphsm", to ensure correct functions are called regardless of
 *    the type of reference (or pointer) used for the function call.
 *
 * 4. Must be public
 * 5. Cannot be static
 * 6. cannot be a friend function of another class.
 * 7. Should be accessed using pointer or reference of base class type to achieve run time polymorphism.
 * 8. The prototype (signature) of virtual functions should be same in base and derived class.
 * 9. Not mandatory for derived class to override, in that case base class version of function is used.
 * 10. A class may have virtual destructor but it cannot have a virtual constructor.
 *
 */
#include <iostream>
using namespace std;

class animal
{
    public:
        animal(){
            cout << "animal" << endl;
        }
        virtual void eat(){
            cout << "animal::eat" << endl;
        }
        virtual void cleanup() = 0;
        virtual ~animal(){
            cout << "~animal" << endl;
        }
};

class dog : public animal{
    public:
        dog(){
            cout << "dog" << endl;
        }
        void eat(){
            animal::eat();
            cout << "dog::eat" << endl;
        }
        void cleanup(){
            cout << "dog::cleanup" << endl;
        }
        ~dog(){
            cout << "~dog" << endl;
        }
};

int main()
{
    dog d;
    d.eat();
    d.animal::eat();
}
