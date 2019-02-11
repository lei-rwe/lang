/** https://eli.thegreenplace.net/2012/06/20/c11-using-unique_ptr-with-standard-library-containers
Basic capabilities

To put it simply, unique_ptr should be the default smart pointer
used by new C++ code, replacing "raw" pointers as much as possible.
unique_ptr cleanly represents the single ownership idiom - it cannot
be copied and assigned, and it cleans up the pointed object when
it's destructed.

Here's some code to demonstrate this [1]:
*/
#include <iostream>
#include <cstdlib>
#include <memory>
using namespace std;

struct Foo {
    Foo() {cerr << "Foo [" << this << "] constructed\n";}
    virtual ~Foo() {cerr << "Foo [" << this << "] destructed\n";}
};

int main(int argc, char** argv) {

    // .. some code
    {
        unique_ptr<Foo> fp(new Foo());

        // unique_ptr<Foo> fp2(fp);    // ERROR! can't copy unique_ptr
        unique_ptr<Foo> fp3;
        // fp3 = fp;                   // ERROR! can't assign unique_ptr

        cerr << "Exiting scope\n";
    } // fp will be destroyed, and will destruct the pointed object

    return 0;
}
