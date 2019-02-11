#include <iostream>
using namespace std;

class Base {
public:
    Base() { cout << "Base" << endl; }
};

class VDer1 : public virtual Base {
public:
    VDer1() { cout << "Der1" << endl; }
};

class VDer2 : public virtual Base {
public:
    VDer2() { cout << "Der2" << endl; }
};

class Der1 : public Base {
public:
    Der1() { cout << "Der1" << endl; }
};

class Der2 : public Base {
public:
    Der2() { cout << "Der2" << endl; }
};

class Join_1: public VDer1, public VDer2 {
public:
    Join_1() { cout << "Join_1" << endl; }
};

class Join_2: public VDer1, public Der2 {
public:
    Join_2() { cout << "Join_2" << endl; }
};

class Join_3: public Der1, public VDer2 {
public:
    Join_3() { cout << "Join_3" << endl; }
};

class Join_4: public Der1, public Der2 {
public:
    Join_4() { cout << "Join_4" << endl; }
};

int main(){
    cout << "==============" << endl;
    Der1 d1;
    cout << "==============" << endl;
    VDer1 vd1;
    cout << "==============" << endl;
    Join_1 j1;
    cout << "==============" << endl;
    Join_2 j2;
    cout << "==============" << endl;
    Join_3 j3;
    cout << "==============" << endl;
    Join_4 j4;
}
