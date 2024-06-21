## BibTex-UI
This repository contains all code of the BibTex-UI group for the Text Technology project in SS2024.  
We format ACL anthology bibtex files as an SQL database, convert it into XML format and finally display it as an HTML webpage.  

#### [Data](Data)
This folder contains two smaller samples of the original data, one including and one excluding the abstracts. The whole bibtex data with abstracts can be found on the IMS servers at "/mount/studenten-temp1/users/BibtexUI/anthology+abstracts.bib".  

#### Source
|step|file|content|
|:-----|:-----|:-----|
|collect|[prepare_readData.py](prepare_readData.py)|Read bibtex file, convert to SQL.| 
|prepare|[collect_toXML.py](collect_toXML.py)| Convert SQL to XML.|
|prepare|[template_format.xml](template_format.xml)| Template for the XML format.|  

#### [XML_outfiles](XML_outfiles)  
This folder contains all (test-) xml files.
