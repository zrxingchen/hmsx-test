from application import app
from web.controllers.user.User import router_user
from web.controllers.index import router_index

app.register_blueprint(router_user, url_prefix='/user') 
app.register_blueprint(router_user, url_prefix='/user')
app.register_blueprint(router_index,url_prefix="/") 