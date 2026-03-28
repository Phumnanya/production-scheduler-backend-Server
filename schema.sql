--
-- PostgreSQL database dump
--

\restrict jeLb7Z7CqaB9BdDLU7h190Hv2BBBmlph3m5DtfjBCi22aynEGtyeI3HZhXdrk3N

-- Dumped from database version 15.14 (Debian 15.14-0+deb12u1)
-- Dumped by pg_dump version 15.14 (Debian 15.14-0+deb12u1)

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

--
-- Name: public; Type: SCHEMA; Schema: -; Owner: eustace
--

-- *not* creating schema, since initdb creates it


ALTER SCHEMA public OWNER TO eustace;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: production_orders; Type: TABLE; Schema: public; Owner: eustace
--

CREATE TABLE public.production_orders (
    id integer NOT NULL,
    machine character varying(50),
    date date NOT NULL,
    task character varying(50),
    quantity integer,
    "startTime" character varying(10),
    "endTime" character varying(10)
);


ALTER TABLE public.production_orders OWNER TO eustace;

--
-- Name: production_orders_id_seq; Type: SEQUENCE; Schema: public; Owner: eustace
--

CREATE SEQUENCE public.production_orders_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.production_orders_id_seq OWNER TO eustace;

--
-- Name: production_orders_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: eustace
--

ALTER SEQUENCE public.production_orders_id_seq OWNED BY public.production_orders.id;


--
-- Name: user; Type: TABLE; Schema: public; Owner: eustace
--

CREATE TABLE public."user" (
    id integer NOT NULL,
    machine character varying(50),
    task character varying(50),
    quantity integer,
    "startTime" character varying(10),
    "endTime" character varying(10),
    date date
);


ALTER TABLE public."user" OWNER TO eustace;

--
-- Name: user_id_seq; Type: SEQUENCE; Schema: public; Owner: eustace
--

CREATE SEQUENCE public.user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_id_seq OWNER TO eustace;

--
-- Name: user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: eustace
--

ALTER SEQUENCE public.user_id_seq OWNED BY public."user".id;


--
-- Name: production_orders id; Type: DEFAULT; Schema: public; Owner: eustace
--

ALTER TABLE ONLY public.production_orders ALTER COLUMN id SET DEFAULT nextval('public.production_orders_id_seq'::regclass);


--
-- Name: user id; Type: DEFAULT; Schema: public; Owner: eustace
--

ALTER TABLE ONLY public."user" ALTER COLUMN id SET DEFAULT nextval('public.user_id_seq'::regclass);


--
-- Name: production_orders production_orders_pkey; Type: CONSTRAINT; Schema: public; Owner: eustace
--

ALTER TABLE ONLY public.production_orders
    ADD CONSTRAINT production_orders_pkey PRIMARY KEY (id);


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: eustace
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);


--
-- Name: DEFAULT PRIVILEGES FOR TABLES; Type: DEFAULT ACL; Schema: public; Owner: postgres
--

ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public GRANT ALL ON TABLES  TO eustace;


--
-- PostgreSQL database dump complete
--

\unrestrict jeLb7Z7CqaB9BdDLU7h190Hv2BBBmlph3m5DtfjBCi22aynEGtyeI3HZhXdrk3N

