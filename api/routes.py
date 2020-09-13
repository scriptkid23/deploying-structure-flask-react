from controllers.IndexController import *

def initialize_routes(api):
    api.add_resource(AwardController,'/api/award')
    api.add_resource(AdminLoginController,'/api/login')
    # api.add_resource(ScratchCardsController,'/api/card')
    api.add_resource(ChallengeController,'/api/challenge')