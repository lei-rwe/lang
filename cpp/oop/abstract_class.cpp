#include <iostream>
using namespace std;

class animal {
private:
	int id;
public:
    animal(){
        cout << "animal" << endl;
    }
    virtual void eat(){
        cout << "animal::eat" << endl;
    }
    virtual ~animal() = 0;
};
animal::~animal() {
    cout << "~animal" << endl;
}

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

void foo(animal &a){
	cout << "foo(animal &a)" << endl;
}
int main()
{
    dog d;
    d.eat();
    d.animal::eat();
}
