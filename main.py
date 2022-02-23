import sys
from worker_functions import WorkerFunctions as worker
if __name__ == "__main__":
    workerFunctions = worker(sys.argv[1])
    result = workerFunctions.runProcess()
    for key, val in result.items():
        print(key, val)
