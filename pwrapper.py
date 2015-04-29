import json
import os
import platform
import requests
import sys

class NotFound(Exception):
    pass

class NotAllowed(Exception):
    pass




class Wrapper:

    def __init__(self, user_agent="Wrapper"):
        self.token = None
        self.URL = "http://localhost:5000/"
        self.user_agent = user_agent

    def get_url(self, url):
        if self.token != None:
            return requests.get(url, headers={'User-Agent':self.user_agent, "Authorization":self.token})
        else:
            return requests.get(url, headers={'User-Agent':self.user_agent})

    def me(self):
        if self.token == None:
            raise NotAllowed
        r = self.get_url(self.URL+"api/v1/me")
        self.raw = json.loads(r.text)
        # self.posts = self.raw["posts"]

    def get_posts(self, user=None):
        if user == None:
            r = self.get_url(self.URL+"api/v1/posts")
        else:
            r = self.get_url(self.URL+"api/v1/posts/%s" % user)

        if r.status_code == 200:
            self.raw = json.loads(r.text)
            self.posts = self.raw["posts"]
            return self.raw
        elif r.status_code == 404:
            raise NotFound
