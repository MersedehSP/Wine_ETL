-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/jaaHef
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "Wine" (
    "Name" VARCHAR(255)   NOT NULL,
    "Price" Integer   NOT NULL,
    "Description" VARCHAR(255)   NOT NULL,
    "Varietal" VARCHAR(255)   NOT NULL,
    "Region" VARCHAR(255)   NOT NULL,
    CONSTRAINT "pk_Wine" PRIMARY KEY (
        "Name"
     )
);

CREATE TABLE "Country" (
    "Country" VARCHAR(255)   NOT NULL,
    "Region" VARCHAR(255)   NOT NULL,
    "State" VARCHAR(255)   NOT NULL,
    "Address" VVARCHAR(255)   NOT NULL,
    CONSTRAINT "pk_Country" PRIMARY KEY (
        "Country"
     )
);

CREATE TABLE "Style" (
    "Sub_type" VARCHAR(255)   NOT NULL,
    "Varietal" VARCHAR(255)   NOT NULL,
    CONSTRAINT "pk_Style" PRIMARY KEY (
        "Sub_type"
     )
);

CREATE TABLE "Merchant" (
    "Merchant" VARCHAR(255)   NOT NULL,
    "Address" VARCHAR(255)   NOT NULL,
    CONSTRAINT "pk_Merchant" PRIMARY KEY (
        "Merchant"
     )
);

CREATE TABLE "Merchant_wine" (
    "Wine_name" VARCHAR(255)   NOT NULL,
    "Merchant" VARCHAR(255)   NOT NULL,
    CONSTRAINT "pk_Merchant_wine" PRIMARY KEY (
        "Wine_name","Merchant"
     )
);

ALTER TABLE "Wine" ADD CONSTRAINT "fk_Wine_Varietal" FOREIGN KEY("Varietal")
REFERENCES "Style" ("Varietal");

ALTER TABLE "Wine" ADD CONSTRAINT "fk_Wine_Region" FOREIGN KEY("Region")
REFERENCES "Country" ("Country");

ALTER TABLE "Merchant_wine" ADD CONSTRAINT "fk_Merchant_wine_Wine_name" FOREIGN KEY("Wine_name")
REFERENCES "Wine" ("Name");

ALTER TABLE "Merchant_wine" ADD CONSTRAINT "fk_Merchant_wine_Merchant" FOREIGN KEY("Merchant")
REFERENCES "Merchant" ("Merchant");

