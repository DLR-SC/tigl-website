Title: Christmas Greetings 2023
Date: 2023-12-22 15:00
Category: Misc
Author: Johannes Holke and Sandro Elsweijer

The t8code developer team wishes merry Christmas, happy holidays and a happy new year 2024.
<img src="images/christmas23/AMR_christmas_card_2023.gif" height="600" />

This year's Christmas mesh shows a christmas tree with sparkling lights and demonstrates on of our new features developed in 2023: CAD-based geometry interpolation.

We store the original CAD geometry of the boundary surfaces/edges in the coarse mesh and using a newly developed volume interpolation scheme we can recover the accurate geometry of all points inside the coarse tree.
Thus, even with very coarse input mesh (and hence being very memory efficient) we can accurately mesh complex geometries.

The left hand side of the tree shows the linear geometry while the right hand side shows a curved one.
The more we refine the more accurate our representation looks.

This feature is based on the works of Sandro Elsweijer and Jakob Fussbroich. For more information, see our [research note at IMR2022](https://elib.dlr.de/186570/), [Sandro's thesis](https://elib.dlr.de/186561) (implementation for quads/hexes) and [Jakob's thesis](https://elib.dlr.de/200442) (implementation for triangles/tets).

