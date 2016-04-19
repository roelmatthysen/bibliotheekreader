#!/usr/bin/python
import urllib2
import urllib
import config
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

class Book:
    
    def __init__(self,author,title):
        self.author = author
        self.title = title
        self.id = ""
    def searchstring(self):
        searchstring = self.author + " " + self.title
        return urllib.quote(searchstring)
    def findbibliotheekid(self):
        tree = ET.ElementTree(file=urllib2.urlopen('http://zoeken.mechelen.bibliotheek.be/api/v0/search/?q=' + self.searchstring() + '&authorization=' + config.api['bibliotheekkey']+'&lang=nl'))
        root = tree.getroot()
        print "#"*85
        print "###  ",self.author.ljust(30), self.title.ljust(50)
        print "#"*85

        for result in tree.iter(tag='result'):
            if result.find('formats').find('format').text!="Gebruikerslijst":
                title=result.find('titles').find('title').text
                if result.find('authors')==None:
                    author="Onbekend"
                elif result.find('authors').find('main-author')!=None:
                    author=result.find('authors').find('main-author').text
                elif result.find('authors').find('author')!=None:
                    author=result.find('authors').find('author').text
                else:
                    author="Onbekend"
                id=result.find('id').text
                loantree = ET.ElementTree(file=urllib2.urlopen('http://zoeken.mechelen.bibliotheek.be/api/v0/availability/?id=' + id + '&authorization=' + config.api['bibliotheekkey']+'&lang=nl'))
                for location in loantree.iter(tag='location'):
                    if location.find('location')==None:
                        lname =  location.get('name')
                        loaned = location.find('items').find('item').find('status').text
                        print author.ljust(30)[0:29].encode('utf-8'), title.ljust(50)[0:49].encode('utf-8'), lname.ljust(20),
                        if loaned == "Uitgeleend":
                            print "Uitgeleend tot "+location.find('items').find('item').find('returndate').text
                        else:
                            print "Beschikbaar"
                        
                
                
                


tree = ET.ElementTree(file=urllib2.urlopen('https://www.goodreads.com/review/list/' + config.api['id'] + '?format=xml&key=' + config.api['key'] + '&v=2&shelf=to-read&per_page=200'))
root = tree.getroot()
reviews = root[1]
books = []
for review in tree.iter(tag='book'):
    book = Book(review.find('authors').find('author').find('name').text,review.find('title').text)
    book.findbibliotheekid()
