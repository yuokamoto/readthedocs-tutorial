#include <sample_class.hpp>

int main()
{
    std::cout << "Hello, world" << std::endl;

    Base base("base class");
    base.print();

    Derived derived("derived class");
    derived.print();
}