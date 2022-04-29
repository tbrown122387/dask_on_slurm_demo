import dask.array as da
import time

# import dask stuff
from dask.distributed import Client
from dask_jobqueue import SLURMCluster


##############################
# (naive) option pricing     #
# with more computing power! #
##############################

# ask for computing resources and select scheduler
cluster = SLURMCluster(cores=40, 
                       memory='375GB', 
                       queue='standard', 
                       project='brown_stats', 
                       local_directory='/scratch/trb5me/',
                       walltime='02:00:00',
                       interface='ib0')
cluster.scale(jobs=10)  # ask for 10 jobs
client = Client(cluster) # this is the "distributed" scheduler we mentioned in class

# time and run
start = time.time()
returns = da.random.normal(loc=ave_day, scale = std_dev, 
                           size = (num_paths, num_days_into_future))
random_paths = (current_price * da.cumprod(1 + returns, axis = 1))
best_case_scenarios = da.max(da.maximum(0, random_paths - strike), axis=1)
best_case_scenarios.compute()
print('finished in ', time.time() - start, " seconds")


