# Currency Notifier
DISCLAIMER:

This project was designed solely for study and for personal use only.

Background/goal:

Following on the previous project that would utilise the API to retrieve historic data and provide basic analysis, the next step was to change the project a little to implement a UI to exchange values directly. 

Dependencies/tools used:

API - I am using the Currency API (see documentation here: https://currency.getgeoapi.com/documentation/) to gather current and historical exchange rates
dotenv - to store API-keys and email logins
tkinter - used to create a UI on python

Challenges/what I have learned:

- Utilise dictionaries to manage widget creations (rather than creating similar widgets by writing out the same code over and over again, use a dictionary to loop through and retrieve information)
- Create a tkinter app in a class instead to encapsulate the code
