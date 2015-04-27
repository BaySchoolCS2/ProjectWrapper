import json
import os
import platform
import requests
import sys

class NotFound(Exception):
    pass

def get_url(url, token, ua):
    if token != None:
        return requests.get(url, auth=token, headers={'User-Agent':ua})
    else:
        return requests.get(url)


class Wrapper:

    def __init__(self, user_agent="Wrapper"):
        self.token = None
        self.URL = "http://localhost:5000/"
        self.user_agent = user_agent

    def me(self):
        r = get_url(self.URL+"api/v1/me", self.token, self.user_agent)
        self.raw = json.loads(r.text)
        self.posts = self.raw["posts"]

    def get_user(self, user):
        r = get_url(self.URL+"api/v1/posts/%s" % user, self.token, self.user_agent)
        if r.status_code == 200:
            self.raw = json.loads(r.text)
            self.posts = self.raw["posts"]
        elif r.status_code == 404:
            raise NotFound
