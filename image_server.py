import os
import time

from google_img_search import GoogleImage

google_img = GoogleImage(os.environ['API-KEY'], os.environ['CX'])

def download_image():
    """This function will read 'image-download.txt' and will search for the desired
    image that is named in image-download.txt."""

    last_modified = 0

    while True:
        time.sleep(10)
        mod_time = os.stat("image-download.txt").st_mtime
        file = open("image-download.txt", "r")
        lines = file.readlines()
        file.close()
        if len(lines) > 0 and mod_time != last_modified:
            data = lines[-1].split(";")
            if len(data) == 4:
                print("Request received. Searching...")
                last_modified = mod_time
                hike_name = data[0]
                image_name = data[1]
                num_of_images = data[2]
                path = data[3]
                #download the desire image
                google_img.search_for(hike_name, image_name, num_of_images, path)
                print(f"Downloaded to {path}")


if __name__ == '__main__':
    download_image()

