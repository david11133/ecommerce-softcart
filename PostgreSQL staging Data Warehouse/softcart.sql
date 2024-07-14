CREATE TABLE public."FactSales"
(
    order_id bigint primary key,
    date_id smallint NOT NULL,
    country_id smallint NOT NULL,
    category_id smallint NOT NULL,
	item_id smallint NOT NULL,
    amount bigint NOT NULL
);


ALTER TABLE public."FactSales"
ADD FOREIGN KEY (date_id)
REFERENCES public."DimDate" (date_id)
NOT VALID;


ALTER TABLE public."FactSales"
ADD FOREIGN KEY (country_id)
REFERENCES public."DimCountry" (country_id)
NOT VALID;


ALTER TABLE public."FactSales"
ADD FOREIGN KEY (category_id)
REFERENCES public."DimCategory" (category_id)
NOT VALID;

ALTER TABLE public."FactSales"
ADD FOREIGN KEY (item_id)
REFERENCES public."DimItem" (item_id)
NOT VALID;



CREATE TABLE public."DimCategory"
(
    category_id smallint primary key,
    category character varying(32)[] NOT NULL
);


CREATE TABLE public."DimCountry"
(
    country_id smallint primary key,
    country character varying(32)[] NOT NULL
);


CREATE TABLE public."DimDate"
(
    date_id smallint primary key,
    date date NOT NULL,
    Year smallint NOT NULL,
    Quarter smallint NOT NULL,
    QuarterName character varying(2)[] NOT NULL,
    Month smallint NOT NULL,
    Monthname character varying(9)[] NOT NULL,
    Day smallint NOT NULL,
    Weekday smallint NOT NULL,
    WeekdayName character varying(9)[] NOT NULL
);



CREATE TABLE public."DimItem"
(
    item_id integer NOT NULL PRIMARY KEY,
    item character varying NOT NULL
);


