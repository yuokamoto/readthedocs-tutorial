#include <sample_class.hpp>

Base::Base(std::string InName):_name(InName)
{}
void Base::print()
{
    std::cout << _name << std::endl;
}

Derived::Derived(std::string InName):Base(InName)
{}
void Derived::print()
{
    Base::print();
    std::cout << "drived: " << _name << std::endl;
}