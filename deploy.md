## First Time Deployment
---------------------	
sudo apt-get update
sudo apt install docker.io
git clone https://github.com/bssoft82/gl-retail-ordering-system.git
cd gl-retail-ordering-system

##Deploy FE-BE
-------------
cd bin
./deploy-fe-be.sh

##Deploy Recommendation_services
-------------------------------
./deploy-recommendation.sh