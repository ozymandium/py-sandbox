Boost.Python Examples
=====================

- currently only supports python 2.7.3
- make sure your library names agree whether built locally or via setup.py (which now works)

Building Locally by Hand
========================
Build this portion from a separate build folder. It is not yet installable via setup.py .
::

    cd boost_python && mkdir build && cd build
    cmake ..
    make
    cd .. && python yay.py