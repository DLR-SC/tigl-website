Title: Release 6.3.0 
Date: 2015-07-29 10:20
Category: Releases
Author: RCE

## Synopsis

* This release fixes a security issue; users that run components on untrusted machines should upgrade to 6.3.0 as soon as possible
* Various minor bugfixes and improvements
* Workflow Data Browser: Added icons to the top-level workflow entries that show the final state of workflows 

### Components

* XML Merger: Added input handling "queue" to static input "XML to integrate"
* Design of Experiments: Improved cleanup of temp directories
* Design of Experiments: The component can now be used in outer loops
* Design of Experiments: Improved validation
* Input Provider: Fixed selection of files and folders in imported projects or projects located outside the workspace
* CPACS Writer: Improved cleanup of temp directories

### Workflow Data Browser

* Added icons to the top-level workflow entries that show the final state of finished workflows; running workflows keep the default workflow icon
* Fixed saving of execution log files in case of an error
* Fixed working directory to be shown for CPACS components

### Tool Integration

* Added a file containing the running workflow's name to the working directory of tools ("rce-workflow-information.txt")
* Fixed "Run only on changed inputs" option
* Fixed path for directory inputs when using placeholder variables


### Security

* This release fixes a security issue; users that run components on untrusted machines should upgrade to 6.3.0 as soon as possible

### Console Commands

* The output of "wf run" now includes the workflow id needed for other commands
* Added a <code>"--compact-output"</code> flag to "wf run" to simplify scripted usage

### Remote Access

* Made a minor protocol change that allows consistent behavior for Debian 7 clients

### Internal

* Increased the heap size setting for RCE instances running on 32-bit Java by 20%
* Various minor bugfixes and improvements
* Reduced debug log output volume to make it easier to inspect