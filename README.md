
[![HitCount](http://hits.dwyl.io/Hardik0707/EasyGlobalization.svg)](http://hits.dwyl.io/Hardik0707/EasyGlobalization)

# EasyGlobalization
Globalization is a process of designing applications intended for users of different languages across the Globe. Frameworks like ASP.Net, Java Struts or Java Spring provides an easy structure to create Resource file/Properties file for different languages but as a developer it is very difficult and time consuming activity, for languages other than local languages developer needs to translate it from one base  language to require language. EasyGlobalization is a tool for creating a resource file(for ASP.Net) in different languages with the help of one resource file.  

### Download
* Please Download latest Executable from [here](https://github.com/Hardik0707/EasyGlobalization/releases).

### Usage
1. Download and run Executable file or main.py
2. Select Framework (Right now I have made only for ASP.Net, For Struts/Spring stay tuned). 
3. Select Base Language of already been created resource file.
4. Select Destination Language.
5. Select resource file.
6. Click on Generate and wait till it completes the process.

### Make Executable for cross-platform OS
1. Install [Python 3.6+](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/reference/pip_install/)  
2. Install PyInstaller
```
pip install PyInstaller
```
and other packages like [googletrans](https://pypi.org/project/googletrans/), [wxPython](https://www.wxpython.org/) and [xml.etree.ElementTree](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.ElementTree)

3. Run command
```
Pyinstaller -F main.py EasyGlobalization.py --noconsole --name EasyGlobalization
```
### Why I made this?
Translating few Words and Sentences into specific language is painless but it is laborious when a large number of words required to translate into multiple languages for project. So it's better to automate this effortful activity and spend more time into actual development.    

### Authors
**Hardik Thakkar**  - [Hardik0707](https://github.com/Hardik0707)

### License
This project is licensed under the MIT - see the [LICENSE](./LICENSE) file for details
