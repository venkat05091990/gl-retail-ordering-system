sudo docker build -t gl-ros-app ../gl-retail-ordering-system/fe-be
sudo docker run -it -d -p 5000:5000 -p 3306:3306 gl-ros-app
sudo docker ps -a
