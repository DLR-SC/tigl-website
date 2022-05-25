# Website for TiGL

Homepage (landing page) and announcements for TiGL (http://tigl.github.io).

Based on [Pelican](http://blog.getpelican.com/) and a modifed Polar theme by [CodePassenger](http://www.codepassenger.com/).

## Local Installation

* Clone tigl-website

  ```
  git clone https://github.com/DLR-SC/tigl-website
  ```
  or
  ```
  git clone git@github.com:DLR-SC/tigl-website.git
  ```
* Change to 
  ```
  tigl-website/
  ```

* Install pelican, fabric3 and some other dependencies

  ```
  pip install -r requirements.txt
  ```

## Build 

* Run 
  ```
  pelican -s pelicanconf.py
  ```

  to generate the site locally in `output`.

  For a publication-ready version run

  ```
  pelican -s publishconf.py
  ```

  The generated site will be in `published`.


## Writing Content

Use either [Markdown](http://daringfireball.net/projects/markdown/) or HTML for new articles, as described in [Writing content](http://docs.getpelican.com/en/3.6.3/content.html).

Add new articles to `content`.

### Metadata

The required meta data for TiGL release announcements are:
```
Title: Release 3.0.0
Date: 2019-01-01 00:00
Category: Releases
Author: TiGL
```



### Image sizes

 * Article image: 870x440 px (doesn't apply for the overview image of the article)
 * Thumbnail large: 100x108
 * Thumbnail small: 67x73


