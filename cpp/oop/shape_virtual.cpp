// shape_virtual.cpp
#include <iostream>
using namespace std;

class Shape {
protected:
    const char *_name;
    float _area;
public:
    Shape(const char *name) : _name("Shape"){}
    virtual float area(void) = 0;
    virtual void print_name(void);
};

void Shape::print_name(void){
    cout << _name << endl;
}

class Rectangle : public Shape{
private:
    float _width;
    float _height;
public:
    Rectangle(float width, float height)
        : _name("Rectangle"),
        _width(width), _height(height){}
    float area(void){
        _area = _width * _height;
    }
