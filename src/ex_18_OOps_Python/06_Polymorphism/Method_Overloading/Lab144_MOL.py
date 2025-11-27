class Browser:

    def make_http_request(self):
        print("Hi, Lets make the HTTP request without auth")

    def make_http_request(self, url, auth=None):
        print("Hi, Lets make the HTTP request without auth", url, auth)


t = Browser()
t.make_http_request("google.com")
