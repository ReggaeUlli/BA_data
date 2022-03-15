# BA_data
Code and Data regarding my Bachelor Thesis

Dir "Druckversuche" contains the gcode files and pictures of the results regarding the benchmark tests.

Dir "docker-compose" which contains the docker compose file starting node-red and minio

file "stream.py" which contains the python camera script

file "currentFlow" is the latest version of the used Node-Red Flows containing following flows:
  -"emulated Printer" which emulates printer data for test purposes
  -"printer AAS" which combines the data from octopi and the camera and communicates with the datalake
  -"datalake AAS" which handles the incoming data and puts it into the data lake
  -"transformations" which handles the transformations done inside the data lake
  -"dashboard" which creates the dashboard

idealy only flow "printer AAS" needs to be modified to use this implementation for other applications

# Install
  
  ## install and run minio and node-red
  on a arm system with linux operating system and docker installed:
    
  create the docker volumes for persistent data
  
    docker volume create minio_data
    docker volume create node-red_data
  
  Download this repo:
  
    wget https://github.com/ReggaeUlli/lokale_Organisation_von_Produktionsdaten/archive/refs/heads/main.zip
  
  unzip
    
    unzip master.zip
  
  change directory
    
    cd lokale_Organisation_von_Produktionsdaten-main/docker
   
   start
   
    docker-compose up
    
   access node red via 
   
    <ip of host>:1880
   
   access minio via
   
    <ip of host>:9000
    
   laod example flows from the flows.json file and fit for your usecase
   
   ## install and run python script for camera pictures:
      
   install python
    
    sudo apt-get install python
    
   install pip
   
    sudo apt-get install pip
    
   install OpenCV and socket
   
   
   when downloaded the repo as mentioned above just run the
      
# Notice:
    
   - you may need to run the docker commands as sudo
   - after changing the nodered docker file you may need to run the following once before starting the containers again in order to rebuild them
      
    docker-compose build
      
