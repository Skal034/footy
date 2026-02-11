# footy
Football Database Generator 

Package dependencies :
1. Faker : for generating the actual fake player names as well as the fake city names based on the countries. The fake city names form the basis of the names of the football clubs
Installation : pip install faker
2. GoogleTranslator : The fake names from regions like Korea, Japan, Middle east are in a different language and encoding. These names needed to be translated into english names for universal readability. However there is a caveat to using simple translation to english. Some of these names can be actual phrases which then gets translated into english phrases instead of being just phonetic translation to english. For example, some arabic name may be "الله معك" which would sound like "Allah Maeak" and that should be the actual name. However, it is translated into english literally which then turns out to be "god be with you". 
Installation : pip install deep-translator
