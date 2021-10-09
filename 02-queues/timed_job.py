from my_module import doomed_to_fail
from redis import Redis
from rq import Queue, Retry
import time

redis_conn = Redis()
q = Queue("high", connection=redis_conn)

# This job will fail since the timeout is less than the default job runtime (10 seconds)
job = q.enqueue(doomed_to_fail, job_timeout=5, retry=Retry(max=1))
print(job.result)

# buffer time to complete job
time.sleep(12)
print(job.result)

print("Trying with a job time less than timeout time, this should be successfull")
# We can use args to pass arguments explicitly to the function
# and kwargs to pass keywords arguments that can conflict the RQ parameter keywords.
job = q.enqueue(
    doomed_to_fail,
    job_timeout=5,
    args=(3,),
    kwargs={
        "description": "This message will be returned and variable name is not conflicted"
    },
)
print(job.result)

# buffer time to complete job
time.sleep(12)
print(job.result)
