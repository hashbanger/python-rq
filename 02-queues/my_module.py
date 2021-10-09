import time
import requests

def count_words_at_url(url):
    resp = requests.get(url)
    return len(resp.text.split())

def say_hello(name=""):
        return f'Hello {name} from the job!'

def doomed_to_fail(ttl=10, description=None):
    time.sleep(ttl)

    if not description:
        return "This statement won't be returned if job timeout < 10 seconds."
    else:
        return description