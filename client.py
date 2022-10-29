import time


def user_interface():
    """This function will ask the user for input, then that input gets written to
    image-download.txt file. Which will be read by image_server.py."""
    while True:
        hike_name = input("Enter hiking trail name: ")
        image_name = input("Enter name of file: ")
        num_of_images = input("Enter number of images to download: ")
        directory = input("Save to: ")

        user_input = hike_name + ";" + image_name + ";" + num_of_images + ";" + directory
        file = open("image-download.txt", "w")
        file.write(user_input)
        file.close()
        time.sleep(5)


if __name__ == '__main__':
    user_interface()
