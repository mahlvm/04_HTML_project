import os
from lib.database_connection import get_flask_database_connection
from flask import Flask, request, render_template
from lib.album_repository import AlbumRepository
from lib.artist_repository import ArtistRepository


# Create a new Flask app
app = Flask(__name__)

# @app.route('/emoji', methods=['GET'])
# def get_emoji():
#     return render_template('emoji.html', emoji=':)')
# from example_routes import apply_example_routes
# apply_example_routes(app)

# @app.route('/goodbye')
# def get_goodbye():
#     return render_template("goodbye.html")

@app.route('/albums')
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    return render_template ("albums/index.html", albums=albums)

# @app.route('/artists')
# def get_artist():
#     connection = get_flask_database_connection(app)
#     repository = ArtistRepository(connection)
#     artists = repository.all()
#     return render_template ("artists/index.html", artists=artists)

@app.route('/artists/<album_id>')
def get_album_find(album_id):
    connection = get_flask_database_connection(app)
    repository_album = AlbumRepository(connection)
    repository_artist = ArtistRepository(connection)
    albums = repository_album.find(album_id)
    artists = repository_artist.find(album_id)
    return render_template ("artists/index.html", artists=artists, albums=albums)




if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
