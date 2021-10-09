from my_module import say_hello
from redis import Redis
from rq import Queue
from datetime import datetime, timedelta
import time

# start a worker in a terminal to listen to this job using `rq worker`
q = Queue(connection=Redis())

# enqueue thhe job to run at October 10, 2021 at 12:04
result = q.enqueue_at(datetime(2021, 10, 9, 12, 4), say_hello)
time.sleep(80)
print(result.result)

# enqueue to run the job in 10 seconds
countdown = 10
result = q.enqueue_in(timedelta(seconds = countdown), say_hello)
time.sleep(countdown + 2) # giving 2 seconds buffer for the worker to complete the job
print(result.result)