Instructions on how to use:

Note: Will need to enable Google Custom Search API. Instructions can be found here:
https://pypi.org/project/Google-Images-Search/


The microservice consist of two python files: 
image_server.py: this is the "server"
google_img_search.py: this takes care of searching/downloading image from google.

The optional file included:
client.py: this is to help demonstrate how to communicate with image_server.py

How to REQUEST data:
Four parameters/values are needed, they are:
1) name of hike
2) file name
3) number of images to download
4) directory where images will be saved

This information must be given in a string and written into image-downloaded.txt file. For example, it can be something like this (mac):

multnomah falls;oregon;1;//Users//NewUser//Desktop//images_downloaded

How to RECEIVE data:
Make sure the directory given from above exists. Then the server will automatically look up images from google and download the desired number of images into that directory.


UML Diagram:

![](https://i.imgur.com/HvQV87q.png)
