## PROJECT NAME 
*My_Pic_Hub*


## AUTHOR 
Asande Larvine


## DESCRIPTION 

This is a photo gallery web Application where you can view photos and see the details of each photo

## Features


As a user of the application you will be able to:


1. View different photos that interest you.
2. Click on a single photo to expand it and also view the details of the photo. The photo details will appear on a modal within the same route as the main page.
3. Search for different categories of photos. (ie. Sneakers, Art)
4. Click on share icon to share the image with any of your social account or alternatively Copy a link to the photo and share.
5. View photos based on the location they were taken or category.

## Admin Dashboard

[Admin Dashboard Login](https://larv-gallery-hub.herokuapp.com/admin)  with credentials

    username : `Pic_Hub`

    password : `@pichub`
### Installation and setup instructions

1. Clone this repo: git clone https://github.com/asandelarvine/My_Pic_Hub
2. The repo comes in a zipped or compressed format. Extract to your preferred location and open it.
3. open your terminal and navigate to gallery then create a virtual environment.For detailed guide refer  [here](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/)
3. To run the app, you'll have to run the following commands in your terminal
    
    
       pip install -r requirements.txt
4. On your terminal,Create database gallery using the command below.


       CREATE DATABASE gallery;
5. Migrate the database using the command below


       python3.8 manage.py migrate
6. Then serve the app, so that the app will be available on localhost:8000, to do this run the command below


       python manage.py runserver
7. Use the navigation bar/navbar/navigation pane/menu to navigate and explore the app.


## TECHNOLOGIES USED 
* [Python3.8](https://www.python.org/)
* [Django](https://docs.djangoproject.com)
* [Heroku](https://heroku.com)
* HTML - For building Mark Up pages/User Interface
* CSS - For Styling User Interface

## Known Bugs

* Location not displaying, but yet to be resolved.


## CONTACTS
asandelarvine@gmail.com

## LIVE LINK
https://larv-gallery-hub.herokuapp.com/
