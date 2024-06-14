import bibtexparser
import psycopg2
from psycopg2 import sql


def read_bib(filepath):
    # Read the BibTeX file
    with open(filepath, 'r') as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)

    # Access the entries
    entries = bib_database.entries
    print(entries[1])

    return entries


def insert_entry(cursor, entry):
    query = sql.SQL('''
    INSERT INTO bibtex_entries (entry_type, cite_key, title, author, year, journal, booktitle, publisher, note, abstract, keywords)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
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
    cursor.execute(query, data)


def connect_sql(db_entries):

    conn = psycopg2.connect(
        host="bergbussard",
        database="bibtexui",
        user="takamamo",    # add your username
        password="biui"     # add your password 
    )
    
    cursor = conn.cursor()

    # Create the table to store the BibTeX entries
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS bibtex_entries_wabstracts (
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

    data_path = "/mount/studenten-temp1/users/BibtexUI/anthology.bib"
    data_path_samples1 = "/mount/studenten-temp1/users/takamo/TextTech/anthology_samples.bib"
    data_path_samples = '/mount/studenten-temp1/users/takamo/TextTech/anthology+abstracts_short.bib'
    
    #la = read_bib(data_path_samples1)
    bib_db = read_bib(data_path_samples)
    connect_sql(bib_db)
    
