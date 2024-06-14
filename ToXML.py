import psycopg2
import xml.etree.ElementTree as ET
import xml.dom.minidom


def xml_tree(all_citations, columns, out_filename):
    # Add root element
    corpus = ET.Element("corpus")
    
    # Populate the XML tree
    for citation in all_citations:
        entry = ET.SubElement(corpus, "entry")

        basicInfo = ET.SubElement(entry, "basicInfo")
        dateInfo = ET.SubElement(entry, "dateInfo")
        extraInfo = ET.SubElement(entry, "extraInfo")

        for col_name, col_value in zip(columns, citation):
            if col_name in ["author", "title", "cite_key"]:
                col_elem = ET.SubElement(basicInfo, col_name)
            elif col_name in ["year", "month"]:
                col_elem = ET.SubElement(dateInfo, col_name)
            elif col_name in ["url", "abstract"]:
                col_elem = ET.SubElement(extraInfo, col_name)
            else:
                continue
            col_elem.text = str(col_value)

    # Write the XML to a file
    tree = ET.ElementTree(corpus)
    tree.write(out_filename)


def convert2XML(out_filename):
    # Connect to the database to fetch information
    conn = psycopg2.connect(
        host="bergbussard",
        database="bibtexui",
        user="takamamo",    # add your username
        password="biui"     # add your password 
    )
    
    cursor = conn.cursor()
    
    # Fetch all the necessary columns
    cursor.execute("""
    SELECT cite_key, title, author, year, month, url, abstract
    FROM bibtex_entries_abstracts
    """)
    all_citations = cursor.fetchall()

    # Define the column names in the order they are fetched
    columns = ["cite_key", "title", "author", "year", "month", "url", "abstract"]
    
    # Draw XML tree
    xml_tree(all_citations, columns, out_filename)
    
    # Close database
    cursor.close()
    conn.close()
    print("Check if data is created.")
    

def beautify_xml(xml_fname):
    dom = xml.dom.minidom.parse(xml_fname) # or xml.dom.minidom.parseString(xml_string)
    pretty_xml_as_string = dom.toprettyxml()
    with open("out_file.xml", 'w') as out:
        out.write(pretty_xml_as_string)
    
    

if __name__ == "__main__":
    out_name = "output_TEST2.xml"
    convert2XML(out_name)
    beautify_xml('/mount/studenten-temp1/users/takamo/TextTech/output_TEST2.xml')
    
