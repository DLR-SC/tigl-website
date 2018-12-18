Title: Release 2.4.0
Date: 2012-12-17 10:20
Category: Releases
Author: RCE


### Changelog

* Major rework of the network/communication system; changes include:
	- significant performance improvements
	- simplified setup of ad-hoc networks; in typical use cases, clients only a single line of configuration to connect to a network
	- simplified handling of firewalled systems and subnets 
* reduced supported languages to English to avoid language mixups with third-party software
* added sample project with example workflows
* improved validation of Excel component configuration
* improved error handling in Python component if an unsupported Python installation was chosen
* improvements in graphical user interface of RCE (zooming behavior, graph plotting in Optimizer and Parametric Study component, etc.)
* cleaned up graphical user interface on very first start of RCE
* fixed "Simple Wrapper" execution under Linux when using multi-line command configurations created on Windows
* fixed handling of multiple arrays in Python component 