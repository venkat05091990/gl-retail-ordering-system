cp /home/ubuntu/*.sav gl-retail-ordering-system/Recommendation_services/
sudo docker build -t gl-ros-app-recommendation ../Recommendation_services/.
sudo docker run -it -d -p 8000:8000 gl-ros-app-recommendation
sudo docker ps -a
