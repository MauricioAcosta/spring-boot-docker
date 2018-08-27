#!/usr/bin/env bash

gradle clean build

# rationale: Wait for postgres container to become available
# link: https://cstan.io/?p=8620&lang=en
printf "Wait a moment while loading the database."
while ! PGPASSWORD='postgres' psql -h postgres -U postgres -p 5432 -l &> /dev/null
do
  printf "."
  sleep 2
done
printf "\n"

java -jar build/libs/*.jar
