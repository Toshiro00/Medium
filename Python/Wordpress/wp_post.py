import requests
from datetime import *

class Wordpress():
    def __init__(self):
        # For Image upload
        self.POST_MEDIA = 'http://localhost/wp-json/wp/v2/media' 

        # For Article upload
        self.POST_ARTICLE = 'http://localhost/wp-json/wp/v2/posts' 

        # For Update
        self.UPDATE_POST = 'http://localhost/wp-json/wp/v2/posts/' 

        # Replace your token here.
        self.JWT_TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9sb2NhbGhvc3QiLCJpYXQiOjE2NTcxOTU2NDUsIm5iZiI6MTY1NzE5NTY0NSwiZXhwIjoxNjU3ODAwNDQ1LCJkYXRhIjp7InVzZXIiOnsiaWQiOiIxIn19fQ.ZnTL_GfhAagIvAZxh3C_TkrLroiAk7gp1y5snnuS45w'

    def post(self):
        headers = {
            'Authorization': 'Bearer %s' % self.JWT_TOKEN,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        data = {
            'title': 'My first post with Python',
            'slug': 'my-first-post-with-python',
            'content': 'I read a great post on medium and I made it. But I have to fill this space with beautiful contents.',
            'categories': '1',
            'authors': 'admin',
            'status': 'publish',
            'format': 'standard',
        }
        response = requests.post(self.POST_ARTICLE, headers=headers, json=data)
        return response

    def post_image(self):
        headers = {
            'Authorization': 'Bearer %s' % self.JWT_TOKEN,
        }

        # Your image path here
        image = 'test.png'

        files = {
            "file": (image, open(image, 'rb'), 'image/jpg'),
            }

        # Fill data as you wish, if you dont want caption leave it blank
        data = {
            'title': 'My First Image',
            'alt_text': 'My First Alt Text',
            'caption': ' ',
        }

        response = requests.post(self.POST_MEDIA, headers=headers, files=files, data=data)
        response_dict = response.json()
        link = response_dict.get('guid').get('rendered')

        if response.status_code == 201:
            return link

    def run(self):
        # Post and get response
        post_response = self.post()
        image_response = self.post_image()

        # Print
        print('Post Response: {}'.format(post_response))
        print('Image Link: {}'.format(image_response))


if __name__ == '__main__':
    post = Wordpress()
    post.run()