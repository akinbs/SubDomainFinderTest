import threading
import requests

target = input("Write target domain: ")
urls = []


class ThreadingGetter(threading.Thread):

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        response = Request(self.url)
        if response:
            print("Subdomain Found ----------->" + self.url)
        else:
            pass

def Request(url):
    try:
        return requests.get(url)
    except:
        pass


def DataThreading(urls_):
    threads = []
    for i in urls_:
        t = ThreadingGetter(i)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()


with open("SubDomainList.txt", "r") as MyList:
    for word in MyList:
        word = word.strip()
        url = "http://" + word + "." + target
        urls.append(url)
    DataThreading(urls)

