from app import app
from app import db
from posts.blueprint import posts

import view

app.register_blueprint(posts, url_prefix='/blog')

if __name__ == '__main__':
	app.run(host='127.0.0.2', port=5002, debug=True)