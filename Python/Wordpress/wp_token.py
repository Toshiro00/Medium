import requests

class Token():
    def __init__(self, *args):
        self.username = args[0]
        self.password = args[1]
        self.endpoint = 'http://your-beautiful-website.com/wp-json/jwt-auth/v1/token'

    def generate(self):
        data = {
        "username": self.username,
        "password": self.password
        }
        
        token = requests.post(self.endpoint, data)
        return token

if __name__ == '__main__':
    #username = 'admin'
    #password = 'admin'

    print('=== Welcome to Token Generation ===')
    print('=== Generated for Medium Users ===')
    print('=== Feel free to use and share ===')
    print('=== Enter your username and password to create tokens  ===')
    username = input('Username : ')
    password = input('Password : ')

    token = Token(username, password)
    generated = token.generate()

    if generated.status_code == 200:
        print(generated.text)
        print()
        print('Token generated successfully.')
    else:
        print('There is some error with your username and password.')