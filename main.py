from website import create_app
from website import create_database

app = create_app()


if __name__ == '__main__':
    create_database(app)
    app.run(debug=True)