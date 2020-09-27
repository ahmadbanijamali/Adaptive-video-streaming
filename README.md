# Adaptive video streaming
Adaptive video streaming scenario from Rover using Kuksa running on RPi3.

Two way of running the application: 
1- Clone the repository and deploy each of the services separately:
 ```
 git clone https://github.com/ahmadbanijamali/Adaptive-video-streaming.git
 cd Adaptive-video-streaming
 Python3 speedtest.py
 Python3 videoadaptation.py
 ...
 ```
 
 2- Pull and run the docker image from dockerhub:
 ```
 docker run ahmadbanijamali/adaptivevideo-from-rpi3:v1
 ```
 
