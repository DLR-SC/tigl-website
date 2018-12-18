Title: Release 6.2.1 
Date: 2015-06-24 10:20
Category: Releases
Author: RCE

## Synopsis

* Fixed broken directory structure for files and directories, which are received as input values by the script component and by integrated tools
* Removed reliably XSLT mapping files from working directories of integrated CPACS tools (in some cases they are left)
* Endpoints can be deleted again even if they are currently connected
* Due to some issues, the renaming option for files and directories received by integrated tools is removed (it is always "-As incoming-" now) 