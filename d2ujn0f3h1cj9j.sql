-- Adminer 4.6.3-dev PostgreSQL dump

\connect "d2ujn0f3h1cj9j";

DROP TABLE IF EXISTS "check_ins";
DROP SEQUENCE IF EXISTS check_ins_id_seq;
CREATE SEQUENCE check_ins_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1;

CREATE TABLE "public"."check_ins" (
    "id" integer DEFAULT nextval('check_ins_id_seq') NOT NULL,
    "user_id" integer NOT NULL,
    "location_id" integer NOT NULL,
    "comment" character varying,
    CONSTRAINT "check_ins_pkey" PRIMARY KEY ("id"),
    CONSTRAINT "check_ins_user_id_location_id_key" UNIQUE ("user_id", "location_id"),
    CONSTRAINT "check_ins_location_id_fkey" FOREIGN KEY (location_id) REFERENCES locations(id) NOT DEFERRABLE,
    CONSTRAINT "check_ins_user_id_fkey" FOREIGN KEY (user_id) REFERENCES users(id) NOT DEFERRABLE
) WITH (oids = false);


DROP TABLE IF EXISTS "locations";
DROP SEQUENCE IF EXISTS locations_id_seq;
CREATE SEQUENCE locations_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1;

CREATE TABLE "public"."locations" (
    "id" integer DEFAULT nextval('locations_id_seq') NOT NULL,
    "zip_code" character varying NOT NULL,
    "city" character varying NOT NULL,
    "state" character varying NOT NULL,
    "latitude" numeric,
    "longitude" numeric,
    "population" integer,
    CONSTRAINT "locations_pkey" PRIMARY KEY ("id"),
    CONSTRAINT "locations_zip_code_key" UNIQUE ("zip_code")
) WITH (oids = false);


DROP TABLE IF EXISTS "users";
DROP SEQUENCE IF EXISTS users_id_seq;
CREATE SEQUENCE users_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1;

CREATE TABLE "public"."users" (
    "id" integer DEFAULT nextval('users_id_seq') NOT NULL,
    "username" character varying NOT NULL,
    "password" character varying NOT NULL,
    CONSTRAINT "users_pkey" PRIMARY KEY ("id"),
    CONSTRAINT "users_username_key" UNIQUE ("username")
) WITH (oids = false);


-- 2018-07-12 15:23:17.273666+00
