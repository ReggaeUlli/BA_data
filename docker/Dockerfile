FROM nodered/node-red
RUN wget https://github.com/ReggaeUlli/node-red-contrib-minio-all/archive/refs/heads/master.zip
RUN unzip master.zip
RUN npm install ./node-red-contrib-minio-all-master
RUN npm install node-red-contrib-zip
RUN npm install node-red-dashboard
