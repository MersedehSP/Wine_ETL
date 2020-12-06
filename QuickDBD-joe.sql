-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/6P1lVW
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "wine" (
    "wine_id" SERIAL   NOT NULL,
    "wine_name" VARCHAR   NOT NULL,
    "varietal" VARCHAR   NOT NULL,
    "price" Decimal   NOT NULL,
    "description" VARCHAR   NOT NULL,
    "region_id" int   NOT NULL,
    CONSTRAINT "pk_wine" PRIMARY KEY (
        "wine_id"
     )
);

CREATE TABLE "merchant_wine" (
    "merchant_name" VARCHAR   NOT NULL,
    "wine_id" SERIAL   NOT NULL,
    "wine_name" VARCHAR   NOT NULL
);

CREATE TABLE "region" (
    "region_id" int   NOT NULL,
    "country" VARCHAR   NOT NULL,
    "region" VARCHAR   NOT NULL,
    "state" VARCHAR   NOT NULL,
    CONSTRAINT "pk_region" PRIMARY KEY (
        "region_id"
     )
);

CREATE TABLE "merchant" (
    "merchant_name" VARCHAR   NOT NULL,
    "merchant_address" VARCHAR   NOT NULL,
    CONSTRAINT "pk_merchant" PRIMARY KEY (
        "merchant_name"
     )
);

ALTER TABLE "wine" ADD CONSTRAINT "fk_wine_region_id" FOREIGN KEY("region_id")
REFERENCES "region" ("region_id");

ALTER TABLE "merchant_wine" ADD CONSTRAINT "fk_merchant_wine_merchant_name" FOREIGN KEY("merchant_name")
REFERENCES "merchant" ("merchant_name");

ALTER TABLE "merchant_wine" ADD CONSTRAINT "fk_merchant_wine_wine_id" FOREIGN KEY("wine_id")
REFERENCES "wine" ("wine_id");

