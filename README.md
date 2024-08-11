# Augusta-CRM
# reconnect container
docker exec -it 79417d407676f242827d7bc95c7395e8a5ccb6ab9604ff76c417f915510d0ad1 bash

# run image container
docker run -it --gpus -all -p 8000:8000 -v D:\rishi_sunak:/app rkd3d9/django:latest bash 

# Docker commands for firebase
docker run -it -p 9199:9199 -p 9099:9099 -p 9005:9005 -p 9000:9000 -p 8085:8085 -p 8080:8080 -p 5001:5001 -p 5000:5000 -p 4000:4000 -v D:\rishi_sunak:/app --name firebase_auth_db andreysenov/firebase-tools bash
