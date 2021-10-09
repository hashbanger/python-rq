from my_module import count_words_at_url
from redis import Redis
from rq import Queue
import time

# start a worker in a terminal to listen to this job using `rq worker`
q = Queue(connection=Redis())
result = q.enqueue(count_words_at_url, 'http://google.com')

time.sleep(2) # it takes some time for the worker to get the job done.

print(result.result)