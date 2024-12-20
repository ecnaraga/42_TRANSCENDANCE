# 42_TRANSCENDANCE

Goal (4 people team project)

    - Devellop a responsive web application of a pong game on Google Chrome. We implements the followings features :
      - Deploy the web application using Docker
      - Server side Pong Game (implement an API for game logic)
      - Remote player
      - Matchmaking and Tournament in remote mode
      - Using Django (python language) as backend and PostgreSQL as database
      - Security (https connection and web secure sockets (wss), hashed password, protection against SQL injections/XSS, Two-Factor Authentification (2FA) and JWT)
      - Using Bootstrap to build the frontend
      - Standard user management, authentification
      - Live chat
      - Multi browser compatibility
      - User and games statistics dashboard
    
Launch

    0.Add a .env at the root of the docker-compose and at the root of the backend's Dockerfile
    1.The .env must includes the following environment variables :
      - Required to use POST GRESQL :
        - POSTGRES_PASSWORD
        - POSTGRES_USER
        - POSTGRES_DB
      - Related to django administrator :
        - DJANGO_SUPERUSER_USERNAME
        - DJANGO_SUPERUSER_EMAIL
        - DJANGO_SUPERUSER_PASSWORD
      - Ip that launch the application : can be localhost (127.0.0.1)
        - IP
      - Use by OAuth to be abble to connect directly via 42 school API :
        - CLIENT_ID
        - CLIENT_SECRET
      - Required by Django to secure features such as session encryption, CSRF tokens, ... :
        - SECRET_KEY
      - Related to user that will send a code throw mail to check id before login : 
        - EMAIL_HOST_USER='gcomfor42@gmail.com' 
        - EMAIL_HOST_PASSWORD='wunq pzqs zdcc yndz' 
        - DEFAULT_FROM_EMAIL='Transcendence <gcomfor42@gmail.com>'

    2.To be able to use remote mode : add to the django settings.py your local ip address in the ALLOWED_HOSTS variable
    
    3.Compile with docker compose up --build

    4.In google Chrome browser go to https://localhost:1234/ and begin to navigate
    To connect from another computer in the same network go to https://<local ip address of the computer who launch the docker compose>:1234/ and begin to navigate

    
