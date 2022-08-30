from flask import make_response

class Response:
    def __init__(self, response_message=""):
        self.response = make_response(response_message)

    def cookies(self, key, value):
        self.response.set_cookie(key, value)
        return self

    def delete_cookies(self, key):
        self.response.delete_cookie(key)
        return self
    
    def redirect(self, path="/"):
        self.response.headers["location"] = path
        return self.response, 302