import os
from lib.database_connection import get_flask_database_connection
from flask import Flask, request, render_template, redirect
from lib.album_repository import AlbumRepository
from lib.album_validator import AlbumValidator
from lib.album import Album
from lib.artist_repository import ArtistRepository
from lib.artist_validator import ArtistValidator
from lib.artist import Artist



app = Flask(__name__)

@app.route('/albums')
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    return render_template ("albums/index.html", albums=albums)

######

@app.route('/albums/<album_id>')
def get_album(album_id):
    connection = get_flask_database_connection(app)
    repository_album = AlbumRepository(connection)
    album = repository_album.find(album_id)
    return render_template ("albums/show.html", album=album)

######


# @app.route('/artists/<album_id>')
# def get_album_find(album_id):
#     connection = get_flask_database_connection(app)
#     repository_album = AlbumRepository(connection)
#     repository_artist = ArtistRepository(connection)
#     albums = repository_album.find(album_id)
#     artists = repository_artist.find(album_id)
#     return render_template ("artists/index.html", artists=artists, albums=albums)

######

@app.route('/artists')
def get_artist():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artists = repository.all()
    return render_template ("artists/index.html", artists=artists)

######

@app.route('/artists/<artist_id>')
def get_album_show(artist_id):
    connection = get_flask_database_connection(app)
    repository_artist = ArtistRepository(connection)
    artist = repository_artist.find(artist_id)
    return render_template ("artists/show.html", artist=artist)

######

@app.route("/albums/new")
def get_album_new():
    return render_template("/albums/new.html")

######

@app.route("/albums", methods=["POST"])
def create_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    validator = AlbumValidator(
        request.form['title'],
        request.form['release_year']
    )
    if not validator.is_valid():
        errors = validator.generate_errors()
        return render_template("albums/new.html", errors=errors)
    album = Album(
        None,
        validator.get_valid_title(),
        validator.get_valid_release_year(),
        1
    )
    title = request.form['title']
    release_year = int(request.form['release_year'])
    album = Album(None, title, release_year,1)
    repository.create(album)
    return redirect(f"/albums/{album.id}")


######

@app.route("/artists/new")
def get_artist_new():
    return render_template("/artists/new.html")


######

@app.route("/artists", methods=["POST"])
def create_artist():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    validator = ArtistValidator(
        request.form['name'],
        request.form['genre']
    )
    if not validator.is_valid():
        errors = validator.generate_errors()
        return render_template("artists/new.html", errors=errors)
    artist = Artist(
        None,
        validator.get_valid_name(),
        validator.get_valid_genre()
    )
    name = request.form['name']
    genre = (request.form['genre'])
    artist = Artist(None, name, genre)
    repository.create(artist)
    return redirect(f"/artists/{artist.id}")



if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))


