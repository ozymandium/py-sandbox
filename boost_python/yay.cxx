#ifndef _YAY
#define _YAY
// c++ source
char const* yay() { return "Yay!"; }

struct World{
    void set(std::string msg) { this->msg = msg; }
    std::string greet() { return msg; }
    std::string msg;
};

class WorldClass {
public:
    WorldClass() { this->msg = "Yay for classes!"; }
    ~WorldClass() { std::cout << "Goodbye!\n"; }
    void set(std::string msg) { this->msg = msg; }
    std::string greet() { return msg; }
// private:
    std::string msg;
};

#endif

// make a python interface
#include <boost/python.hpp>
BOOST_PYTHON_MODULE(libyay) // this name is what you will import
{   using namespace boost::python;
    
    def("yay", yay);

    class_<World>("World")
        .def("greet", &World::greet)
        .def("set", &World::set)
    ;
    
    class_<WorldClass>("WorldClass")
        .def("greet", &WorldClass::greet)
        .def("set", &WorldClass::set)
    ;
}
