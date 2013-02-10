Boost.Python Examples
=====================

- currently only supports python 2.7.3
- This directory invisible to the rest of the sandbox, serves as an example only

Building
========
Build this portion from a separate build folder. It is not yet installable via setup.py .
::

    cd boost_python && mkdir build && cd build
    cmake ..
    make
    cd .. && python yay.py