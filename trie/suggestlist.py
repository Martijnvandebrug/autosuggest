import xml.etree.ElementTree as ET

class Suggestlist:
    def __init__(self):
        self.words = dict()

    def addWords(self, xml, element, attrib):
        root = ET.parse(xml).getroot()

        for query in root.iter(element):
            self.words[query.attrib[attrib]]=int(query.text)

    def starts_with_prefix(self, prefix):
        newWords= dict()
        for key, value in self.words.iteritems():
            if(str(key).startswith(prefix)):
                print key
