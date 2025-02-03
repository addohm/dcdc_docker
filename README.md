Django Docker stack using nginx and postgres

Deployment:

1) Clone this repo `git clone https://your_token@github.com/addohm/dcdc_docker.git`
2) Build the docker image (`docker build -t django:latest . --platform=linux/amd64`), or pull it from hub.docker.com
2) Move the .env.example to .env `mv .env.example .env`
3) Make all the necessary changes in the `.env` file
4) 