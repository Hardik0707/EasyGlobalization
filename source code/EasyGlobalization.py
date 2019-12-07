import xml.etree.ElementTree as ET
from googletrans import Translator

def SelectFramework():
    frameworks = [u'ASP.NET']
    return frameworks

def SelectBaseLanguage():
    base_lang = ['en','ar','hi','gu','jp']
    return base_lang

def SelectDestinationLanguage():
    # print(base_lang)
    dest_lang = ['en','ar','hi','gu','jp']
    return dest_lang

def GenerateNewFileDetails(filepath,dest_lang):
    # print(dest_lang)
    filename = 'Resources.'+ dest_lang +'.resx'
    filepath = filepath[:filepath.rindex("\\")+1]
    return filename,filepath
    
def GenerateTranslatedFile(filepath,base_lang,dest_lang):
    xmltree = ET.parse(filepath)
    root = xmltree.getroot()
    translator = Translator()
    for data in root.findall('data'):
        value = data.find('value')
        # print(value.text)
        text = translator.translate(value.text,dest=dest_lang)
        # print(text)
        value.text = text.text
    del translator
    return xmltree

# filepath = 'Resources.resx'
# xmltree = GenerateTranslatedFile(filepath=filepath,base_lang='en',dest_lang='hi')
# xmltree.write('Resource.hi.resx',encoding='utf-8',method='xml',xml_declaration=True)
