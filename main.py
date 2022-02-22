import sys
from worker_functions import WorkerFunctions as worker
if __name__ == "__main__":
    workerFunctions = worker(sys.argv[1])
    workerFunctions.runProcess()
