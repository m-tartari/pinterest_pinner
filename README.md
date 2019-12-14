# Pinterest Pinner
This script publishes all photos from a selected page into a target Pinterest board using the Pinterest API. It has been custom made for [Compagnia d'arme del Santo Luca](http://www.compagniadarmedelsantoluca.it/) but can be easily adapted to be used for any website.

## Download
this project can by downloaded using:
```
git clone https://github.com/m-tartari/pinterest-pinner.git
```
and run using:
```
python3 pinner.py
```

## Before use
Before using this script you need to edit the data.json file. It should contain:
```
{
  "board_name": "Name of the board in which the images will be saved",
  "the_album": "http://www.url_from_which_you_want_to_save_images",
  "access_token": "put_here_your_pinterest_access_token"
}
```
The access token can be generated using [postman](https://www.getpostman.com/) and following [Pinterest API official guidelines](https://developers.pinterest.com/docs/api/overview/).
