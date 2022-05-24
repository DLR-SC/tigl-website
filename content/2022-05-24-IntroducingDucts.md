Title: Introducing ducts
Date: 2022-05-24 17:45
Category: News
Author: Anton Reiswich


<div class="row">
	<div class="col-md-8">
		<div class="feature-image">
			<img src="images/ductPicture1.png"/>
		</div>
	</div>
</div>

We are happy to announce TiGL’s new duct feature, that will be included in the coming release. It allows the user to create duct cutouts in wings and fuselages.


Based on a corresponding new CPACS development, TiGL was extended to support ducts and duct assemblies for aircraft configurations.

### Duct geometry ###

As for the case of a fuselage, the geometry of a duct is modelled using a network of profile and guide curves.

<div class="row">
	<div class="col-md-8">
		<div class="feature-image">
			<img src="images/ductPicture2.png"/>
		</div>
	</div>
</div>

Ducts are implemented in such a way, that TiGL always considers them as solids. 

### Basic modelling workflow ###

The related basic modelling workflow is as follows: 

  1. Define ducts.
  
     <div class="row">
	    <div class="col-md-8">
    		<div class="feature-image">
    			<img src="images/ductPicture33.png"/>
    		</div>
    	</div>
     </div>
  
  2. Define duct assemblies. Each duct assembly references the ducts it is composed of.
  
     <div class="row">
	   <div class="col-md-8">
		   <div class="feature-image">
			   <img src="images/ductPicture6.png"/>
		   </div>
     	</div>
     </div>
  
  3. Use the duct assemblies as a cutting tool to create cutouts of wings and fuselages via Boolean subtraction.

     <div class="row">
	   <div class="col-md-8">
		   <div class="feature-image">
			   <img src="images/ductPicture7.png"/>
		   </div>
	   </div>
     </div>
	
### Exclusion lists ###
	
For a higher level of control, there is an option to define an exclusion list for each duct assembly. Such a list contains the particular wings and fuselages that should not be cut by the considered assembly.

```xml
<excludeObjectUIDs>
              <uID>Fuselage</uID>
</excludeObjectUIDs>
```

<div class="row">
	<div class="col-md-8">
		<div class="feature-image">
			<img src="images/ductPicture9.png"/>
		</div>
	</div>
</div>

### Symmetry flag ###

Furthermore, ducts come with a symmetry flag, allowing the user to save modelling time in the case of symmetric configurations.

<div class="row">
	<div class="col-md-8">
		<div class="feature-image">
			<img src="images/ductPicture8.png"/>
		</div>
	</div>
</div>

