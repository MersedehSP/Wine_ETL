-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/jaaHef
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "Wine" (
    "Name" VARCHAR(255)   NOT NULL,
    "Points" Integer   NOT NULL,
    "Description" VARCHAR(255)   NOT NULL,
    "Merchant" VARCHAR(255)   NOT NULL,
    CONSTRAINT "pk_Wine" PRIMARY KEY (
        "Name"
     )
);

CREATE TABLE "Country" (
    "Country" VARCHAR(255)   NOT NULL,
    "Region" VARCHAR(255)   NOT NULL,
    "State" VARCHAR(255)   NOT NULL,
    "Address" VVARCHAR(255)   NOT NULL,
    "Name" VARCHAR(255)   NOT NULL
);

CREATE TABLE "Style" (
    "Name" VARCHAR(255)   NOT NULL,
    "Sub_type" VARCHAR(255)   NOT NULL,
    "Varietal" VARCHAR(255)   NOT NULL
);

ALTER TABLE "Country" ADD CONSTRAINT "fk_Country_Name" FOREIGN KEY("Name")
REFERENCES "Wine" ("Name");

ALTER TABLE "Style" ADD CONSTRAINT "fk_Style_Name" FOREIGN KEY("Name")
REFERENCES "Wine" ("Name");

