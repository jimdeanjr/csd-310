import mysql.connector
from mysql.connector import errorcode


def show_films(cursor, title):

    cursor.execute("""SELECT genre_name AS Genre, film_name AS Name, film_director
				   AS Director, studio_name AS Studio FROM movies.film, movies.studio, movies.genre
				   WHERE studio.studio_id=film.studio_id AND genre.genre_id=film.genre_id;""")

    films = cursor.fetchall()

    print("\n -- {} --".format(title));

    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2],
                                                                                         film[3]));

config = {
	"user": "root",
	"password": "P@$$w0rd",
	"host": "127.0.0.1",
	"database": "movies",
	"raise_on_warnings": True
}

try:
	db = mysql.connector.connect(**config)

	print("\nDatabase user {} connected to MySQL on host {} with database {}" .format(config["user"], config["host"], config["database"]))

	cursor=db.cursor()
	cursor.execute("SELECT film_name, film_releaseDate FROM movies.film;")
	show_films(cursor, "--DISPLAYING FILMS--");



except mysql.connector.Error as err:
	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print(" The supplied username or password are invalid")

	elif err.errno == errorcode.ER_BAD_DB_ERROR:
		print(" The specified database does not exist")

	else:
		print(err)

finally:
	db.close()
