from app import create_app

if "__main__" == __name__:
    app = create_app()
    app.run()