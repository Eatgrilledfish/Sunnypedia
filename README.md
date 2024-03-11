# Sunnypedia
**G13 IE website**

This repository contains the Sunnypedia Flask application, which is a web application for aggregating and displaying Sunscreen guide. The application is designed to be deployed using Gunicorn as the WSGI server, with Nginx serving as a reverse proxy to manage incoming requests and provide additional security and performance enhancements.


**Frontend:** Vue3 + Element Plus

**Frontend hosting:** Aws

**Database:** Mysql 8.0 Database 

**Middleware:** Gunicorn

**Backend:** Aws + Flask  + Nginx+ Swagger UI API


**Nginx** plays the role of a reverse proxy server in this configuration. It receives client requests from the Internet and forwards those requests to the backend Gunicorn server based on its configuration. Nginx can also serve static files, perform load balancing, provide SSL termination, among other tasks, thus reducing the load on the backend server and enhancing the overall application's performance and security.


**Gunicorn** holds the role of the backend, running the Flask application, handling business logic, and data processing.

**Nginx** acts as a reverse proxy, situated "in front" of Gunicorn's "backend." It first receives requests from clients, but here the "frontend" is in relation to the server-side architecture, meaning Nginx handles incoming external requests and decides how to communicate with internal services (like Gunicorn).

BacknEnd Api: [13.237.185.73:8000](http://13.237.185.73:8000/)

FrontEnd page: https://aokodaisuki.com/

Database: Mysql
ip:13.237.185.73
port:3306
user: remote_user
password: Sunnypediag13!


#### API
**Surbubs**
https://api.aokodaisuki.com/api/suburbs
**Graph data**
https://api.aokodaisuki.com/api/graph

**Sunscreen calculator**
curl -X 'POST' \
  'https://api.aokodaisuki.com/api/sunscreen' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "gender": "male",
  "height": 0,
  "weight": 0,
  "head": "string",
  "top": "string",
  "bottom": "string",
  "shoes": "string"
}'

**Uv Index Weather**
curl -X 'POST' \
  'https://api.aokodaisuki.com/api/weather' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "suburb": "string"
}'



