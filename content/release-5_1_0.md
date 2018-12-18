Title: Release 5.1.0 
Date: 2014-07-25 10:20
Category: Releases
Author: RCE


### GUI

* Added a view to execute RCE console commands
* Added miscellaneous context menu entries for faster access to key features (such as integrating a new tool or creating the workflow examples project)
* Fixed short cut for renaming workflow nodes (it is just F2 now)
* Improved visibility of self-connections of components in the workflow editor
* Component names are shortened from the center if the entire name is too long to fit in the workflow node box
* Further improved the GUI's responsiveness, especially when RCE is connected to remote instances
* Placeholders (such as Python installation path, cluster component credentials) are not shared between copied workflow files anymore
* Various bug fixes 

### Workflow components 

* Cluster component 
	- Absolute paths to the cluster queuing system commands are now configurable 
	- Added support for indicating failed cluster jobs 
* Converger component 
	- The number of iterations to consider in the convergence check is now configurable (not only the current and previous, but the current and n previous values can be considered now)  
* Optimizer component  
	- Starts dispatching initial design variable values for evaluation not before it gets the first explicit evaluation request from the optimization algorithm 

### Tool integration 

* Tools can be published and unpublished on the file-system level without restarting RCE (especially useful for non-GUI server nodes) 
* Miscellaneous improvements 

### Command interface 

* The "wf run" command can now be used to run workflow files containing placeholders (Python path etc.) as well; this is done by specifying a JSON file containing the required placeholder values
* Added the "wf verify" command for batch testing of workflow files; placeholder files are supported as with the "wf run" command 

### Administration 

* When installing RCE as a Linux daemon, the RCE instance can now be run as a non-root user (which is highly recommended); note that the installation process still requires root permissions
* Added a startup check to detect missing temporary folder permissions early 

### Network

* Active connection attempts can now be cancelled by pressing "stop/disconnect" in the Network View, or by using the "cn stop" console command
* Failed connections waiting to auto-reconnect can now be made to reconnect immediately (without stopping them first) by pressing "start/connect" in the Network View, or by using the "cn stop" console command 

### Remote access / Tool Access 

* In addition to the remote execution of single tools, complete workflows can now be invoked through the SSH/SCP interface 

### Documentation

* Added contextual help for all workflow components
* Removed the standard Eclipse platform's help content from the integrated help center and replaced it with information about RCE's user guide
* Extended the user guide with help for integrating tools in RCE 
