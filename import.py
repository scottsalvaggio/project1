import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():

    # Open a file using Python's CSV reader.
    f = open("test.csv")
    reader = csv.reader(f)

    # Skip the first row with column headings
    next(reader, None)

    # Iterate over the rows of the opened CSV file.
    for row in reader:

        # Execute database queries, one per row; then print out confirmation.
        # Convert zip_code (row[0]) to a 5-character string (with leading zeros if needed)
        db.execute("INSERT INTO locations (zip_code, city, state, latitude, longitude, population) \
                    VALUES (:zip_code, :city, :state, :latitude, :longitude, :population)",
                    {"zip_code": str(row[0]).zfill(5), "city": row[1], "state": row[2], "latitude": row[3],
                     "longitude": row[4], "population": row[5]})
        print(f"Added {row[1]}, {row[2]} {row[0]}. Location: ({row[3]}, {row[4]}). Population: {row[5]}.")

    # Technically this is when all of the queries we've made happen!
    db.commit()

if __name__ == "__main__":
    main()