import psycopg2
import xml.etree.ElementTree as ET


def xml_tree(all_citations, columns):
    # add root element
    corpus = ET.Element("corpus")
    
    # Populate the XML tree
    for citation in all_citations:
        basicInfo= ET.SubElement(corpus, "basicInfo")
        #dateInfo = ET.SubElement(corpus, "dateInfo")
        #extraInfo = ET.SubElement(corpus, "extraInfo")
        for col_name, col_value in zip(columns, citation):
            col_elem = ET.SubElement(basicInfo, col_name)
            col_elem.text = str(col_value)

    # Write the XML to a file
    tree = ET.ElementTree(corpus)
    tree.write("output_TEST2.xml")


def convert2XML():
    
    # connect to database to fetch information
    conn = psycopg2.connect(
        host="bergbussard",
        database="bibtexui",
        user="takamamo",    # add your username
        password="biui"     # add your password 
    )
    
    cursor = conn.cursor()
    
    #cursor.execute("SELECT query_to_xml('SELECT author, year FROM bibtex_entries_abstracts', true, false, '');")  # FROM <tablename>
    #rows = cursor.fetchall()
    
    cursor.execute("SELECT author FROM bibtex_entries")
    authors = [row[0] for row in cursor.fetchall()]

    cursor.execute("SELECT query_to_xml('SELECT year FROM bibtex_entries_abstracts', true, false, '');")
    years = [row[0] for row in cursor.fetchall()]
    print(years)
    
    columns = []
    
    # draw xml tree
    #xml_tree(rows, columns)
    
    # close database
    cursor.close()
    conn.close()
    print("Check if data is created.")
    
    

if __name__ == "__main__":
    convert2XML()