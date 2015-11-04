from urllib.request import urlopen,unquote
from bs4 import BeautifulSoup
import requests

#busca avançada no google, procura apenas no pt.wikipedia.org um determinado termo, e retorna o link do wikipedia.
def googleSearch(terms):
    stop=False
    results = requests.get("https://www.google.com.br/search",params={'h1':'pt-BR','q':terms,'as_sitesearch':'pt.wikipedia.org'},headers={'User-Agent': 'Mozilla/41.0.1'})
    soup = BeautifulSoup(results.text, 'html.parser')
    for tag in soup.find_all('a'):
        var = tag.get('href')
        if(var.__contains__('pt.wikipedia.org/wiki') and not stop):
            link = var
            stop=True

    url = (link.replace('&','=').split('='))
    return unquote(url[1])

#retorna uma lista de termos relevantes(tag <a></a> e <b></b>)do corpo do texto de uma pagina do wikipedia.
def crawlerWiki(terms):
    results=[]
    try:
        page = urlopen(googleSearch(terms)).read()
        soup = BeautifulSoup(page, 'html.parser')
        for tag in soup.find_all(["a", "b"]):
            if(tag.parent.name=='p'):
                try:
                    int(tag.string)
                except:
                    results.append(tag.string.lower())
    except:
        pass
    finally:
        return results

