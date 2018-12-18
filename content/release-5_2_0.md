Title: Release 5.2.0 
Date: 2014-08-25 10:20
Category: Releases
Author: RCE


### General

* Improved clean up of RCE's temp directory 

### GUI 

* General performance improvement in workflow data browser
* Fixed handling of scripts that were openend in an editor at the same time and that belong to different script components 

### Workflow components 

* Optimizer component
	- Improved behavior if optimizer fails or isn't available at all 
* Script component
	- Improved error handling if non-existing files are written to an output 

### Tool integration 

* Fixed bug using boolean values in pre/post script
* Added support for relative paths to the tool directory (relative to the RCE installation directory) 

### Network

* Fixed a bug where many crashed connections could cause a high number of remaining threads and could also cause a memory leak 

### Headless RCE 

* Added new command for batch execution. It executes a set of commands and shuts down RCE no matter what: --batch <command string>
* Added support for placeholder values on component instance base (and not only on component type base)
* Improved fault tolerance when execution a workflow in batch mode and not all of the required remote nodes exists immediately on start up because of network latency (but will be available directly after start up) 

### Documentation

* Improved documentation of string security filter
* Added documentation for placeholder value files used in headless mode 
