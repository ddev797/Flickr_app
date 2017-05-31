# Flickr_app

Flickr_app is built to get all images from Flickr api based on search term and lat/lng.

For eg:
Search Term/Tags : Sunrise
Lat : 12.9354922
Lng : 77.6146828

Generate FLick api key from here : https://www.flickr.com/services/apps/create/

Steps to create env variable in .bashrc file:
1. GO to your HOME folder and look for a file named .bashrc
2. Open it with a text editor
3. Add the following lines of code:
```export flickr_api_key="FLICKR_API_KEY"```


Steps to install python files to execute this project:
1. Open terminal
2. Create a folder where you want the project to be installed
3. Download or pull code from github
4. Run ```pip install virtualenv``` on the terminal
5. If the above command gives any permission error then use ```sudo``` before every ```pip``` command Eg: ```sudo pip install virtualenv```
6. Create a virtual environment by executing this command :  ```virtualenv .env```
7. Now activate the virtual environment by executing this command : ```source .env/bin/activate```
8. Install all the requirements for the project by executing this command : ```pip install -r requirements.txt```
9. If you are getting an error around six library then execute this command : ```sudo -H pip install --ignore-installed six```
10. Now execute the command : ```python get_image.py```
11. It'll download all images in your folder



