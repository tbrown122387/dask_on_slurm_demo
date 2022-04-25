## Overview

This is based off of the video tutorial available [here.](https://jobqueue.dask.org/en/latest/) It is adapted to run on
UVA's Rivana cluster. 

## Connect to Rivanna 

Replace my username with your username, and enter your password when prompted. If this doesn't work for you, make sure
you have an account on file, and check out more information [here](https://www.rc.virginia.edu/userinfo/rivanna/login/).

    ssh -Y trb5me@rivanna.hpc.virginia.edu 

## Install Software

Install Miniconda and all required packages. For the `wget` command, you can get the download url from their website.

    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
    chmod +x Miniconda3-latest-Linux-x86_64.sh
    ./Miniconda3-latest-Linux-x86_64.sh
    
Follow all the prompts to install miniconda. Log out of the frontend, and then log back in through ssh. Once you're back on the
frontend, run the following commands to install some additional libraries.

    conda install dask ipython
    pip install dask-jobqueue

## Running Python Code


Before logging in, upload to the cluster any data you might need in your program. Do something like this from your local machine

    scp /home/taylor/data/cool_data.csv trb5me@rivanna.hpc.virginia.edu:/scratch/trb5me/

If the data set is large, this will take a few minutes. 

Next, ssh into the frontend of the cluster. Open up python by typing `ipython`, and then run this Python code, or
something like it:

    from dask_jobqueue import SLURMCluster
    cluster = SLURMCluster(cores=40, memory='375GB', queue='standard', project='brown_stats', local_directory='/scratch/trb5me/')
    cluster.scale(jobs=10)  # ask for 10 jobs

This assumes you want to run jobs on a "Standard" queue/partition. A lot of the information about the nodes on that partition comes from [here.](https://www.rc.virginia.edu/userinfo/rivanna/queues/) It is important to realize that you may or may not have access to some of these, and that some queues limit how many nodes/processes you can request.

You can check on the status of your jobs from the command line. Run something like `qstat -u trb5me`. If your code is
running slowly, that might be explained by the fact that your jobs are still sitting in the queue. This will help you
tell if they are. 

If you want to read in that data we mentioned earlier, you can run something like this

    import os
    os.chdir("/scratch/trb5me/")
    import dask.dataframe as dd
    my_data = dd.read_csv('cool_data.csv', dtype=dtypes) 



