import falcon
from dog_breeds import Resource


api = application = falcon.API()

dog_breeds = Resource()
api.add_route('/dog_breeds', dog_breeds)
