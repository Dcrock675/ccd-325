# Drew Crockett
# Module 7.2
# 11/29/25

import mysql.connector

def main():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Brewer18",
            database="movies"
        )

        cursor = db.cursor()

        # -------------------------------
        # Query 1: All fields from studio
        # -------------------------------
        print("=== Query 1: Studio Table ===")
        cursor.execute("SELECT * FROM studio")
        studios = cursor.fetchall()
        for studio in studios:
            print("Studio Record:", studio)
        print("\n")

        # -------------------------------
        # Query 2: All fields from genre
        # -------------------------------
        print("=== Query 2: Genre Table ===")
        cursor.execute("SELECT * FROM genre")
        genres = cursor.fetchall()
        for genre in genres:
            print("Genre Record:", genre)
        print("\n")

        # -------------------------------
        # Query 3: Movies < 2 hours
        # -------------------------------
        print("=== Query 3: Movies with runtime < 120 minutes ===")
        cursor.execute("SELECT movie_name FROM movie WHERE runtime < 120")
        movies = cursor.fetchall()
        for movie in movies:
            print("Movie Name:", movie[0])
        print("\n")

        # -------------------------------
        # Query 4: Movies grouped by director
        # -------------------------------
        print("=== Query 4: Movies grouped by director ===")
        cursor.execute("SELECT movie_name, director FROM movie GROUP BY director, movie_name")
        films = cursor.fetchall()
        for film in films:
            print("Movie Name: {}\nDirector: {}\n".format(film[0], film[1]))

        # Close connection
        cursor.close()
        db.close()

    except mysql.connector.Error as err:
        print("Error:", err)

if __name__ == "__main__":
    main()
