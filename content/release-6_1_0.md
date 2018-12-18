Title: Release 6.1.0 
Date: 2015-04-16 10:20
Category: Releases
Author: RCE


### Workflow Components 

* Added new component: Switch 
	- Directs data on the base of a condition to one of two outputs 
* Added new component: Design of Experiments (DOE) 
	- Supports sampling of a bounded solution space 
* Converger: Replaced "maximum iterations" by "maximum convergence checks" 
* Parametric Study: Added option "fit to bounds"
* Optimizer 
	- Added support for mixed integer optimization 
	- Integrated new algorithm method called NOMAD, which is more applicable for mixed integer optimization 

### Tool Integration 

* Extended options for the deletion of working directories: they can be kept in the case of an error now
* Pre and post processing scripts now have the "shutil" module imported by default to simplify file and directory copying
* Enabled tabbing through the "Tool Description" page of the tool integration wizard 

### Workflow Editor

* Added possibility to define custom connection paths
* Added support for workflow labels 

### Workflow Data Browser 

* Improved performance when fetching the list of workflows and when expanding timelines
* Fixed an error in the graphical tree view which sometimes occured when deleting workflows ("Comparison method violates contract")
* Fixed an error which allowed running workflows to be deleted under certain circumstances 

### Workflow Data Management 

* Improved stability and performance (especially for workflows with a high number of component runs - in the order of >10,000 runs) 

### GUI Miscellaneous 

* Improved the performance of the workflow list view (workflows and their states were updated very slowly from remote workflow hosts)
* Changed the font (Courier) for the command console and script editing areas (the Script component's editor and the tool integration wizard's pre and post processing pages)
* Fixed layout of the input table of the OutputWriter component
* Validation of workflow components' configuration is now only done when saving the workflow; this improves GUI performance
* Validation errors and/or warnings are now checked at workflow start again and are shown to the user with a popup dialog
* Workflow execution wizards shows the actual instance names as they appear in the network view
* The "Apply to all" button in the placeholder page of the workflow execution wizard copies the placeholder only to other placeholders of the same data type and the same component type now
* Improved the insert locations of pasted workflow nodes; prevented the case where inserted components have the same position, which made them hard to tell apart
* Connection Editor: Inputs which are required but not connected yet are marked with a red asterisk 

### Remote Access  

* Added a command to only list components that are compatible with the "run-tool" requirements
* Made command output easier to parse by client code (used by upcoming C/C++ API)
* Added a default version ("1") to published workflows so "run-wf" and "run-tool" can use the same API calls 

### Console Commands 

* Added console commands to pause, resume, cancel, and dispose workflows
* Added console command to list all active workflows (wf list) 

### Configuration

* Changed the embedded SSH server's "host" parameter to "ip" for clarity ("host" still works, but a warning is logged)
* Fixed some configuration documentation issues 

### Deployment

* Provided 32-bit .deb packages (in addition to existing 64-bit packages) 

### Documentation

* Added documentation for concept behind the CPACS mapping of integrated CPACS-capable tools 

### CPACS

* Updated namespace for map in cpacs mapping files (old one still works, but a warning is logged) 

### Miscellaneous

* Disabled the "<profile>/output/console.combined.*.log" files to conserve disk space; if you were using them, please contact us for discussion of this feature
* Removed irrelevant stack traces to reduce log volume
* Improved log output of network error situations
* Added "--profile" option as an alternative/alias to "-p"
* Fixed the profile directory's name not being used for the temp directory prefix (was always "default")
* Cleaned up the command console's "help" output
* Script component (Jython) now sends unique NaV values to the affected outputs within one run
* A workflow component, which triggers that a workflow is finished, doesn't forward the finish information anymore (this led to warnings in the log)
* Reduced callback attempts of a workflow component if its workflow controller is not reachable anymore; reduced number of error messages in the log
* Increased the automated test coverage (especially, workflow engine, data management, workflow components)
* Generation of "Output/autoExportOnStartup.json" is now optional (default: off) 


