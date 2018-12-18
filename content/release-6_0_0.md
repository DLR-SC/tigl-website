Title: Release 6.0.0 
Date: 2015-01-15 10:20
Category: Releases
Author: RCE

### Workflow Editor

* Components in a workflow can now be temporarily disabled: during workflow execution, these components and all their connections are treated as if they didn't exist
* Added an option to show the number of connections represented by a line between two components
* The connection editor dialog can now be opened by double-clicking a connection line, too
* Added shortcuts for "Draw Connection" mode (ALT + D) and "Selection" mode (ALT + S) 

### Connection Editor 

* Improved handling of workflows with many connections
* Inputs which are already connected to an output are now marked by a small arrow
* Added more filtering options for inputs and outputs (match exactly, start with, contain) 

### Workflow List 

* Pause/Resume/Cancel/Dispose can now be applied to multiple workflows at once 

### Timeline GUI 

* Added new feature that visualizes when each component was running during workflow execution 

### Configuration

* Merged all previous configuration files (*.json) into a single file (configuration.json)
* Added option to open and edit this configuration file within the GUI (Help -> Open Configuration File)
* Made example configurations and path information accessible from the GUI (Help -> Open Configuration Information)
* Moved example configuration files to the easier-to-find "examples/configuration" folder
* The "instanceName" configuration entry now supports the placeholders ${systemUser} and ${hostName} for better default naming of RCE instances
* Added "connectOnStartup" option to network connections; the old behavior was to always connect when RCE starts, which is now optional 

### Multi-User Support  

* Added full support for multi-user operation, i.e. one RCE installation can be used by multiple users on the same system; the RCE installation directory can be set to "read-only" for all users
* Added support for multiple profiles per user, each with its own configuration, log files, and data storage
* On Linux, temporary file directories are now automatically separated (/tmp/rce-temp-<user id>) to prevent file ownership and permission problems; when customizing this path, the placeholder ${systemUser} is available 

### Installation and Release Signing 

* Provided .deb packages for Debian/Ubuntu/Mint
* Provided .rpm packages for CentOS/Red Hat/SUSE
* Provided a signed APT repository for Linux Debian/Ubuntu/Mint which allows installation via "apt-get" or package managers with GUI (e.g. Synaptic), as well as full integration with automatic system updates
* All .zip, .deb, and .rpm release packages now have digitally signed checksum files (SHA256SUMS.asc) 

### Linux Support 

* Completely reworked (and simplified) Linux daemon installation and handling ("rce-daemon" command)
* Improved Linux distribution compatibility; RCE is now regularly tested on Debian 7, SUSE 11 SP 2, and CentOS 7 (all 64 bit); it is also confirmed to run on Ubuntu 12 LTS, Ubuntu 14 LTS, Mint 17, and Red Hat Enterprise 6
* Added standard Linux desktop integration (application icon and basic menu entry) 

### Remote Tool/Workflow Access 

* Added a Remote Workflow Access template, which can also be used for out-of-the box testing
* Simplified the handling of input and output directories; when accessing them from script code, no additional sub-directory levels ("/input/") are required anymore
* Moved example script files to the easier-to-find "examples/remote_access" folder 

### Optimizer Component 

* Added an output that indicates whether gradients are requested by the optimizer method within the current iteration
* Updated integrated Dakota version from 5.1 to 6.0
* Added Dakota methods: SOGA, MOGA
* Added support for using precalculation files (reset files)
* Added support for failure-tolerant optimization loops (see Section "Workflow Engine" below) 

### Script API 

* Various improvements and extensions (e.g. support for "not a value", execution count, persistent state)
* Added option to close the outputs of tools in pre/postprocessing scripts of tool integration
* Removed deprecated parts of the API 

### Tool Integration 

* Made the script API accessible in pre/postprocessing
* Added an option to limit the number of parallel tool executions (e.g. to prevent excessive license usage) 

### Data Management 

* Major rework of the data management backend (data model and API) to increase performance and robustness
* Workflow Data Browser now shows input and output data of all components and additional workflow run information
* Workflow Data Browser now also shows the path to the working directories of integrated tools (for manual inspection) 

### Usability 

* Simplified resetting the "Don't ask again" setting of the workspace chooser. It can be reset via "Help -> Open Configuration Information". 

### Batch mode (rce --batch) 

* Command execution output is now written to standard output as well, which makes it available from the invoking command line
* Improved robustness 

### Workflow Engine 

* Completely reworked workflow execution (as a prerequisite for single component run, restart after failure, and stepwise execution)
* Reworked scheduling options (initial, required, optional -> constant, single, consumed and required, required if connected, not required). For details and migration path, see documentation.
* Provided better support for nested loops including reset of nested loops
* Made optimization and parametric study loops failure-tolerant, i.e. extended Python/Jython script API to allow to indicate that tool/script failed, but only because of invalid input parameters
* Added automatic writing of basic history data (inputs, outputs) to all components
* Fixed workflow console row writer to ensure no log rows are missing after workflow execution
* Added handling of system time differences between workflow controller and component
* Added handling of system time differences between workflow controller and component hosts
* Added support for limitation of parallel tool executions 

### Cluster

* Added support for TORQUE 5.0 

### Converger

* Added possiblity to finish on first check for negative values 

### Commands

* Added "–dispose" flag to "wf run" command to allow disposal after workflow execution
* Added "–dispose", "–pr" and "–sr" flags to "wf verify" command (for automated testing) 

### Other/Misc 

* Merged the three former RCE editions (Standard/CPACS/Transport) into a single one
* Improved branding (splash screen, about dialog, ...)
* Upgraded to Eclipse RCP 3.7.2
* Improved the cleanup mechanism for temporary files
* On RCE startup, the last debug.log and warnings.log files are automatically preserved as *.previous.log
* Various bugfixes
* Various usability tweaks 

