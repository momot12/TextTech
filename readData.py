import bibtexparser
import psycopg2
from psycopg2 import sql


def read_bib(filepath):
    # Read the BibTeX file
    with open(filepath, 'r') as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)

    # Access the entries
    entries = bib_database.entries
    print(entries[0])

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
        entry.get('journal', ''),
        entry.get('booktitle', ''),
        entry.get('publisher', ''),
        entry.get('note', ''),
        entry.get('abstract', ''),
        entry.get('keywords', '')
    )
    cursor.execute(query, data)



def connect_sql(db_entries):

    conn = psycopg2.connect(
        host="bergbussard",
        database="ttws2021",
        user="ttws2021",
        password="acid"
    )
    
    cursor = conn.cursor()

    # Create the table to store the BibTeX entries
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS bibtex_entries (
        id SERIAL PRIMARY KEY,
        entry_type TEXT,
        cite_key TEXT,
        title TEXT,
        author TEXT,
        year TEXT,
        journal TEXT,
        booktitle TEXT,
        publisher TEXT,
        note TEXT,
        abstract TEXT,
        keywords TEXT
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
    data_path_samples = "/mount/studenten-temp1/users/takamo/TextTech/anthology_samples.bib"
    
    bib_db = read_bib(data_path_samples)
    connect_sql(bib_db)
    
    
    
    
    """
        Probleme:
        {'pages': '17473--17485', 'url': 'https://aclanthology.org/2024.lrec-main.1519', 'publisher': 'ELRA and ICCL', 'address': 'Torino, Italia', 'year': '2024', 'month': 'May', 'booktitle': 'Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024)', 'editor': 'Calzolari, Nicoletta  and\nKan, Min-Yen  and\nHoste, Veronique  and\nLenci, Alessandro  and\nSakti, Sakriani  and\nXue, Nianwen', 'author': 'Chen, Lei  and\nLi, Bobo  and\nZheng, Li  and\nWang, Haining  and\nMeng, Zixiang  and\nShi, Runfeng  and\nFei, Hao  and\nZhou, Jun  and\nLi, Fei  and\nTeng, Chong  and\nJi, Donghong', 'title': "What Factors Influence {LLM}s{'} Judgments? A Case Study on Question Answering", 'ENTRYTYPE': 'inproceedings', 'ID': 'chen-etal-2024-factors-influence'}
        Traceback (most recent call last):
        File "/mount/studenten-temp1/users/takamo/TextTech/readData.py", line 91, in <module>
            connect_sql(bib_db)
        File "/mount/studenten-temp1/users/takamo/TextTech/readData.py", line 52, in connect_sql
            cursor.execute('''
        psycopg2.errors.InsufficientPrivilege: FEHLER:  keine Berechtigung für Schema public
        LINE 2:     CREATE TABLE IF NOT EXISTS bibtex_entries (
    """