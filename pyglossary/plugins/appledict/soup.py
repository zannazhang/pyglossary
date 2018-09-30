try:
	import bs4 as BeautifulSoup
except:
	import BeautifulSoup

if int(BeautifulSoup.__version__.split(".")[0]) < 4:
	raise ImportError(
		"BeautifulSoup is too old, required at least version 4, " +
		"%r found.\n" % BeautifulSoup.__version__ +
		"Please run `sudo pip3 install lxml beautifulsoup4 html5lib`"
	)


