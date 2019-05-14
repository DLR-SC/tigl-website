Title: Finishing the CPACS 3 wing structure implementation
Date: 2019-05-14 09:24
Category: News
Author: Martin Siggel

CPACS 3 offers many new ways to define wing structural elements.
Spars can now be defined between two ribs. 
Ribs also have a multitude of ways to be positioned, including the positioning
 
  - at a dedicated spar positioning,
  - at arbitrary eta/xsi coordinates,
  - at any position on a spar, the leading edge or the trailing edge
  - and any combination of them.
 
 The implementation of all these new features took us a while and
 was the main issue, why TiGL 3 is not yet released.
 
 The good news: We have to everything in shape and support all
 these new features.
 Here's a first glimpse of what you can expect with the new
 structural definition:
 
 ![New ribs and spars features](images/ribsspars-cpacs3.png)
 
### Automatic conversion to CPACS 3 ###
 
The new CPACS definition comes to the price of more
complex CPACS files. Converting a CPACS 2 file into the
new format can be very time consuming and error prone,
if many ribs and spars are defined in the file.

To help you with the conversion process, we developed a small
``cpacs2to3`` utility. Like TiGL, this converter is open source
and hosted on github: [https://github.com/DLR-SC/cpacs2to3/](https://github.com/DLR-SC/cpacs2to3/)

cpacs2to3 can be installed with the Conda package manager.
Just create a new virtual environment and install cpacs2to3 in it:

```
conda create -n cpacs2to3 python=3.5 cpacs2to3 -c dlr-sc
```

To convert a cpacs file, use ``cpacs2to3`` as follows

```
activate cpacs2to3
cpacs2to3 myaircraft.xml -o myaircraftv3.xml
```

### Limitations of the conversion ###

CPACS 2 allowed to explicitly placing a rib in a wing section element.
With the new definition, ribs can be placed with arbitrary eta/xsi
coordinate combinations, which also enables to place a rib in a section.

In TiGL 2 however, ribs that have been placed into a section where not
affected by a rib rotation around the z axis. Meaning, the rib kept always
to be in the section. With the new definition, this is not the case anymore.
The cpacs2to3 converter will return a warning in this case.
Then it is up to the user to decide, what to do.

If you really want to have a rib inside a section, there is still
the explicit rib positioning, which allows an exact rib positioning
inside a section.