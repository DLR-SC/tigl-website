Title: Release 6.2.0 
Date: 2015-06-12 10:20
Category: Releases
Author: RCE

## Synopsis

* Improved usability of various graphical user elements including log messages
* Extended and improved the access of tools and workflows via SSH (remote access)
* Fixed minor bugs
* Internal improvements (e.g., improved quality assurance by increasing unit test coverage) 

### Usability

* Script component
	- Files and directories (received as input values) keep their name (affects e.g. the name shown in the workflow data browser)
	- Added support to show whitespace characters in the text field used to write the Python script 
* Tool integration dialog
	- Added support for editing values (inputs, outputs, properties etc.) on double click
	- Added dialog which helps to create Python commands to copy files or directories within the pre or post execution script 
* Workflow data browser
	- The host instance of each workflow component is now shown
	- Added possibility to open CPACS files in the TiGL viewer from the workflow data browser's context menu 
* Workflow list
	- Workflows can be deleted now with the Del key
	- Fixed default sorting (now by time) 
* Command console: added feature to clear command console line on Esc
* Workflow console: added possibility to copy either a whole console line or just the message itself
* Announce syntax errors in the main configuration file of RCE at start up
* Workflow execution
	- Improved warning shown in the workflow execution dialog if workflow components are not available or only available with other versions (which prevents the user from executing a workflow at all)
	- Improved warning when component versions of workflow file and current installation don't match
	- Added the new placeholders "${profileName}" and "${version}" to instance name configuration; this is intended to simplify deployments with many instances 

### Remote Access (access of tools and workflows via SSH) 

* Workflows published with the "ra-admin publish-wf" command are now persistent by default (ie, they are still available after restarting the RCE instance)
* Tools on the RCE instance running the SSH server must now be explicitly published to be available
* Clients can now explicitly select the instance of a tool that is available on multiple RCE instances
* Filtered the "list-tools" output to tools that actually match the Remote Access requirements
* The client's tool selection is now checked against the published/available tools before execution; before this, invalid values simply caused the generated workflow to fail
* Improved error handling and feedback messages 

### Bug Fixes 

* Joiner component: fixed the configuration GUI of the joiner component so that its elements are applied correctly after undo or redo
* Command console: Fixed pasting from clipboard into the command console on linux systems (fixed delay and issue with line break)
* Fixed writing integer values to outputs of type float in script component and post script of integrated tools
* Workflow data browser: fixed exporting directories from the workflow data browser
* Files and projects can be deleted from workspace projects now even if they were opened beforehand
* Workflow editor: workflow components, which are not available, can be now copied/cutted and pasted as they were be available
* Fixed resource leaks in workflow data browser and workflow timeline view
* Workflow engine: constant inputs of loop driver components (e.g. Optimizer, DOE, ... ) are now reset if loop was reset (mainly affects loop drivers of nested loops) 

### Internal Improvements 

* Improved quality assurance by increasing unit test coverage
* Refactor the code base responsible for loading, mapping, and saving XML files
