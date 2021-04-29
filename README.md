# Django Case Study

This project creates two REST endpoints to conver numbers into english words

## About

This project uses:

-  [Docker](https://www.docker.com/) to create containers

-  [Docker-compose](https://docs.docker.com/compose/) to manage containers

-  [Django](https://www.djangoproject.com/) as Web framework

-  [django rest_framework](https://www.django-rest-framework.org/) for REST endpoint tools

-  [Postgresql](https://www.postgresql.org/) Database for future work purposes (authentication)

  
  

## Set up

  

1. Install Docker and Docker compose

2. Get Docker containers up

`docker-compose up`

  

## Usage

  

The web application has two REST endpoints [POST, GET] under `num_to_english` URL. Both endpoints accept a number and covert it to English words

  

###  GET 
- Request
`curl -XGET 'http://localhost:8000/num_to_english/?number=12345678'`
- Response
```json
{
	"status": "ok",
	"num_to_english": "twelve million three hundred forty five thousand six hundred seventy eight"
}
```
 ### POST
 - Request
```
curl -XPOST 'http://localhost:8000/num_to_english/' \
--header 'Content-Type: application/json' \
--data-raw '{
	"number": "12345678"
}'
```
- Response
```json
{
	"status": "ok",
	"num_to_english": "twelve million three hundred forty five thousand six hundred seventy eight"
}
```

### Bad Request 
- A `BAD REQUEST` **400** status will be sent if the number is not an integer
- A `NOT IMPLEMENTED` **501** status will be sent if there is any other error 

## Future work

PostgreSQL and pyscopg2 are installed in this project. We are able to make migrations and get an **authentication token** table to use this endpoints anywhere. 

