from flask import Flask

def create_app():
    app = Flask(__name__)
    @app.route('/api/v1/hello-world-5')
    def index():
        return "Hello World 5",200
    return app

if __name__ == '__main__':
    from waitress import serve
    serve(create_app(), host='0.0.0.0', port=5000   )
