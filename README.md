## Overview

This is based off of the video tutorial available [here.](https://jobqueue.dask.org/en/latest/) It is adapted to run on
UVA's Rivana cluster. 

## Connect to Rivanna 

Replace my username with your username, and enter your password when prompted. If this doesn't work for your setup,
check out more information [here](https://www.rc.virginia.edu/userinfo/rivanna/login/).

    ssh -Y trb5me@rivanna.hpc.virginia.edu 

## Install Software

    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
    chmod +x Miniconda3-latest-Linux-x86_64.sh
    ./Miniconda3-latest-Linux-x86_64.sh
    
Follow all the prompts to install miniconda. Log out, and then log back in through ssh. Once you're back on the
frontend, run the following commands

    conda install dask ipython
    pip install dask-jobqueue

After this all works, you can test that you're able to start up `ipython` and `import` some libraries. Just type 

    ipython

in the console, and then type the `import dask` statements in python to do that. 


## Running Python Code

ssh into the frontend of the cluster. Open up python by typing `ipython`, and then run code like this:

    from dask_jobqueue import SLURMCluster
    cluster = SLURMCluster(cores=40, memory='375GB', queue='standard', project='brown_stats', local_directory='/scratch/trb5me/')
    cluster.scale(jobs=10)  # ask for 10 jobs

This assumes you want to run jobs on a "Standard" queue/partition. A lot of the information about the nodes on that partition comes from [here.](https://www.rc.virginia.edu/userinfo/rivanna/queues/) It is important to realize that you may or may not have access to some of these, and that some queues limit how many nodes/processes you can request.


