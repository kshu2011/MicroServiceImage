from google_images_search import GoogleImagesSearch


class GoogleImage:
    """this class uses google_images_search library and allows
    the user to search/download image from google."""

    def __init__(self, api_key, cx):
        self._gis = GoogleImagesSearch(api_key, cx)

    def search_for(self, name, image_name, num_of_images, directory):
        _search_params = { #search parameters - searching for 'name' and will download the given num of images
            'q': name,
            'num': int(num_of_images)
        }
        # this will search and download and save final with custom name to given location
        self._gis.search(search_params=_search_params, path_to_dir=directory,
                         custom_image_name=image_name)
