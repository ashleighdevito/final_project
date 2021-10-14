
CREATE TABLE "Movie" (
    "movie_id" INTEGER   NOT NULL,
    "title" VARCHAR   NOT NULL,
    "movie_rating" VARCHAR   NOT NULL,
    "release_date" DATE   NOT NULL,
    "runtime" INTEGER   NOT NULL,
    "metascore" INTEGER   NOT NULL,
    "imdb_rating" FLOAT   NOT NULL,
    "domestic_boxoffice" INTEGER   NOT NULL,
    "budget" INTEGER   NOT NULL,
    "buzz" INTEGER   NOT NULL,
    CONSTRAINT "pk_Movie" PRIMARY KEY (
        "movie_id"
     )
);

CREATE TABLE "Genre" (
    "genre_id" INTEGER   NOT NULL,
    "genre_name" VARCHAR   NOT NULL,
    CONSTRAINT "pk_Genre" PRIMARY KEY (
        "genre_id"
     )
);

CREATE TABLE "Movie_Genre_Junction" (
    "movie_id" INTEGER   NOT NULL,
    "genre_id" INTEGER   NOT NULL,
    CONSTRAINT "pk_Movie_Genre_Junction" PRIMARY KEY (
        "movie_id","genre_id"
     )
);

CREATE TABLE "Person" (
    "person_id" INTEGER   NOT NULL,
    "name" VARCHAR   NOT NULL,
    CONSTRAINT "pk_Person" PRIMARY KEY (
        "person_id"
     )
);

CREATE TABLE "Role" (
    "role_id" INTEGER   NOT NULL,
    "role_name" VARCHAR   NOT NULL,
    CONSTRAINT "pk_Role" PRIMARY KEY (
        "role_id"
     )
);

CREATE TABLE "Movie_Person_Role_Junction" (
    "movie_id" INTEGER   NOT NULL,
    "person_id" INTEGER   NOT NULL,
    "role_id" INTEGER   NOT NULL,
    CONSTRAINT "pk_Movie_Person_Role_Junction" PRIMARY KEY (
        "movie_id","person_id","role_id"
     )
);

ALTER TABLE "Movie_Genre_Junction" ADD CONSTRAINT "fk_Movie_Genre_Junction_movie_id" FOREIGN KEY("movie_id")
REFERENCES "Movie" ("movie_id");

ALTER TABLE "Movie_Genre_Junction" ADD CONSTRAINT "fk_Movie_Genre_Junction_genre_id" FOREIGN KEY("genre_id")
REFERENCES "Genre" ("genre_id");

ALTER TABLE "Movie_Person_Role_Junction" ADD CONSTRAINT "fk_Movie_Person_Role_Junction_movie_id" FOREIGN KEY("movie_id")
REFERENCES "Movie" ("movie_id");

ALTER TABLE "Movie_Person_Role_Junction" ADD CONSTRAINT "fk_Movie_Person_Role_Junction_person_id" FOREIGN KEY("person_id")
REFERENCES "Person" ("person_id");

ALTER TABLE "Movie_Person_Role_Junction" ADD CONSTRAINT "fk_Movie_Person_Role_Junction_role_id" FOREIGN KEY("role_id")
REFERENCES "Role" ("role_id");

