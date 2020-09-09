# Flask React

Configuration
---
For API, "HERE_GEOCODING_API_KEY" parameter should be entered for distance based geocoding agency
If you want to change API port, should be entered PORT in env file and should be change ports ("1996:1996") in docker-compose.yml file
    
    cp default.env .env
    
Install
----
After installation, you should be waiting a few munites for initial data and service deploying

    docker-compose up -d --build

Usage
---
After docker-compose build, you can use API and with postman collections in postman_collections directory you can test API

    http://localhost:1996

Endpoints
---
    service-status | GET |{{baseUrl}}/api/common/
    initial-data | GET |{{baseUrl}}/api/common/inital-data
    get item by id | GET |{{baseUrl}}/api/agencies/{{id}}
    get all agencies items | GET |{{baseUrl}}/api/agencies/
    add agency | POST | {{baseUrl}}/api/agencies/
    delete agency | DELETE | {{baseUrl}}/api/agencies/{{id}}
    get item by id | GET |{{baseUrl}}/api/brokers/{{id}}
    get all brokers items | GET |{{baseUrl}}/api/brokers/
    add broker | POST | {{baseUrl}}/api/brokers/
    delete agency | DELETE | {{baseUrl}}/api/brokers/{{id}}
    get item by id | GET |{{baseUrl}}/api/agencies-domain-whitelist/{{id}}
    get all items | GET |{{baseUrl}}/api/agencies-domain-whitelist/
    add agency domain whitelist | POST | {{baseUrl}}/api/agencies-domain-whitelist/
    delete agency domain whitelist | DELETE | {{baseUrl}}/api/agencies-domain-whitelist/{{id}}

WEB
---
You can reach from below url with default settings

    http://localhost:3000/

