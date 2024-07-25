## BibTex-UI
This repository contains all code of the BibTex-UI group for the Text Technology project in SS2024.  
We format ACL anthology bibtex files from https://aclanthology.org/ as an SQL database, convert it into XML format and finally display it as an HTML webpage using xslt.  

#### [Data](Data)
This folder contains two smaller samples of the original data, one including and one excluding the abstracts. The whole bibtex data with abstracts can be found on the IMS servers at "/mount/studenten-temp1/users/BibtexUI/anthology+abstracts.bib".  

#### Source
|Step|Path|Content|Run the project|
|:-----|:-----|:-----|:-----|
|Prerequisites| - | - | Establish an ssh connection to the IMS servers and make sure you have access to "/mount/studenten-temp1/users/BibtexUI/".|
|Collect|[prepare_readData.py](prepare_readData.py)|Read bibtex file, convert to SQL.| Run the file (being located in the top folder).|
|Prepare|[collect_toXML.py](collect_toXML.py)| Convert SQL to XML.| Run the file (being located in the top folder).|
|Access|[final_webpage](final_webpage)| Directory including xsl and html files. <br> (According xml file: [XML_outfiles/out_all_formatted.xml](XML_outfiles/out_all_formatted.xml)) | After having created the xml file, use the program xsltproc to create the html file: "xsltproc final_webpage.xsl out_all_formatted.xml > final_webpage.html".|

#### [XML_outfiles](XML_outfiles)  
This folder contains all (test-) xml files. All files are created in [collect_toXML.py](collect_toXML.py).  
Final outputs are [output_all.xml](XML_outfiles/output_all.xml) (whole output, not formatted) and [out_all_formatted.xml](XML_outfiles/out_all_formatted.xml) (whole output, formatted).

#### [Templates](Templates)
This folder contains our original, self-designed templates for xml and html formats.
