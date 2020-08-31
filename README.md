# [Blog](http://lauraemc.pythonanywhere.com/) 
* hosted on pythonanywhere.com

Created as part of University of Birmingham bridging coursework to progress from second year

## Run site locally
### Setup 
```
virtualenv venv
source venv/bin/activate 
pip install requirements.txt
```
### Run 
```
python manage.py runserver
```

## Tests
### Run functional tests 
`python functional_tests.py`

### Run unit tests
`python manage.py test`

* meets all tests when logged in - currently do not have functionality to log in guest users
* as a result will encounter error when trying to access a page that you do not have permissions for - e.g. manually entering an edit post URL 

## Resources used:
Tutorial - [Django girls](https://tutorial.djangogirls.org/en/)

Design template - [HTML5 UP](https://html5up.net/solid-state)

Images (all labelled for reuse)- 
* https://commons.wikimedia.org/wiki/File:TDD_Global_Lifecycle.png
* https://pixabay.com/illustrations/webdesign-design-web-website-3411373/
* https://www.geograph.org.uk/photo/4346039
* https://commons.wikimedia.org/wiki/File:New_office.jpg
