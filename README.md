# Edu-Bot

## How to Get the Bot running by Using the Github Code
Firstly clone the repo locally or Download the source code.

After getting the source code we need to install python and rasa on to system. My recommendation is to download python using miniconda or Anaconda.

>Link for miniconda: https://docs.conda.io/en/latest/miniconda.html

>Link for Anaconda: https://www.anaconda.com/products/individual

After installing the python, it is recommended to create a seperate environment for RASA and install the required libraries into it.( Sometimes the libraries versions may differ for differnet packeges which might cause some dependency issues while using rasa )

Command to create a new Env.

> conda create -n \<Name of Environment> python=3.6

> conda create -n rasa python=3.6

Once the environment is created we can activate it using
> conda activte \<name of environment>

> conda activate rasa

After activating the environment we can install rasa by using
> pip install rasa[full]==2.6

Now we are ready with all the required dependencies. Let's see how we can train our model.

### To train model
We can train our model using below command
> rasa train

### To talk to bot in shell we need to run following two commands in parallel
    > rasa shell
    > rasa run actions
rasa shell will provide us with a command line prompt using which we can have conversation with the bot.

### To see bot working locally with UI
we need first run the following to commands in parallel.
    
    > rasa run -m models --enable-api --cors "*" 
    > rasa run actions
After running the above commands. The next step is to open the <b>index.html</b> file in browser.(index.html file is present with the source code)



## Running the bot using Docker
First docker is required to be installed on the system to use it. It can be downloaded using the given link mentioned below.
> Link: https://docs.docker.com/engine/install/

Once docker is installed we need to create docker image of the project, it can be done using the below mentioned command.
> docker build -t \<Name for image> .

> docker build -t edubot .

After creating image using the above command we can check it with the following command
> docker images

It will list out all available images on the system.

To start docker container with the image bulit in above step we can use below command.

> docker run -it -p 5005:5005 \<name of image to run>

> docker run -it  -p 5005:5005 edubot

If it gives an error port 5005 already in use, their are two things that we can do
1. check if some other container is already running with the same port number and stop it
    - To see list of running container we can use
    > docker ps
    - after seeing which container is running already we can stop it using
    > docker stop \<contaner id>
2. We can change link differnet port number with the docker container and update the same port number in the index.html file. ( *socketUrl* : [ localhost ]: [ port-number ] )
    > docker run -it  -p [ port-number ]:5005 edubot
    - This will map your localhost [ port-number ] to 5005 and that 5005 port is used by docker container

### Some Useful Commands Realted to Docker
- To list running containers
    > docker ps
- To list all containers(running and stoped both)
    > docker ps -a
- To stop Docker container
    > docker stop \<container-id>
- To see available Images
    > docker images
- To remove a docker image
    > docker image rm -f \<image name>
