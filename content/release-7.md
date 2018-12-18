Title: RCE 7 
Date: 2015-12-01 15:00
Category: Releases
Author: RCE
Image: release-7/general.png

We are proud to announce RCE 7. A major release with a lot of features and various improvements. Below you find a selection of some features. Please see [GitHub](https://github.com/rcenvironment/rce/wiki/Changelog:-7.x.x-Releases) for the full changelog.

### Remote Tool Access via SSH Connections
To access and execute tools across untrusted networks, we added support for tool access and execution via SSH, a secure network protocol. Please note that otherwise RCE is intended to be used in trusted networks only. 


![Photo]({attach}images/release-7/ssh_connections.png)

Passwords for SSH accounts are configured as non-recoverable ("hashed") format now. We added a special configuration interface for SSH accounts ("rce --configure"). To support editing SSH accounts on servers, this UI can also be run in text mode.
 
![Photo]({attach}images/release-7/ssh-account_config.png)

### Enhanced Workflow Logging

We reviewed and improved all of the workflow-related log messages. We made them more suitable for end users. A log file is stored for each workflow component. Additionally, a log file for each workflow is stored with all of the error log messages related to the workflow. 

![Photo]({attach}images/release-7/workflow_logging.png)

### Enhanced Workflow Examples

We reworked the workflow examples so that they function as a kind of tutorial now.

![Photo]({attach}images/release-7/workflow_examples.png)

### New Workflow Components

We added two new workflow components. The 'Database' workflow component supports select, insert, update, and delete statements for MySQL and PostgreSQL databases. The 'Evaluation Memory' workflow component stores evaluation results of workflows for later re-use.

![Photo]({attach}images/release-7/new_workflow_components.png)

### System Monitoring for RCE Instances

We added support for system monitoring. Information about CPU and RAM usage are provided: for the host system, for RCE itself, and for each each tool that is executed by RCE. The information can even be accessed for remote RCE instances.

![Photo]({attach}images/release-7/system_monitoring_and_ssh.png)

