import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


def main():

    # Open a file using Python's CSV reader.
    f = open("zips.csv")
    reader = csv.reader(f)

    # Print and skip the first row (which contains column headings).
    line_num = 1
    print(f"Skipped line {line_num} (column headings)")
    next(reader, None)
    line_num += 1

    # Iterate over the rows of the opened CSV file.
    for row in reader:

        # Execute database queries, one per row; then print out confirmation.
        # Convert zip_code (row[0]) to a 5-character string (with leading zeros if needed).
        db.execute("INSERT INTO locations (zip_code, city, state, latitude, longitude, population) \
                    VALUES (:zip_code, :city, :state, :latitude, :longitude, :population)",
                   {"zip_code": str(row[0]).zfill(5), "city": row[1], "state": row[2], "latitude": row[3],
                    "longitude": row[4], "population": row[5]})
        print(f"Added line {line_num}: {row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]}")
        line_num += 1

    # Commit to database.
    db.commit()


if __name__ == "__main__":
    main()