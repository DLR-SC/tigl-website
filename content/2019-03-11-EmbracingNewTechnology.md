Title: Embracing new technology - Abandon python 2 support and pre C++11 compilers
Date: 2019-03-11 12:03
Category: News
Author: Martin Siggel

During the TiGL development, we tried to make TiGL backwards compatible as much as possible.
This includes the support for old systems with old compilers, support for Qt 4 and Python 2.7.

C++ 11 opens up many new programming paradigms that we don't want to miss anymore.
Many of them will improve the quality of the TiGL source code, such as ```std::unique_pointer```,
lambda functions... to name just a few. Since C++ 11 is not exactly new anymore (8 years old), it is
time to move on. This will affect the systems of which TiGL runs. The minimum requirements are now

 - GCC 4.8
 - Visual C++ 2013
 
The choice of the C++ version also affects directly TiGL's Python support. On Windows,
Python 2.7 extensions have to be compiled with Visual C 2008, which is not compatible with C++ 11.
Therefore, we won't be able to provide Python 2.7 extensions for Windows with a C++ 11 based source code.
Since Python 2.7 will [retire in 2020](https://pythonclock.org/), it is now the right time to abandon Python 2 support.
TiGL will still be available from Python 3!

#### TLDR ####
 - TiGL 3 will now use C++11 code
 - No support for VC 2008 and GCC < 4.8
 - No support for Python 2.7 anymore 