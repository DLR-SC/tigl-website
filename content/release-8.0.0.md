Title: RCE 8.0 
Date: 2016-12-06 13:19
Category: Releases
Author: RCE

We are proud to announce a new major release: RCE 8 - Red Snapper. It contains several new features and many improvements. Below is a selection of some of them. Please see [GitHub](https://github.com/rcenvironment/rce/wiki/Changelog:-8.x.x-Releases) for the full changelog.

### Manual Verification of Tool Results

In collaborative workflows, the tools involved are contributed by different persons and usually run at different sites within one organization or even accross multiple organizations. Tool results are passed from one tool to all succeeding ones. In a collaborative setup, one want to avoid passing wrong tool results to tools that belong to another person in order to avoid a waste of compute resources at another site. To allow a tool integrator to check tool results before they are passed to another tool, we have introduced the concept of manual verification of tool results. If enabled, the tool results are only passed to other tools if the tool integrator has approved them.

![Photo]({attach}images/release-8.0.0/result_verification.png)

### Enhanced Workflow Editor

In order to prevent overlapping of small elements by larger ones, we have added a z-index ordering for workflow components and labels. Workflow labels can have a header now and we added automatic word wrap. If a workflow file is opened from the workflow data browser a read-only version of the workflow editor is opened now. It allows the comprehension of the workflow and the component configurations without the chance to modify it by mistake. Furthermore, enabling and disabling the so called 'Tool Run Imitation Mode' can be done with the help of the context menu now.

![Photo]({attach}images/release-8.0.0/read_only_editor.png)

### Enhanced Nested Loop Support

RCE is capable of running workflows with nested loops. The creation of nested loops got easier. An additional connection beetween the workflow driver components (indicating whether the loop is terminated) is not required anymore. Furthermore, for each input and output of workflow driver components the information is given whether they are supposed to be connected to the loop driven by this workflow driver component or to the next upper loop.

### Enhanced Workflow Components

We have made several enhancements to workflow components such as:

The evaluation memory component is nested-loop-capable now. We have added a validation for the python executable location given by the user at workflow start for Script components. The Design of Experiments component has a new output that provides the number of design sets going to be sent.
