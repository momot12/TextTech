import bibtexparser
import psycopg2
from psycopg2 import sql


# function to parse bibtex data using bibtexparser
def read_bib(filepath):
    """
        filepath (str): path to raw bibtex data
        returns entries: list of dictionaries with bibtex information
    """
    # Read the BibTeX file
    with open(filepath, 'r') as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)

    # Access the entries
    entries = bib_database.entries
    #print(entries[1].keys())

    return entries


def insert_entry(cursor, entry):
    """
        cursor: accesses the database
        entry (dict): entry from entries to be inserted to posgreSQL database
    """
    query = sql.SQL('''
    INSERT INTO bibtex_entries_abstracts (entry_type, cite_key, title, author, year, month, editor, booktitle, publisher, url, address, abstract, pages)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ''')
    data = (
        entry.get('ENTRYTYPE', ''),
        entry.get('ID', ''),
        entry.get('title', ''),
        entry.get('author', ''),
        entry.get('year', ''),
        entry.get('month', ''),
        entry.get('editor', ''),
        entry.get('booktitle', ''),
        entry.get('publisher', ''),
        entry.get('url', ''),
        entry.get('address', ''),
        entry.get('abstract', ''),
        entry.get('pages', '')
    )

    # add data to database
    cursor.execute(query, data)


def connect_sql(db_entries):
    """
        db_entries (list[dict]): data to be inserted to database

        this function initialises the sql-database

    """

    conn = psycopg2.connect(
        host="bergbussard",
        database="bibtexui",
        user="takamamo",    # add your username
        password="biui"     # add your password 
    )
    
    cursor = conn.cursor()

    # Create the table to store the BibTeX entries
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS bibtex_entries_abstracts (
        id SERIAL PRIMARY KEY, 
        entry_type TEXT,
        cite_key TEXT,
        title TEXT,
        author TEXT,
        year TEXT,
        month TEXT,
        editor TEXT,
        booktitle TEXT,
        publisher TEXT,
        url TEXT,
        address TEXT,
        abstract TEXT,
        pages TEXT
    )
    ''')
    conn.commit()

    # Insert all entries
    for entry in db_entries:
        insert_entry(cursor, entry)

    # Commit the changes and close the connection
    conn.commit()
    cursor.close()
    conn.close()



if __name__ == "__main__":

    data_path = "/mount/studenten-temp1/users/BibtexUI/anthology.bib" # on IMS server 
    data_path_samples1 = "./Data/anthology_samples.bib" # without abstracts 
    data_path_samples2 = './Data/anthology+abstracts_short.bib' # with abstracts
    
    # read data with bibtex parser
    bib_db = read_bib(data_path_samples2)
    # save on sql database 
    connect_sql(bib_db)
