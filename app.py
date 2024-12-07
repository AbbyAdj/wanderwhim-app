import routes
from flask import Flask

app = Flask(__name__)
app.register_blueprint(routes.all_routes)


if __name__ == '__main__':
    app.run(debug=True)

