--
-- PostgreSQL database dump
--

-- Dumped from database version 12.5 (Ubuntu 12.5-1.pgdg20.04+1)
-- Dumped by pg_dump version 12.5 (Ubuntu 12.5-1.pgdg20.04+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: album; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.album (
    album_id integer NOT NULL,
    album_name character varying(100),
    date_released timestamp without time zone,
    artist_id integer NOT NULL
);


--
-- Name: album_album_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.album_album_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: album_album_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.album_album_id_seq OWNED BY public.album.album_id;


--
-- Name: alias; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.alias (
    alias_id integer NOT NULL,
    alias_name character varying(50),
    user_id integer
);


--
-- Name: alias_alias_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.alias_alias_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: alias_alias_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.alias_alias_id_seq OWNED BY public.alias.alias_id;


--
-- Name: artist; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.artist (
    artist_id integer NOT NULL,
    artist_name character varying(100),
    "Country" character varying(50),
    gross_worth integer
);


--
-- Name: artist_artist_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.artist_artist_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: artist_artist_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.artist_artist_id_seq OWNED BY public.artist.artist_id;


--
-- Name: playlist; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.playlist (
    id integer NOT NULL,
    tracks_id integer NOT NULL
);


--
-- Name: tracks; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.tracks (
    tracks_id integer NOT NULL,
    tracks_name character varying(100),
    date_released timestamp without time zone,
    genre character varying(50),
    artist_id integer NOT NULL,
    album_id integer NOT NULL
);


--
-- Name: tracks_tracks_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.tracks_tracks_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: tracks_tracks_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.tracks_tracks_id_seq OWNED BY public.tracks.tracks_id;


--
-- Name: user; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."user" (
    id integer NOT NULL,
    email character varying(320) NOT NULL,
    password character varying(400) NOT NULL,
    first_name character varying(50),
    "Surname" character varying(50),
    "Age" integer,
    "Address" character varying(100),
    "City" character varying(50),
    "State" character varying(50),
    "Country" character varying(50),
    "Postcode" integer,
    token character varying(500)
);


--
-- Name: user_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.user_id_seq OWNED BY public."user".id;


--
-- Name: album album_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.album ALTER COLUMN album_id SET DEFAULT nextval('public.album_album_id_seq'::regclass);


--
-- Name: alias alias_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.alias ALTER COLUMN alias_id SET DEFAULT nextval('public.alias_alias_id_seq'::regclass);


--
-- Name: artist artist_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.artist ALTER COLUMN artist_id SET DEFAULT nextval('public.artist_artist_id_seq'::regclass);


--
-- Name: tracks tracks_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.tracks ALTER COLUMN tracks_id SET DEFAULT nextval('public.tracks_tracks_id_seq'::regclass);


--
-- Name: user id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."user" ALTER COLUMN id SET DEFAULT nextval('public.user_id_seq'::regclass);


--
-- Data for Name: album; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.album (album_id, album_name, date_released, artist_id) FROM stdin;
1	Crystal	1976-09-03 00:00:00	8
2	Allison	2015-09-02 00:00:00	2
3	Richard	1985-10-13 00:00:00	5
4	Bradley	1981-09-08 00:00:00	5
5	Michael	2011-06-15 00:00:00	4
6	Todd	2008-09-23 00:00:00	1
7	James	1989-06-13 00:00:00	2
8	James	1991-10-12 00:00:00	9
9	Whitney	2003-09-05 00:00:00	6
10	Erin	2010-02-17 00:00:00	5
\.


--
-- Data for Name: alias; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.alias (alias_id, alias_name, user_id) FROM stdin;
\.


--
-- Data for Name: artist; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.artist (artist_id, artist_name, "Country", gross_worth) FROM stdin;
1	Michael Armstrong	Liberia	15273358
2	Jason Flores	Norfolk Island	47819054
3	Alexandra Brown	Portugal	47978988
4	Timothy Rogers	Oman	26752158
5	April Ruiz	Timor-Leste	47572466
6	Jake Morrison	Comoros	46309997
7	Samuel Rivera	Bhutan	43876106
8	Jose Martinez	Zimbabwe	37892875
9	Evan Johnson	Western Sahara	31371797
10	Aaron Collins	Kenya	28707220
\.


--
-- Data for Name: playlist; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.playlist (id, tracks_id) FROM stdin;
5	8
9	6
5	6
9	9
3	7
6	4
3	3
5	1
5	5
6	9
10	3
8	3
1	9
\.


--
-- Data for Name: tracks; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.tracks (tracks_id, tracks_name, date_released, genre, artist_id, album_id) FROM stdin;
1	Jeremy	1995-09-30 00:00:00	Tina	1	9
2	Jason	2019-03-05 00:00:00	Chelsea	5	4
3	Neil	1997-05-18 00:00:00	Richard	1	3
4	Amy	2006-10-24 00:00:00	James	4	1
5	Robert	2005-10-31 00:00:00	Alexis	8	4
6	Robert	2010-10-27 00:00:00	Ryan	4	4
7	Jason	2018-05-26 00:00:00	Roberta	9	4
8	Randall	2006-07-19 00:00:00	Paula	4	6
9	Jennifer	1983-02-24 00:00:00	Heather	8	2
10	Dylan	1994-06-08 00:00:00	Reginald	4	4
\.


--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public."user" (id, email, password, first_name, "Surname", "Age", "Address", "City", "State", "Country", "Postcode", token) FROM stdin;
1	test0@test.com	$2b$12$kWGF8Ll5X4BBF4X8z.eIAuRv/cAakJ369sYjtCZNsLkSThhukZSEu	Brent	Joe	26	568 Darrell Curve\nNew Jody, MA 72013	West Matthew	New Jersey	Kiribati	1009	eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MDkzMjQxMTQsIm5iZiI6MTYwOTMyNDExNCwianRpIjoiNGRiOTk0NTgtNTMwOC00OGVhLTk1NWYtZTc3MzU5MjFmNTlkIiwiZXhwIjoxNjA5NDEwNTE0LCJpZGVudGl0eSI6IjEiLCJmcmVzaCI6ZmFsc2UsInR5cGUiOiJhY2Nlc3MifQ.lQo0LJIqXkMOz8JDOm21avmBTIhY02B00BbSTdfXX54
2	test1@test.com	$2b$12$SWw4/j/dZmi.YYc8H8xIf.mlGKzP5nW9X.dqAbrbvJ8udlS/g38j6	Joshua	Audrey	23	58688 Bradford Branch\nNorth Jessica, IN 83995	East Madelinemouth	Rhode Island	Heard Island and McDonald Islands	1455	eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MDkzMjQxMTQsIm5iZiI6MTYwOTMyNDExNCwianRpIjoiZThlMjVjZjctMzAzNi00NTg4LTg0ZDMtODA3ODM2ODMyOWY5IiwiZXhwIjoxNjA5NDEwNTE0LCJpZGVudGl0eSI6IjIiLCJmcmVzaCI6ZmFsc2UsInR5cGUiOiJhY2Nlc3MifQ.6oko9iToDnVzKWn98WVQZ2gU2nWT7mGshsjLTqjDBH8
3	test2@test.com	$2b$12$7m9F.UoaCOUKZQpUhLAXTOt/da6kNgpFqkTR8r1Pnq1aWjqH78Sty	Michelle	Stacey	18	783 Kristina Plain\nBowmanville, DE 38237	Port Joseph	Hawaii	United Kingdom	2787	eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MDkzMjQxMTUsIm5iZiI6MTYwOTMyNDExNSwianRpIjoiZGNiYzI0ZjMtMTk0OS00ODQ1LTg1MWEtYTJkNTVmMzkwNjllIiwiZXhwIjoxNjA5NDEwNTE1LCJpZGVudGl0eSI6IjMiLCJmcmVzaCI6ZmFsc2UsInR5cGUiOiJhY2Nlc3MifQ.FFzEX34R9gEeTKxN9w3NhWDdQSe2mcI7No1nLadZ6Yg
4	test3@test.com	$2b$12$5CyAf5NsD/5hBA9/BuuP3ewOQ9ulH/vWxl.hCQk4UR1M1OJc9XmcK	Shane	James	27	40372 Richardson Springs\nNew Yvonnehaven, ID 70000	Normanborough	Massachusetts	Bhutan	2809	eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MDkzMjQxMTUsIm5iZiI6MTYwOTMyNDExNSwianRpIjoiODA4ZTdlODktYTdmMS00ZTAxLTgxZDAtY2VkN2MwNzhlZDEwIiwiZXhwIjoxNjA5NDEwNTE1LCJpZGVudGl0eSI6IjQiLCJmcmVzaCI6ZmFsc2UsInR5cGUiOiJhY2Nlc3MifQ.PD0ympm0X4ibSs-sefK7YGkY5hiAdBUR6s88_b6p4t0
5	test4@test.com	$2b$12$UVqujmgDv5.nRIqXQTsR0uqALE050kZ/ltMgGk4X/icuwbKcKQQyi	Shannon	Stephanie	19	171 Roy Falls\nBrittanyborough, NC 72994	Fitzgeraldburgh	Iowa	Moldova	2273	eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MDkzMjQxMTUsIm5iZiI6MTYwOTMyNDExNSwianRpIjoiZDBhYjdmOTUtOTRmNC00NDc4LWJkOWYtMGE3ZDQxMDNkYzIzIiwiZXhwIjoxNjA5NDEwNTE1LCJpZGVudGl0eSI6IjUiLCJmcmVzaCI6ZmFsc2UsInR5cGUiOiJhY2Nlc3MifQ.vNeMSEaTH2IaHQo-sXRI9RernfiORHhQPcT616FugQ0
6	test5@test.com	$2b$12$spWJrydYaXN8llfHGUm0Bud7fV9A4Arj1rYo.OKaqWv84TaZqxrT6	Michael	Shawn	59	7451 Crawford Circle Suite 310\nWallsside, MD 14693	Orozcoside	Montana	Netherlands Antilles	1616	eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MDkzMjQxMTUsIm5iZiI6MTYwOTMyNDExNSwianRpIjoiNTFiMDRiNDQtYWZjNi00NDkxLTkzNTctNzViMmUzNzM2MGNkIiwiZXhwIjoxNjA5NDEwNTE1LCJpZGVudGl0eSI6IjYiLCJmcmVzaCI6ZmFsc2UsInR5cGUiOiJhY2Nlc3MifQ.BkPUU0Atg9ppP9S5xUpWGJu7Zs4K8OCLoIN4Az4HD4I
7	test6@test.com	$2b$12$Gb8jJambVprvWDgbBIGrEu3OCUTls9OwFpjqSsFtzPi8nRAvFPhVC	Luis	Laurie	30	36494 Kelsey Bypass Suite 800\nMorrisland, CO 20906	Robertstad	New York	New Caledonia	2107	eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MDkzMjQxMTUsIm5iZiI6MTYwOTMyNDExNSwianRpIjoiMDk4YWI1ZjAtZDE1ZC00MzQ4LWE0NzItZDc5NjJiZGI1OTcxIiwiZXhwIjoxNjA5NDEwNTE1LCJpZGVudGl0eSI6IjciLCJmcmVzaCI6ZmFsc2UsInR5cGUiOiJhY2Nlc3MifQ.vjgHCDLZqDVWINFn-_IfYWsti6y9V8rciNPV4IBqnMk
8	test7@test.com	$2b$12$CR4OLv4cgrd.4DekbX58geR.FnENX8S/MmuOvCTWQUxLTEUqP1RfW	Calvin	Jennifer	32	44442 Jack Park\nEatonborough, CO 59280	East Peter	Connecticut	Palestinian Territory	1293	eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MDkzMjQxMTYsIm5iZiI6MTYwOTMyNDExNiwianRpIjoiY2U5YTU1MTAtNWIzZi00MjdkLWJlNmUtZTU5MDlmZTY2ZjBjIiwiZXhwIjoxNjA5NDEwNTE2LCJpZGVudGl0eSI6IjgiLCJmcmVzaCI6ZmFsc2UsInR5cGUiOiJhY2Nlc3MifQ.aznocnz1mxNzbJIEZeyS9lqk44-h_LqWmPNRAp2SCoI
9	test8@test.com	$2b$12$v/R0xuiF9PIqqTAQp59.n.RCYk8jQAIgqic/n5R7rhErHgG3kUijm	Jacob	Matthew	46	7736 Casey Ranch\nPort Jeffreytown, CT 89602	Timothyfort	Arkansas	Swaziland	1567	eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MDkzMjQxMTYsIm5iZiI6MTYwOTMyNDExNiwianRpIjoiYzcwZTQ5N2ItZTcyZC00NGZmLTg0YzYtNWI2ZWMyNjQ2OTRkIiwiZXhwIjoxNjA5NDEwNTE2LCJpZGVudGl0eSI6IjkiLCJmcmVzaCI6ZmFsc2UsInR5cGUiOiJhY2Nlc3MifQ.TwEwY0iFeIhVP4os1GK33DUUl6sco2P9hzdJLnpubGg
10	test9@test.com	$2b$12$XuBApq3EWhobQ2CV5jDtrep698IkZFQvuLyMrbdZw3fyiWgsfVqke	Amanda	Kayla	37	8561 Smith Turnpike\nNorth Brittany, MS 26440	Lake Paul	Oklahoma	South Africa	1964	eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MDkzMjQxMTYsIm5iZiI6MTYwOTMyNDExNiwianRpIjoiOGFjNDgxZDgtODBjZC00MDVmLThmNmUtMWIzNzQxMDYzNDUxIiwiZXhwIjoxNjA5NDEwNTE2LCJpZGVudGl0eSI6IjEwIiwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.ShC7D-v0ZG4Wl7klvyTp2Cvq9h6E7RV1y3J0heoFWRI
\.


--
-- Name: album_album_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.album_album_id_seq', 10, true);


--
-- Name: alias_alias_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.alias_alias_id_seq', 1, false);


--
-- Name: artist_artist_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.artist_artist_id_seq', 10, true);


--
-- Name: tracks_tracks_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.tracks_tracks_id_seq', 10, true);


--
-- Name: user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.user_id_seq', 10, true);


--
-- Name: album album_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.album
    ADD CONSTRAINT album_pkey PRIMARY KEY (album_id);


--
-- Name: alias alias_alias_name_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.alias
    ADD CONSTRAINT alias_alias_name_key UNIQUE (alias_name);


--
-- Name: alias alias_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.alias
    ADD CONSTRAINT alias_pkey PRIMARY KEY (alias_id);


--
-- Name: artist artist_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.artist
    ADD CONSTRAINT artist_pkey PRIMARY KEY (artist_id);


--
-- Name: playlist playlist_id_tracks_id_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.playlist
    ADD CONSTRAINT playlist_id_tracks_id_key UNIQUE (id, tracks_id);


--
-- Name: tracks tracks_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.tracks
    ADD CONSTRAINT tracks_pkey PRIMARY KEY (tracks_id);


--
-- Name: user user_email_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_email_key UNIQUE (email);


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);


--
-- Name: album album_artist_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.album
    ADD CONSTRAINT album_artist_id_fkey FOREIGN KEY (artist_id) REFERENCES public.artist(artist_id);


--
-- Name: alias alias_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.alias
    ADD CONSTRAINT alias_user_id_fkey FOREIGN KEY (user_id) REFERENCES public."user"(id);


--
-- Name: playlist playlist_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.playlist
    ADD CONSTRAINT playlist_id_fkey FOREIGN KEY (id) REFERENCES public."user"(id);


--
-- Name: playlist playlist_tracks_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.playlist
    ADD CONSTRAINT playlist_tracks_id_fkey FOREIGN KEY (tracks_id) REFERENCES public.tracks(tracks_id);


--
-- Name: tracks tracks_album_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.tracks
    ADD CONSTRAINT tracks_album_id_fkey FOREIGN KEY (album_id) REFERENCES public.album(album_id);


--
-- Name: tracks tracks_artist_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.tracks
    ADD CONSTRAINT tracks_artist_id_fkey FOREIGN KEY (artist_id) REFERENCES public.artist(artist_id);


--
-- PostgreSQL database dump complete
--

