# Search Overton 28 Jan 2024

* les documents pour le dataset overton sont sur le drive
https://drive.google.com/drive/u/0/folders/1w2cj61q7nVeVbuLuaC0OwLYZfr-DSNMR

* les mots cles et sources sont spécifiées dans le doc
https://docs.google.com/spreadsheets/d/1zb78cbbyqIbdNwbAY0KFmVMM-TA4-5LZZsGX0O95nGg/edit#gid=0

    * on y trouve aussi le mapping entre le nom de l'institution en clair et le mot clef de recherche associé dans Overton.
    Par ex: 'United Nations CEPAL'  =>  'uncepal', 'oecd' => 'oecddiscovery', ...

* La recherche a été faite sur chaque paire (institution, keyword). Soit en tout 29*32 = 928 requètes.

* On obtient 32307 documents uniques

* Le fichier source_keyword_mapping_202401280804.csv a la liste de tous les documents et la / les source(s) et le(s) keyword(s) correspond(s).

* Le nom des fichiers de résultats est construit sur le mode : <institution>_<keyword>.jsonl
par exemple:  euinvestbank_robotics.jsonl : documents trouvés avec le keyword 'robotics' pour l'institution 'euinvestbank'

* les fichiers de résultats ne contiennent que les documents qui n'ont pas deja été trouvé lors d'une requète antérieure.
* les fichier de résultats vides ne sont pas sur le drive.
