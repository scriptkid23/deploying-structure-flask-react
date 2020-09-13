from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from security.blacklist import blacklist

class UserObject:
    def __init__(self, username, roles):
        self.username = username
        self.roles = roles

jwt = JWTManager()
def initialize_Security(app):
    jwt.init_app(app)
    
@jwt.user_claims_loader
def add_claims_to_access_token(user):
    return {'roles': user.roles}

@jwt.user_loader_callback_loader
def user_loader_callback(identity):
    if identity not in users_to_roles:
        return None

    return UserObject(
        username=identity,
        roles=users_to_roles[identity]
    )
    
@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.username

@jwt.user_loader_error_loader
def custom_user_loader_error(identity):
    ret = {
        "msg": "User {} not found".format(identity)
    }
    return ret 


# Logout 
@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return jti in blacklist