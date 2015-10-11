# forumdev-div
a collection of django apps used by the forumdev project which (at least not yet) warrant a standalone project since they are very specifically design for use cases in the forumdev project 

#### install

> don't forget to link the subfolders (boxes, categories) into your django folder

add `boxes` and `categories` in `INSTALLED_APPS` in settings.py

run `./manage.py syncdb`

now you can place the plugins via the structure mode on your page...
