import falcon
import json
#from app.config import db_session, init_session
#from app.middleware import JSONTranslator
#import app.views


#api = falcon.API(middleware=[JSONTranslator()])
#api.add_route('/tasks/', views.TaskResource())


init_session()
if __name__ == "__main__":
   api.run(host="0.0.0.0", debug=True)