class Browser:
    def make_http_request(self,url):
        print("Making http request",url)

    def  make_http_request(self,url,auth=None):
        print("Making http request",url,auth)

t=Browser()
t.make_http_request("http://www.python.org","admin")


