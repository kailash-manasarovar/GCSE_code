def get_scores():
    import mysql.connector

    db_connection = mysql.connector.connect(user='root', password='password',host='127.0.0.1',database='dancers')

    cursor = db_connection.cursor()

    couple_scores = []

    cursor.execute("""SELECT * FROM Round1""")

    for row in cursor:
        couple = {
            'Couple': row[0],
            'Judge1': row[1],
            'Judge2': row[2],
            'Judge3': row[3],
            'Judge4': row[4],
            'Judge5': row[5]
        }
        couple_scores.append(couple)
    cursor.close()
    return couple_scores


scores = get_scores()
print(scores)