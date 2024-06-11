import psycopg2
import xml.etree.ElementTree as ET


def xml_tree(rows, columns):
    # add root element
    root = ET.Element("root")
    
    # Populate the XML tree
    for row in rows:
        row_elem = ET.SubElement(root, "row")
        for col_name, col_value in zip(columns, row):
            col_elem = ET.SubElement(row_elem, col_name)
            col_elem.text = str(col_value)

    # Write the XML to a file
    tree = ET.ElementTree(root)
    tree.write("output_TEST.xml")


def convert2XML():
    
    # connect to database to fetch information
    conn = psycopg2.connect(
        host="bergbussard",
        database="bibtexui",
        user="takamamo",    # add your username
        password="biui"     # add your password 
    )
    
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM bibtex_entries")  # FROM <tablename>
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    
    # draw xml tree
    xml_tree(rows, columns)
    
    # close database
    cursor.close()
    conn.close()
    print("Check if data is created.")
    
    

if __name__ == "__main__":
    convert2XML()