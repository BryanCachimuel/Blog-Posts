from blogr import create_app

if __name__ == '__main__':
    app = create_app()
    # estableciendo que la aplicación se ejecute en modo debug
    app.run()