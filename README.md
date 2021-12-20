# Edu-Chatbot

#### To train model 

rasa train 


#### To talk to bot in shell

rasa shell



#### To see bot working locally with UI


 
rasa run -m models --enable-api --cors "*" 


If it gives error port 5005 already in use 
check with
1.  docker ps 
    > if your container is running if yes stop it 
    > and if no container is running and it is still saying the same.
 
2.  rasa run -m models --enable-api --cors "*" -p [ port-number ] 
    > and also make sure that this port number is also present in index.html in *socketUrl* : [ ip-address ]: [ port-number ]


## To run Docker image of chatbot

> *you can replace Edu-Chatbot with your bot name*

docker build -t demo-bot. 

docker run -it  -p 5005:5005 demo-bot:latest


If it gives an error port 5005 already in use

1.  docker run -it  -p [ port-number]:5005 demo-bot:latest 

This will map your localhost [ port-number ] to 5005 and that 5005 port is used by docker container
But make sure  that this port number is also present in IDP.html in *socketUrl* : [ localhost ]: [ port-number ]
#### To run chatbot in shell using docker container

docker run  -it --workdir /app demo-bot bash ./scripts/start_shell.sh


#### To stop Docker container

docker stop <container-id>


#### To remove docker image


docker image rm -f demo-bot:latest


# To connect Personal Website to Server using socket io

1. Made an Folder in server

2. Installed rasa (rasa 2.6.0)
    
    pip3 install -U pip
    pip3 install rasa
    

3. git pull from repo to get the latest code

4.  rasa train 

5. Open html file where you embedded the script from [here](https://github.com/botfront/rasa-webchat)
    ( any html file that can be present locally can be used just make sure
        1. In socketUrl : [ ip-address]:5005 of server )

6. Make sure the port you are mentioning is open  ( from Server UI you can do this )
    ( In our case we had to manually to open port *5005 from Azure server* because rasa by default runs on port 5005 )
7.  rasa run -m models --enable-api --cors "*"  
    *or*
8.  docker build -t demo-bot . 

8.a  docker run -it  -p 5005:5005 demo-bot:latest  

# To stop the Rasa Server connected via socket io

1.  lsof -i:5005  ( to see which service is running on port 5005 and what is the PID)

2.  
    kill $(lsof -t -i:5005)

    or

    kill -9 $(lsof -t -i:5005)