from db.run_sql import run_sql

from models.artist import Artist
from models.album import Album

def save(artist):
    sql = "INSERT INTO artists (name) VALUE (%s) RETURNING *"
    value = [user.name]
    results = run_sql(sql, value)
    id = results[0]['id']
    artist.id = id
    return artist

def delete_all():
    pass

def select(id):
    pass

def albums(artist):
    pass
