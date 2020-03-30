# COVID-19 Backend  

* Implement RestfulAPI to serve the data available for cities, each day as the pademic progresses
* Implement script to extract data from offical sites like dep. of public health to get the case data
 
## Setup for local dev (for macOS)

Install Python3 thru brews if you don't have it already

#### `brews install python3`

You should have `pip3` installed now as part of python3

Install `virtualenv` and `virtualenvwrapper` for project management

#### `sudo pip3 install virtualenv virtualenvwrapper` 

Following the post-install instruction to setup the wrapper script to auto run on starting terminal window

You are ready to create a virtual env for this project now. Let's call it `covid19`

#### `mkvirtualenv covid19`

You will be in this virtual python env now after this. 

To deactivate this env, 

#### `deactivate`

To work on the `covid19` env

#### `workon covid19`

To list the available envs

#### `workon`

After the virtual env is setup, make you are working on the `covid19` env, as indicated in the prompt with parenthesis, clone this project to your development folder.

#### `cd <your preferred project location>`
#### `git clone <github address of your fork>`

Please do fork this project 

Go into the backend folder

#### `cd covid19/backend`

Install the requirements

#### `pip install -r requirements.txt`

Run Django migration

#### `python manage.py migrate`

Start Django dev server

#### `python manage.py runserver`

Go to your browser and load `http://localhost:8000` to see django is properly setup. 

You are ready to code!!

Read [Django tutorial here](https://docs.djangoproject.com/en/3.0/intro/tutorial01/)






