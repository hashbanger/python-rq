from my_module import say_hello
from redis import Redis
from rq import Queue, Retry

q = Queue(connection=Redis())

# Retrying the job upto three times
result = q.enqueue(say_hello, retry=Retry(max=3))

# Retrying the job upto three times at certain intervals
result = q.enqueue(say_hello, retry=Retry(max=3), interval=[10, 20, 30])