Title: Release 4.0.0 
Date: 2013-11-29 10:20
Category: Releases
Author: RCE


### GUI

* Added a wizard to simplify the creation of new workflows
* Extended Network view
	- Workflow components are shown per node (for own node: locally installed and published ones; for remote nodes: published ones)
	- Connections to other nodes are shown
	- Connections to others can be managed (added, edited, deleted, started, stopped) 
* Fixed issues regarding copy&paste of workflow components
* Fixed result view of Parametric Study component when it is opened multiple times
* Improved responsiveness of the graphical user interface by reworking long-lasting operations
* General improvements
 	- Fix configuration validation in Script component
	- Added additional context menus where applicable
	- Removed tool bar icons for workflow control as they didn't work reliably; may be added again in a future version
	- Removed unnecessary menu entries in the graphical user interface
	- Added button in placeholder page (in workflow execution wizard) to select a file from the file system if the placeholder represents a file system path
	- Added menu entry to switch between workspaces
 	- Added menu entry to restart RCE 

### Workflow Components 

* Added generic integration concept to integrate tools as workflow components
  	- Tools are integrated using a graphical wizard
 	- Newly integrated tools can immediately be made available ("published") to other users 
* Fixed constraints handling in Optimizer component for Dakota algorithms
* Made Converger component more robust against inputs that are received after convergence of component
* Restricted input types of Parametric Study component to floating point numbers and integers
* If script in Script component reads an input that is optional or required and which has no new value, an exception is thrown now
* Reworked Cluster component: inputs and outputs are directories, and multiple jobs can be submitted within one iteration 

### Workflow Engine 

* Added new data type "Directory"
* Reworked the way how values/data are sent from one workflow component to another to improve performance and adapt to the new multi-network feature (see below)
* Marked workflow components as deprecated if they are intended to be removed in future versions
* When workflow components (without result views) are finished, the hosting RCE node can now be shut down without breaking the workflow
* Fixed a memory leak that occurred during workflow component execution 

### Communication Layer  

* RCE nodes can now connect to multiple networks without creating a connection between them; previously, this caused all networks to merge into a single, larger network. The new behaviour gives network administrators better control of computing resources.
* Made network connections restartable (usable from Network View and command shell)
* Provided infrastructure for more efficient distribution of node information (for example, the list of published components)
* Improved handling of routing information
* Improved routing performance by reducing the number of re-calculations
* Fixed a server-side resource leak in the ActiveMQ network transport
* Added first draft of an SSH administration console 

### Others 

* Removed unnecessary files in installation folder of RCE (launcher(.exe), eclipsec.exe)
* Improved log messages (e.g. removed irrelevant stack traces, reviewed and reduced warnings)
* "rce.log" is now located in the main directory (previously in "configuration")
* Improved internal event handling
* Shortened path length of temporary files
* General tweaks, bugfixes and performance improvements 
