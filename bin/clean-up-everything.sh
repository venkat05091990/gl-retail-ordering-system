sudo docker rm $(sudo docker ps -a -q)
sudo docker rmi $(sudo docker images)
git reset --hard
git pull
