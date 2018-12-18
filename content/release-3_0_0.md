Title: Release 3.0.0
Date: 2013-08-02 10:20
Category: Releases
Author: RCE


### Changelog

* Added support for remote upload of large files
* Unified data types of input values and output values which are used by workflow components (Note: all workflow files created with RCE < 3.0.0 will be updated by RCE when opening them for the first time)
* Replace the Python workflow component with a more generic Script workflow component which supports still Python and and latterly also Jython
* Added check if two RCE instances are compatible to each other (connection between them will be refused if not compatible)
* Added support for maximum iteration count in Converger workflow component
* Reduced messages exchanged during workflow run
* Improved GUI
	- added icon in workflow runtime tab, which shows the current state of a workflow
	- Fixed memory leak in tab showing the input values of running workflow components
	- Reworked and improved most of the workflow component configuration GUIs
	- Improved the workflow run editor: it only allows RCE nodes to be selected which has the workflow component with an exact matching version installed
	- Added check for invalid connections: if data type of one connection's endpoint (input/output) is changed it will be checked now if it is compatible with the data type of the other endpoint
	- Made the GUI in general more responsive even if long running (remote) operations are performed in the underlying backend
	- More minor improvements 
