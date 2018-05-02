-- Table: public.friends

-- DROP TABLE public.friends;

CREATE TABLE public.friends
(
    uid integer NOT NULL DEFAULT nextval('users_id_seq'::regclass),
    id integer,
    domain character varying COLLATE pg_catalog."default",
    nickname character varying COLLATE pg_catalog."default",
    screen_name character varying COLLATE pg_catalog."default",
    first_name character varying COLLATE pg_catalog."default",
    last_name character varying COLLATE pg_catalog."default",
    maiden_name character varying COLLATE pg_catalog."default",
    sex integer,
    bdate character varying COLLATE pg_catalog."default",
    city character varying COLLATE pg_catalog."default",
    home_town character varying COLLATE pg_catalog."default",
    country character varying COLLATE pg_catalog."default",
    relation_partner character varying COLLATE pg_catalog."default",
    mobile_phone character varying COLLATE pg_catalog."default",
    home_phone character varying COLLATE pg_catalog."default",
    skype character varying COLLATE pg_catalog."default",
    facebook character varying COLLATE pg_catalog."default",
    facebook_name character varying COLLATE pg_catalog."default",
    twitter character varying COLLATE pg_catalog."default",
    instagram character varying COLLATE pg_catalog."default",
    contacts character varying COLLATE pg_catalog."default",
    photo_max_orig character varying COLLATE pg_catalog."default",
    connections character varying COLLATE pg_catalog."default",
    exports character varying COLLATE pg_catalog."default",
    site character varying COLLATE pg_catalog."default",
    deactivated character varying COLLATE pg_catalog."default",
    hidden character varying COLLATE pg_catalog."default",
    career character varying COLLATE pg_catalog."default",
    education character varying COLLATE pg_catalog."default",
    university character varying COLLATE pg_catalog."default",
    university_name character varying COLLATE pg_catalog."default",
    faculty character varying COLLATE pg_catalog."default",
    faculty_name character varying COLLATE pg_catalog."default",
    graduation character varying COLLATE pg_catalog."default",
    military character varying COLLATE pg_catalog."default",
    occupation character varying COLLATE pg_catalog."default",
    relatives character varying COLLATE pg_catalog."default",
    relation character varying COLLATE pg_catalog."default",
    schools character varying COLLATE pg_catalog."default",
    status character varying COLLATE pg_catalog."default",
    personal character varying COLLATE pg_catalog."default",
    activities character varying COLLATE pg_catalog."default",
    interests character varying COLLATE pg_catalog."default",
    music character varying COLLATE pg_catalog."default",
    movies character varying COLLATE pg_catalog."default",
    tv character varying COLLATE pg_catalog."default",
    books character varying COLLATE pg_catalog."default",
    games character varying COLLATE pg_catalog."default",
    quotes character varying COLLATE pg_catalog."default",
    about character varying COLLATE pg_catalog."default"
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.friends
    OWNER to postgres;