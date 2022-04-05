#include <string>
#include <iostream>

//!  A test class. 
/*!
  A more elaborate class description.
*/
class Base
{
public:

    //! A constructor.
    /*!
      A more elaborate description of the constructor.
      \param InName name of class instance.
    */
    Base(std::string InName);
    
    //! A normal member taking two arguments and returning an integer value.
    /*!
      \param a an integer argument.
      \param s a constant character pointer.
      \return The test results
      \sa QTstyle_Test(), ~QTstyle_Test(), testMeToo() and publicVar()
    */
    virtual void print();
protected:
    std::string _name; /*! name of the class. */
};

class Derived : public Base
{
public:
    Derived(std::string InName);
    //! A normal member taking two arguments and returning an integer value in derived.
    /*!
      \param a an integer argument.
      \param s a constant character pointer.
      \return The test results
      \sa QTstyle_Test(), ~QTstyle_Test(), testMeToo() and publicVar()
    */
    virtual void print() override;
};