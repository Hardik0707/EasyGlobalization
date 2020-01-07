import xml.etree.ElementTree as ET
from googletrans import Translator

LANGUAGES = {'english': 'en',
                 'afrikaans': 'af',
                 'albanian': 'sq',
                 'amharic': 'am',
                 'arabic': 'ar',
                 'armenian': 'hy',
                 'azerbaijani': 'az',
                 'basque': 'eu',
                 'belarusian': 'be',
                 'bengali': 'bn',
                 'bosnian': 'bs',
                 'bulgarian': 'bg',
                 'catalan': 'ca',
                 'cebuano': 'ceb',
                 'chichewa': 'ny',
                 'chinese (simplified)': 'zh-cn',
                 'chinese (traditional)': 'zh-tw',
                 'corsican': 'co',
                 'croatian': 'hr',
                 'czech': 'cs',
                 'danish': 'da',
                 'dutch': 'nl',
                 'esperanto': 'eo',
                 'estonian': 'et',
                 'filipino': 'tl',
                 'finnish': 'fi',
                 'french': 'fr',
                 'frisian': 'fy',
                 'galician': 'gl',
                 'georgian': 'ka',
                 'german': 'de',
                 'greek': 'el',
                 'gujarati': 'gu',
                 'haitian creole': 'ht',
                 'hausa': 'ha',
                 'hawaiian': 'haw',
                 'hebrew': 'iw',
                 'hindi': 'hi',
                 'hmong': 'hmn',
                 'hungarian': 'hu',
                 'icelandic': 'is',
                 'igbo': 'ig',
                 'indonesian': 'id',
                 'irish': 'ga',
                 'italian': 'it',
                 'japanese': 'ja',
                 'javanese': 'jw',
                 'kannada': 'kn',
                 'kazakh': 'kk',
                 'khmer': 'km',
                 'korean': 'ko',
                 'kurdish (kurmanji)': 'ku',
                 'kyrgyz': 'ky',
                 'lao': 'lo',
                 'latin': 'la',
                 'latvian': 'lv',
                 'lithuanian': 'lt',
                 'luxembourgish': 'lb',
                 'macedonian': 'mk',
                 'malagasy': 'mg',
                 'malay': 'ms',
                 'malayalam': 'ml',
                 'maltese': 'mt',
                 'maori': 'mi',
                 'marathi': 'mr',
                 'mongolian': 'mn',
                 'myanmar (burmese)': 'my',
                 'nepali': 'ne',
                 'norwegian': 'no',
                 'pashto': 'ps',
                 'persian': 'fa',
                 'polish': 'pl',
                 'portuguese': 'pt',
                 'punjabi': 'pa',
                 'romanian': 'ro',
                 'russian': 'ru',
                 'samoan': 'sm',
                 'scots gaelic': 'gd',
                 'serbian': 'sr',
                 'sesotho': 'st',
                 'shona': 'sn',
                 'sindhi': 'sd',
                 'sinhala': 'si',
                 'slovak': 'sk',
                 'slovenian': 'sl',
                 'somali': 'so',
                 'spanish': 'es',
                 'sundanese': 'su',
                 'swahili': 'sw',
                 'swedish': 'sv',
                 'tajik': 'tg',
                 'tamil': 'ta',
                 'telugu': 'te',
                 'thai': 'th',
                 'turkish': 'tr',
                 'ukrainian': 'uk',
                 'urdu': 'ur',
                 'uzbek': 'uz',
                 'vietnamese': 'vi',
                 'welsh': 'cy',
                 'xhosa': 'xh',
                 'yiddish': 'yi',
                 'yoruba': 'yo',
                 'zulu': 'zu',
                 'Filipino': 'fil',
                 'Hebrew': 'he'}


def LanguageToLangCode(lang):
    global LANGUAGES
    return LANGUAGES[lang]

def SelectFramework():
    frameworks = [u'ASP.NET']
    return frameworks

def SelectBaseLanguage():
    global LANGUAGES
    return list(LANGUAGES.keys())

def SelectDestinationLanguage():
    global LANGUAGES
    return list(LANGUAGES.keys())

def GenerateNewFileDetails(filepath, dest_lang):
    filename = 'Resources.' + LanguageToLangCode(dest_lang) + '.resx'
    filepath = filepath[:filepath.rindex("\\")+1]
    return filename, filepath

def GenerateTranslatedFile(filepath, base_lang, dest_lang):
    base_lang = LanguageToLangCode(base_lang)
    dest_lang = LanguageToLangCode(dest_lang)
    xmltree = ET.parse(filepath)
    root = xmltree.getroot()
    translator = Translator()
    for data in root.findall('data'):
        value = data.find('value')
        # print(value.text)
        text = translator.translate(value.text, dest=dest_lang)
        # print(text)
        value.text = text.text
    del translator
    return xmltree

# filepath = 'Resources.resx'
# xmltree = GenerateTranslatedFile(filepath=filepath,base_lang='en',dest_lang='hi')
# xmltree.write('Resource.hi.resx',encoding='utf-8',method='xml',xml_declaration=True)

