###**Playlist Youtube Downloader - Version 1.0**

Utilisation de:
- [youtube-dl](http://rg3.github.io/youtube-dl/)
- [argparse](http://docs.python.org/3/library/argparse.html)
- [os](http://docs.python.org/3/library/os.html)
- [time](http://docs.python.org/3/library/time.html)

---

#####Arguments

- -u / --url	->	Url de la playlist
- -f / --file	->	Chemin du fichier contenant la liste d'url

---

#####Exemples d'utilisation

	python3 main.py -u http://www.youtube.com/...
Extraction audio au format .m4a à partir de l'url d'une playlist

	python3 main.py -f ./listingUrl
Extraction audio au format .m4a à partir d'un fichier contenant une liste d'url
