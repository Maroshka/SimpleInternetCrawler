from urllib2 import *
from bs4 import BeautifulSoup
import re
import random 

def getInternalLinks(bs, currentUrl):
	intLinks = []
	for link in bs.findAll('a',href=re.compile(r'^(/|.'+currentUrl+')')):
		if 'href' in link.attrs and link['href'] not in intLinks:
			intLinks.append(link['href'])

	return intLinks

def strip(url):
	domain = url.replace('http://', '').replace('www','').split('/')[0]
	return domain


def getExternalLinks(bs, currentUrl):
	ext = []
	for link in bs.findAll('a',href=re.compile(r'^(http|www)((?!'+currentUrl+').)*$')):
		if 'href' in link.attrs and link['href'] not in ext:
			ext.append(link['href'])

	return ext

def crawl(initUrl):
	html = urlopen(initUrl)
	bs = BeautifulSoup(html)
	domain = strip(initUrl)
	links = getExternalLinks(bs, domain)
	if len(links) == 0:
		links = getInternalLinks(bs, domain)
		if len(links) != 0:
			golink = links[random.randint(0, len(links)-1)]
			print golink
			try:
				crawl(golink) 
			except:
				golink = links[random.randint(0, len(links)-1)]
				print golink
				crawl(golink) 
		else:
			print "Think youre funny, ha?"


	else:
		golink = links[random.randint(0, len(links)-1)]
		print golink
		try:
			crawl(golink) 
		except:
			golink = links[random.randint(0, len(links)-1)]
			print golink
			crawl(golink) 


if __name__ == '__main__':
	crawl("http://oreilly.com")
	

