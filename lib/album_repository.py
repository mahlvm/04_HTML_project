from lib.album import Album
class AlbumRepository:

    def __init__ (self, connection):
        self._connection = connection
    
    def all(self):

        rows = self._connection.execute("SELECT * FROM albums")
        return [
            Album (row["id"], row["title"], row["release_year"], row["artist_id"])
            for row in rows
        ]
    
    def create(self, album):
        rows = self._connection.execute(
            "INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s) RETURNING id",
            [album.title, album.release_year, album.artist_id]
        )
        album.id = rows[0]['id']
        return None
    
    def find(self, album_id):
        rows = self._connection.execute("SELECT * FROM albums WHERE id = %s", [album_id])
        row = rows[0]
        return Album(row["id"], row["title"], row["release_year"], row["artist_id"])