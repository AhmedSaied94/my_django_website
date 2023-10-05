docker compose -f docker-compose-local.yml down
docker build -t ahmedsaied94/saied_back_image:latest .
docker compose -f docker-compose-local.yml up