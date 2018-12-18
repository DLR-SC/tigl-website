Title: RCE 7.1 
Date: 2016-05-24 15:00
Category: Releases
Author: RCE
Image: release-7.1/general.png

We recently released RCE 7.1, a new minor version with several new features and many improvements. Below is a selection of some features. Please see [GitHub](https://github.com/rcenvironment/rce/wiki/Changelog:-7.x.x-Releases) for the full changelog.

### Unified Access to Documentation in RCE

Documentation of RCE is spread over different places: component documentation is accessible from the workflow editor, documentation about tool integration is accessible from the tool integration dialog, and the user guide in PDF format. We introduced a new help system to make all of the documentation additionally accessible from one single place. Go to the menu bar under "Help -> Help Contents". A window opens with all of the documentation and nice navigation and search capabilities.

![Photo]({attach}images/release-7.1/help_system.png)

### Workflow Outline View

Workflows with many components get quite big. For keeping track of those workflows, we added a new outline view. It displays the complete workflow in a thumbnail format and highlights the area of the workflow which is currently shown in the workflow editor.

![Photo]({attach}images/release-7.1/outline_view.png)

### Enhanced Workflow Canceling

In case a workflow is canceled (by the user or after a failure in the workflow), integrated tools as well as running Python scripts (executed by the Script component) are canceled imediately. It is no longer waited until they terminate itself. Also, jobs submitted to a cluster (by the Cluster component) are canceled imediately. In case of long running tools, scripts or cluster jobs, compute time is saved now.

![Photo]({attach}images/release-7.1/canceled.png)

### Extended SSH Remote Access

RCE provides an SSH interface to execute components and workflows (among others). Next to username and password, authentication via key files is now supported. Also, when connecting an RCE client to another RCE instance via SSH, not only remotely published components can be used in workflows, but also remotely published workflows appear in the workflow component palette ready to use in workflows.


### Enhanced Workflow Components

We made enhancements to several workflow components such as:

The mapping file required by the XML Merger can be sent as an input. This makes reloading the mapping file on each change obsolete.  
The Evaluation Memory can be used in fault-tolerant loops as it is now able to treat loop failures properly.
The behavior of the Converger can be defined in case convergence was not reached. Also, outputs are added which indicate convergence for every input separately.
The Output Writer supports new placeholders: "original filename" and "execution count".  
