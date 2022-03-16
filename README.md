# BA_data
Code and Data regarding my Bachelor Thesis with the title "Local management of historic production data of a 3D-Printer"

A local data storage for a 3D printer is build based on the data lake concept. 

- directory "docker" contains the docker files to start node red and minio 
- file "stream.py" which contains the python camera script
- file "exampleFlow.json" which contains the node-red flows for the given example application 
- diretory "Benchmark tests" contains the gcode files and pictures of the results regarding the benchmark tests.

file "exampleFlow.json" is the latest version of the used Node-Red Flows containing following flows:
  - "emulated Printer" which emulates printer data for test purposes
  - "printer AAS" which combines the data from octopi and the camera and communicates with the datalake
  - "datalake AAS" which handles the incoming data and puts it into the data lake
  - "transformations" which handles the transformations done inside the data lake
  - "dashboard" which creates the dashboard

idealy only flow "printer AAS" needs to be modified to use this implementation for other applications

# Install
  ## Install octopi
  
  install the octopi image on an SD following the offical guide: https://octoprint.org/download/
  
  ## install minio and node-red
  
  on a arm system with linux operating system (for example the octopi image mentioned above):
  
  install docker
  
    curl -fsSL https://get.docker.com -o get-docker.sh
    ‍Sudo sh get-docker.sh
    sudo apt-get install libffi-dev libssl-dev
    sudo apt install python3-dev
    sudo apt-get install -y python3 python3-pip
    sudo pip3 install docker-compose
    
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
   
   ## install the python script for camera pictures:
      
   install python
    
    apt-get install python
    
   install pip
   
    apt-get install pip
   
   install socket package
   
    pip install socket
   
   install OpenCV 
   
    pip install pip opencv-contrib-python
   
   run the camera stream script by navigating to the directory of the repo and running
    
    sudo service webcamd stop
    python camera_stream.py
      
# Notice:
    
   - you may need to run the docker and apt-get commands as sudo
   - after changing the nodered docker file you may need to run the following once before starting the containers again in order to rebuild them by:

    docker-compose build
  
   - if installing opencv on the pi leads to problems follow: https://raspberrypi-guide.github.io/programming/install-opencv
      
