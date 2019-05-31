CREATE TABLE restaurant(
   id serial PRIMARY KEY,
   place VARCHAR (2048) NOT NULL,
   address VARCHAR (2048) NOT NULL,
   latitude DECIMAL (8,6) NOT NULL,
   longitude DECIMAL (8,6) NOT NULL,
   tips text NOT NULL
);