Title: Release 2.3.0
Date: 2012-04-19 10:20
Category: Releases
Author: RCE


### Changelog

* added optimizer component (currently for Windows only)
 	- Black-box optimization with Dakota
	- Currently supported algorithms: Quasi-Newton method, HOPSPACK Asynch Pattern Search, Coliny Evolutionary method (all of them single- and multi-objective) 
* improved "simple wrapper" component
	- added Jython as pre- and post-processing scripting language
	- added support for OS-independent and multiple commands 
* graphical user interface improvements
	- added shortcuts for copy, cut and paste (Crtl+C, Crtl+X, Ctrl+V) in Python editor and text areas
 	- made several operations asynchronous to improve responsiveness
	- added zoom to workflow editor
 	- added editing of workflow component input values
	- added information about number of component runs in mouse-over of workflow component
	- Python installation path is now reset properly after moving a workflow to another platform
	- added integrated help for components
	- added more user-friendly "properties" tab for parametric study component
	- improved Python component usage
	- added "Profiles" properties tab to enable switching between workflow component properties sets
	- removed verbose log output after update 
* raised timeouts to support long running communication between RCE instances
* improved the build/release/update process
	- made it possible to provide updates for third-party libraries
	- improved versioning to reduce update size
	- regrouped installable feature sets (for example, component groups)
	- improved p2 metadata generation
	- added support for independent RCE editions 