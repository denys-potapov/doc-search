-- Table: public.documents

-- DROP TABLE IF EXISTS public.documents;

CREATE TABLE IF NOT EXISTS public.documents
(
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    text text COLLATE pg_catalog."default" NOT NULL DEFAULT ''::text,
    status character varying(8) COLLATE pg_catalog."default" NOT NULL DEFAULT 'PENDING'::character varying,
    CONSTRAINT documents_pkey PRIMARY KEY (id)
)
