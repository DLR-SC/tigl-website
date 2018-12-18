Title: RCE 8.1
Date: 2017-07-14 13:53
Category: Releases
Author: RCE

We just released RCE 8.1, which contains several new features and improvements. Here we present a selection of new features. Please see [GitHub](https://github.com/rcenvironment/rce/wiki/Changelog:-8.x.x-Releases) for the full changelog.

### Workflow Editor

In RCE 8.1, bidirectional connections between components are now depicted by separate connection lines, which allows a better overview over the workflow. Also we enhanced the zooming capabilities of the workflow editor and added the capability to export workflows as images.

![Photo]({attach}images/release-8.1.0/bidirectional_connections.png)

### Enhanced Workflow Components

We made enhancements to several workflow components: 
For all driver componennt, start values can be declared as constant. In the DOE Component, it is now possible to define a custom table as start input.


### Startup

We added a dialog for selecting the profile to start RCE with. Furthermore we reduced the disk activity on startup to allow a more efficient start of RCE.