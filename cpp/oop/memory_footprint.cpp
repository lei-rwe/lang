#include <stdio.h>
class Base1 {
public:
    char a1[100];
    Base1(){       printf("Base1\n");  }
    void Hi1(){    printf("Base1::Hi1\n");  }
   ~Base1(){       printf("~Base1\n");  }
};

class Base2 {
public:
    char a2[100];
    Base2(){       printf("Base2\n");  }
    void Hi2(){    printf("Base2::Hi2\n");  }
   ~Base2(){       printf("~Base2\n");  }
};

class Base3 {
public:
    char a3[100];
    Base3(){       printf("Base3\n");  }
    void Hi3(){    printf("Base3::Hi3\n");  }
   ~Base3(){       printf("~Base3\n");  }
};

class Derived : public Base1, public Base2, public Base3 {
public:
    char a[100];
    void Hi(){    printf("Hi from Derived!\n");  }
};

int main()
{
    Derived * pDerived = new Derived;
    Base1 * pBase1 = (Base1 *)pDerived;
    pBase1->Hi1();
    Base2 * pBase2 = (Base2 *)pDerived;
    pBase2->Hi2();
    Base3 * pBase3 = (Base3 *)pDerived;
    pBase3->Hi3();

    delete pDerived;
}
