Title: Release 5.0.0 
Date: 2014-05-15 10:20
Category: Releases
Author: RCE


### Workflow components 

* Added an "Output Writer" component to write directories and files to the local file system 
* Optimizer
	- The iteration count is now available as an output
	- Added support for the Vector data type (to support multiple (hundreds) of design variables)
	- Added support for start values and optimal solution outputs
	- Gradients variables can be set as goals in Dakota
	- Added support for nested loops 
* Script
	- Added support for Vector and Matrix data types
	- Added support for history data (shown in the workflow data browser)
	- Fixed memory leaks related to frequent script execution 
* Tool integration
	- Added support for history data (shown in the workflow data browser)
	- Added support for hot deployment of configuration.json files (i.e., if a new tool configuration is dropped at the proper place, the tool will be considered and integrated immediately without any further user interaction. Especially useful for RCE server instances without a GUI)
	- Bugfix: All console output is now properly separated in the workflow console view 
* Renamed component: Merger -> Joiner
* Replaced/improved some component icons
* Simplified the identifiers of components (the ones which are used in the .json files to configure which of the components are published)
* Improved the ToolAccess interface that allows external (non-RCE) clients to execute integrated tools via SSH/SCP 
* Various bugfixes and performance improvements 

### GUI

* Improved the responsivness of the graphical user interface, especially in distributed setups under high load
* Workflow editor
	- Connections are now properly handled when workflow nodes are copied and pasted
	- Introduced different sizes and shapes for workflow components in the editor
	- Removed the "Advanced" configuration tab as it is not intended (and therefore confusing) for end users
        Added support for a "point&click" method to connect component's endpoints (in addition to the existing "drag&drop" method) 
* Workflow data browser
 	- The storage location of history data is now visible in the browser
 	- Component history entries now use the component's icon for easier recognition
	- Sorting is now context sensitive (e.g., no support for alphabetical sortinng in timeline subtree)
	- When exporting, all history data is now properly fetched recursively, even if it was not made visible before
	- Updated the internal history data format for better long-term stability 
* Improved the iteration counter for components in the workflow execution view 
* Various graphical user interface improvements 

### Documentation

* Added information about supported operating systems
* Added information about the scheduling parameters: required, initial, optional
* Added documentation of the ToolAccess feature
* General improvements 

### Configuration and administration  

* Switched to Java 7 (i.e., Java 7 or higher is required to execute RCE 5.0.0 and above)
* Added a separate log file that only lists warnings and errors (warnings.log)
* The location of the instance data directory (including the data management's storage) can now be freely configured; it is no longer restricted to be inside "<user home>/.rce" 

