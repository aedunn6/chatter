# chatter

To run container/code: `docker-compose up backend`
 * to explictily build images before starting the container: `docker-compose up --build backend`
 * Test that it's running at http://localhost:18000/test

To stop/remove container: `docker-compose down`
 * to also delete the old db volume: `docker-compose down -v`
