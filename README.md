# Website for RCE

Homepage (landing page) and announcements for RCE (http://rcenvironment.de).

Based on [Pelican](http://blog.getpelican.com/) and a modifed Polar theme by [CodePassenger](http://www.codepassenger.com/).

## Local Installation

* Install Python ([Anaconda](https://store.continuum.io/cshop/anaconda/) works perfectly)

* Install Pelican and supporting libraries

  ```
  pip install pelican
  pip install markdown
  pip install fabric
  pip install ghp-import
  ```

* Clone rce-website

  ```
  git clone https://github.com/DLR-SC/rce-website
  ```
  or
  ```
  git clone git@github.com:DLR-SC/rce-website.git
  ```
* Change to 
  ```
  rce-website/
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

The required meta data for RCE release announcements are:
```
Title: Release 6.3.0 
Date: 2015-07-29 10:20
Category: Releases
Author: RCE
```



### Image sizes

 * Article image: 870x440 px (doesn't apply for the overview image of the article)
 * Thumbnail large: 100x108
 * Thumbnail small: 67x73


