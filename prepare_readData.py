import bibtexparser
import psycopg2
from psycopg2 import sql
from pylatexenc.latex2text import LatexNodes2Text
import pickle


# replace all latex special characters, e.g. \`{o} → ò
def replace_special_characters(all_entries):

    for entry in all_entries:
        for key in entry:
            string_replace = entry[key]
            replaced = LatexNodes2Text().latex_to_text(string_replace).replace("\n", " ")
            entry[key] = replaced

    return all_entries


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
    with open("./Data/out_file.pkl", "wb") as f:
        pickle.dump(entries, f)


    # replace characters
    entries_replaced = replace_special_characters(entries)
    return entries_replaced

def process_data(entries):

    language_model = 0
    classification = 0
    corpora = 0
    evaluation = 0
    language_specific = 0
    catch_all = 0

    for ent in entries:
        title = ent.get('title', '').lower()
        abst = ent.get('abstract', '').lower()


        content = title+ " " +abst

        cont = content.split()

        lm = ["language model", "bert"]
        cla = ["classification"]
        corp = ["corpora", "data set", "dataset"]
        ev = ["evaluation"]
        lang = [ "ukrainian", "german", "indian", "hindi", "spanish", "portugese", "greek", "chinese"]

        found_one = False

        for word in cont:
            if not found_one:
                if word in lm:
                    topic = "language model"
                    language_model += 1
                    found_one = True
                elif word in cla:
                    topic = "classification"
                    classification += 1
                    found_one = True
                elif word in corp:
                    topic = "corpora"
                    corpora  += 1
                    found_one = True
                elif word in ev:
                    topic = "evaluation"
                    evaluation += 1
                    found_one = True
                elif word in lang:
                    topic = "language specific"
                    language_specific += 1
                    found_one = True


        if not found_one:
            topic = "catch_all"
            catch_all += 1
        # ent.update({"title": ,"abstract": , "topic": topic})
        ent.update({"topic": topic})

    res_dict = {
            "language_model": language_model,
            "classification": classification,
            "corpora": corpora,
            "evaluation": evaluation,
            "language_specific": language_specific,
            "catch_all": catch_all
            }

    return res_dict, entries



def insert_entry(cursor, entry):
    """
        cursor: accesses the database
        entry (dict): entry from entries to be inserted to posgreSQL database
    """
    query = sql.SQL('''
    INSERT INTO bibtex_entries_abstracts (entry_type, cite_key, title, author, year, month, editor, booktitle, publisher, url, address, abstract, pages, topic)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
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
        entry.get('pages', ''),
        entry.get('topic')
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
        pages TEXT,
        topic TEXT
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
    final_data_path = './Data/anthology+abstracts.bib'
    
    # read data with bibtex parser
    bib_db = read_bib(final_path_data)

    with open("./Data/out_file.pkl", "rb") as f:
        data = pickle.load(f)

    res, processed_data = process_data(data)
    
    # save on sql database 
    #connect_sql(bib_db)

    print(bib_db)
