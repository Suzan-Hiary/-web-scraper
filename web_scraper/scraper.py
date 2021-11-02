import requests 
from bs4 import BeautifulSoup

domain='https://en.wikipedia.org'
history_of_mexico= f'{domain}/wiki/History_of_Mexico'



def get_citations_needed_count(url):
    """ 
    get_citations_needed function 
    takes in a url and returns an 
    integer
    """

    result = requests.get(url)

    html_text = result.text
    print(result.text)
    file=open('history_of_mexico.html','w')
    file.write(html_text)
    file.close()
 

    soup = BeautifulSoup(html_text, "html.parser")
    cites=soup.find_all('a', { "title" : "Wikipedia:Citation needed"})

    return len(cites)





def get_citations_needed_report(url):
    result = requests.get(url)

    html_text = result.text
    soup = BeautifulSoup(html_text, "html.parser")
    results=soup.find_all('a', { "title" : "Wikipedia:Citation needed"})
    list=''
    

    for i in results:
           paragraph=i.parent.parent.parent
           list+=f'{paragraph.text}\n'
    return list


get_citations_needed_count(history_of_mexico)
print(get_citations_needed_count(history_of_mexico))
print(get_citations_needed_report(history_of_mexico))
quit()
