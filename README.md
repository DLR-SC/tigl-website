# Website for TiGL

Homepage (landing page) and announcements for TiGL (http://tigl.github.io).

Based on [Pelican](http://blog.getpelican.com/) and a modifed Polar theme by [CodePassenger](http://www.codepassenger.com/).

## Local Installation

* Install Python 2.7 ([Anaconda](https://store.continuum.io/cshop/anaconda/) works perfectly)

* Install Pelican and supporting libraries

  ```
  pip install pelican==3.7.1
  pip install markdown
  pip install "fabric<2"
  pip install ghp-import
  pip install bs4
  ```

***To Do: The API of fabric changed from version 1.14 to 2.4. We need 1.14 which only exists for python 2.7. We should probably modernize these two dependencies...***

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

### Configuration

 * Set proper port for local testing which works on your machine in `fabfile.py`
  ```
  # Port for `serve`
  PORT = 8001
  ```

## Build 

* Generate website 
  ```
  fab build
  ```

* Start local server for testing (accessible via http://localhost:[port]/)
  ```
  fab serve
  ```

* Convenience target for rebuild and starting local server
  ```
  fab reserve
  ```

## Deployment

Deploy to github pages with
  ```
  fab gh_pages
  ```

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


