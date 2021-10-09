from my_module import count_words_at_url
from redis import Redis
from rq import Queue
import time

redis_conn = Redis()
q = Queue("high", connection=redis_conn)

job = q.enqueue(count_words_at_url, "http://nvie.com")
print(job.result)

# buffer time to complete job
time.sleep(2)
print(job.result)