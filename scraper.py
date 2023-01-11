import requests
from bs4 import BeautifulSoup


# helper parse function
def find_citations(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser").find_all(title="Wikipedia:Citation needed")
    # return in list every parent element, paragraph,  of title property in soup
    return [match.find_parent('p').text for match in soup]


# return length of find citations
def get_citations_needed_count(url):
    return len([find_citations(url)])


# join stripped lines in find citations
def get_citations_needed_report(url):
    return '\n'.join([line.strip() for line in find_citations(url)])


if __name__ == '__main__':
    url = 'https://en.wikipedia.org/wiki/Devonian'
    print(f"Number of citations needed: {get_citations_needed_count(url)}\n")
    print("Citations Needed: ")
    print("\n" + get_citations_needed_report(url) + "\n")
