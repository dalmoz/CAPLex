# http://api.textcaptcha.com/d0s5wjhqfa8k0kwgs004sc8co2ugh85b
import urllib2
 
#import easy to use xml parser called minidom:
from xml.dom.minidom import parseString
#all these imports are standard on most modern python implementations

def parseUrl( url, qTag ):
    #download the file:
    filex = urllib2.urlopen(url)
    #convert to string:
    data = filex.read()
    #close file because we dont need it anymore:
    filex.close()
    #parse the xml you downloaded
    dom = parseString(data)
    #retrieve the first xml tag (<tag>data</tag>) that the parser finds with name tagName:
    xmlTag = dom.getElementsByTagName(qTag)[0].toxml()
    #strip off the tag (<tag>data</tag>  --->   data):
    xmlData=xmlTag.replace('<' + qTag + '>','').replace('</' + qTag +'>','')
    #just print the data
    return xmlData