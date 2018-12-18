Title: Release 3.2.0
Date: 2013-09-24 10:20
Category: Releases
Author: RCE


### Changelog

* improved handling of long-lasting remote component initializations
* fixed validation errors not showing up in log
* fixed connection removal via Undo
* workflows are properly disposed on shutdown now
* improved default workspace locations of "launch" configurations
* fixed double-click in read-only workflow view switching to properties view
* changed behaviour of Script component on second click
* updated example workflows and fixed nested loop workflow
* fixed sending an output to more than one input
* guarded converger component against certain loop behavior
* fixed handling of Boolean values in component input view
* existing workflows are now properly shown after a network merge
* workflow console output is now properly removed after workflow deletion
* fixed remote workflow deletion breaking workflow tabs
* fixed workflow console scrolling issues
* made TiGLViewer a dedicated component
* TiglViewer: fixed issue with workbench restart
* Optimizer component: improved configuration GUI
* Python/Jython component: deprecated old script API
* Python/Jython component: using the same names for inputs and outputs is now allowed
* Python/Jython component: fixed hangs on long console output
 * Excel component: fixed pruning of output channel
* minor usability improvements
* improved test code coverage
* various other bug fixes 
