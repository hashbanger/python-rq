from my_module import say_hello
from redis import Redis
from rq import Queue
import time

q = Queue("low", connection=Redis())
# You can also enqueue multiple jobs in bulk with queue.enqueue_many() and Queue.prepare_data():
jobs = q.enqueue_many(
    [
        Queue.prepare_data(say_hello, job_id=f"job-01"),
        Queue.prepare_data(say_hello, kwargs={"name": "prashant"}, job_id=f"job-02"),
    ]
)

time.sleep(2)
print(jobs[0].result)
print(jobs[1].result)

# They can be given to a single pipeline
with q.connection.pipeline() as pipe:
    jobs = q.enqueue_many(
        [
            Queue.prepare_data(say_hello, job_id=f"job-01"),
            Queue.prepare_data(
                say_hello, kwargs={"name": "capeandcode"}, job_id=f"job-02"
            ),
        ]
    )
    pipe.execute()

time.sleep(2)
print(jobs[0].result)
print(jobs[1].result)
