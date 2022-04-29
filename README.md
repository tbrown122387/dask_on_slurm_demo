# Demo of Dask on Rivanna 

## Getting Started

This probably shouldn't be the first thing you read about how to get started on Rivanna. If you want more information, head over to [the user guide.](https://www.rc.virginia.edu/userinfo/rivanna/overview/)


## Upload any Required Data and Scripts

Upload to the cluster any data and/or scripts you might need. Do something like this from your local machine's terminal to upload data

    scp /home/taylor/data/cool_data.csv trb5me@rivanna.hpc.virginia.edu:/scratch/trb5me/

If the data set is large, this will take a few minutes. After it is finished, it will be accessible on the frontend at `/scratch/trb5me/`.

Do the following to upload the included example demo script:

    scp /home/taylor/data/monte_carlo_example.py trb5me@rivanna.hpc.virginia.edu:/scratch/trb5me/


## Connect to Frontend

Use [FastX](https://d2czcjcn5aapf5.cloudfront.net/userinfo/rivanna/logintools/fastx/) to log in to the frontend of Rivanna. In your web browser you'll have something that looks like your local machine's desktop.

## Install IDE (optional)

Install any IDE you want. We use Spyder in class, so we'll stick with that. Type the following in a terminal on the remote machine's frontend:

    conda install -c conda-forge spyder-terminal
    
You might have to answer a few yes/no questions. After that, you can open up Spyder by typing the following in your terminal:

    spyder

## Run Python Code

Assuming you `scp`'d the `monte_carlo_example.py` into `/scratch/trb5me/` (perhaps using the code above), you can open up that file in Spyder. Then you can run the script in Spyder (or in other way). The key lines in that file are the following.

    from dask_jobqueue import SLURMCluster
    cluster = SLURMCluster(cores=40, memory='375GB', queue='standard', project='brown_stats', local_directory='/scratch/trb5me/')
    cluster.scale(jobs=10)  # ask for 10 jobs
    client = Client(cluster)

This assumes you want to run jobs on a "Standard" queue/partition. A lot of the information about the nodes on that partition comes from [here.](https://www.rc.virginia.edu/userinfo/rivanna/queues/) It is important to realize that you may or may not have access to some of these, and that some queues limit how many nodes/processes you can request.

If you want to read in that data set we mentioned earlier, you can run something like this.

    import os
    os.chdir("/scratch/trb5me/")
    import dask.dataframe as dd
    my_data = dd.read_csv('cool_data.csv', dtype=dtypes)

However, the attached script does not make use of external data. 

## Observe Performance

When you request resources, you do not instantaneously receive them. You might end up waiting for those resources for a while, depending on how much you requested, and for how long. You can check on the status of your jobs from the command line. Run something like `qstat -u trb5me`. If your code is running slowly, or not at all, that might be explained by the fact that your resource request jobs are still sitting in the queue. This will help you tell if they are. 

Once the resources have been given to you, and after you started running your code, you can get more information about how everything is working by checking out [Dask's diagnostics](https://docs.dask.org/en/stable/diagnostics-distributed.html). To do that, open up a Firefox browser (in FastX on the frontend), and navigate over to `localhost:8787`. 

