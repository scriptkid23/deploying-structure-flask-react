from mongoengine import connect

# You can connect to a real mongo server instance by your own.
connect(
        db = 'tip-tip-tap',
        host = 'mongodb+srv://alook:alook12345678@object-information.i7udl.mongodb.net/tip-tip-tap?retryWrites=true&w=majority'
)