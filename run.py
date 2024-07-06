from lib import create_app

app, celery_app = create_app()

if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug=True)
