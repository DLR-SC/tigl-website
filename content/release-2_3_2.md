Title: Release 2.3.2
Date: 2012-06-14 10:20
Category: Releases
Author: RCE


### Changelog

* added support for RCE headless mode: workflow execution without GUI
* added workspace chooser at RCE start up
* improved workflow scheduler logic: support of different input usages (required, initial, optional)
* added compare function for text files in workflow data browser
* added "Reset search" button for workflow console filter
* added "Save as ..." to 'File' menu
* extended start up validators: length of parent file system path, JVM settings
* fixed copying of workflow nodes: copied workflow node is a real new clone now. Thus, workflow nodes don't receive configuration values of other nodes anymore)
* fixed minor issues 