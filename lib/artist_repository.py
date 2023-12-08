from lib.artist import Artist
class ArtistRepository:
    
    def __init__ (self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM artists")
        return [
            Artist (row["id"], row["name"], row["genre"])
            for row in rows
        ]
    def create(self, artist):
        rows = self._connection.execute(
            "INSERT INTO artists (name, genre) VALUES (%s, %s) RETURNING id",
            [artist.name, artist.genre]
        )
        artist.id = rows[0]['id']
        return None
    
    def find(self, artist_id):
        rows = self._connection.execute("SELECT * FROM artists WHERE id = %s", [artist_id])
        row = rows[0]
        return Artist(row["id"], row["name"], row["genre"])