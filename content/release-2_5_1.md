Title: Release 2.5.1
Date: 2013-06-10 10:20
Category: Releases
Author: RCE


### Changelog

* extended Converger component to add support for nested loops
* added workflow status icons to workflow runtime tab
* added support for macros to Excel component's export function
* Excel component exports to clipboard with Excel-like insertion
* fixed copying a workflow component in the workflow editor (the copied component had the same name as the orgin one)
* fixed bug with runtime variables, which causes errors under some special circumstances
* fixed some memory leaks
* fixed start up validators
* added validation to the workflow connection editor: it prohibts a connection between an input and more than one output (this would result in scheduling problems)
* minor fixes 