from flask import Response, request
from flask_restful import Resource,reqparse
import json
from services.ScratchCardService import ScratchCardService

scratchCardService = ScratchCardService()

class AdminLoginController(Resource):
    def post(self):
        return None 
class AwardController(Resource):
    def get(self):
        return None
class ChallengeController(Resource):
    
    def post(self):
        payload = request.get_json()
        scratchCardService.addChallenges(payload)
        return Response(json.dumps({"message":"Add challenge succeeded"}), 
                        mimetype="application/json", status=200)

# class ScratchCardsController(Resource):

#     def post(self):
#            payload = request.get_json()
#            scratchCardService.addCard(payload)
#            return None 
        
#     def get(self):
#         return None 
#     def put(self):
#         return None
#     def delete(self):
#         return None
    
