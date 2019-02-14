#include <iostream>

using namespace std;

class collar {
public:
    collar() { cout << "collar: " << endl; }
    // Note: if change above constructor to
    // collar(int) { .... }
    // It won't compile

    ~collar() { cout << "~collar: " << endl; }
};

class Dog {
public:
    collar m_collar;
    string name;
    Dog(string name="Bob") : name (name) { cout << "Dog " << name << " is born" << endl; }
    ~Dog() { cout << "~Dog: " << name << endl; }
};

int main()
{
    Dog a("Henry");
    Dog d;
    d = a;
    return 0;
}

/** Output

collar:
Dog Henry is born
collar:
Dog Bob is born
~Dog: Henry
~collar:
~Dog: Henry
~collar:

 */
