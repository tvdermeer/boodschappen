import falcon
import requests

class Resource(object):
    
    def on_post(self, req, resp):

        json = {
            "message": {
            "affenpinscher": [],
            "african": [],
            "airedale": [],
            "akita": [],
            "appenzeller": [],
            "australian": [
                "shepherd"
            ],
            "basenji": [],
            "beagle": [],
            "bluetick": [],
            "borzoi": [],
            "bouvier": [],
            "boxer": [],
            "brabancon": [],
            "briard": [],
            "buhund": [
                "norwegian"
            ],
            },
            "status": "success"
            }
        resp.status = falcon.HTTP_200
        resp.body = json
