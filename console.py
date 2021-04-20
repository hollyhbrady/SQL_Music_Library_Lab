import pdb
from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

album_repository.delete_all()
artist_repository.delete_all()

artist_1 = Artist("Frank Turner")
artist_2 = Artist("Taylor Swift")

artist_repository.save(artist_1)
artist_repository.save(artist_2)

album_1 = Album("Be More Kind", "Punk", artist_1)
album_2 = Album("Red", "Pop", artist_2)

album_repository.save(album_1)
album_repository.save(album_2)


pdb.set_trace()
