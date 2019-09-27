Title: CPACS Creator Pre-Release
Date: 2019-09-27 14:57
Category: News
Author: Jan Kleinert

**We are happy to announce a pre-release of the CPACS Creator!**

CPACS Creator was developed by *Malo Drougard* at [CFS Engineering](https://cfse.ch/) and will be replace the TiGLViewer in a future release. 

<div class="feature-image">
	<img src="images/cpacscreator-gui.png"/>
</div>

## Features

With the CPACS Creator, you can edit your CPACS files in the TiGLViewer or create an airplane from scratch with just a few mouse clicks. You can

  - add wings and fuselages to your vehicle
  - modify high-level parameters such as width, height, length, positions, dihedral or sweep angle
  - add sections or exchange profile curves
  - manipulate transformations and positionings

and much more!

The high-level cpacs editing functions are also available in the API. You can now easily create small variations of the same aircraft from a python script:

```python
wing = wings.get_wing("Wing")

    for sweep in range(50, 80, 2):
        wing.set_sweep(sweep)
        save(tixi_h, aircraft, "Output/out-sweep-" + str(sweep) + ".xml")
```

## Installation

The pre-release is available as a conda package. We recommend installation into a clean conda environment

```bash
conda create -n cpacscreator python=3.6 cpacscreator -c dlr-sc
```

You can find the documentation [here](pages/documentation). **Enjoy!**
