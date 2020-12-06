-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "merchant" (
    "merchant_name" VARCHAR   NOT NULL,
    "merchant_address" VARCHAR   NOT NULL,
    CONSTRAINT "pk_merchant" PRIMARY KEY (
        "merchant_name"
     )
);

CREATE TABLE "region" (
    "region_id" DECIMAL   NOT NULL,
    "country" VARCHAR   NOT NULL,
    "region" VARCHAR   NOT NULL,
    "state" VARCHAR   NOT NULL,
    CONSTRAINT "pk_region" PRIMARY KEY (
        "region_id"
     )
);

CREATE TABLE "wine" (
    "wine_name" VARCHAR   NOT NULL,
    "varietal" VARCHAR   NOT NULL,
    "price" DECIMAL   NOT NULL,
    "description" VARCHAR   NOT NULL,
    "merchant_name" VARCHAR   NOT NULL,
    "region_id" DECIMAL   NOT NULL,
    CONSTRAINT "pk_wine" PRIMARY KEY (
        "wine_name","merchant_name"
     )
);

CREATE TABLE "merchant_Wine" (
    "merchant_name" VARCHAR   NOT NULL,
    "wine_name" VARCHAR   NOT NULL,
    CONSTRAINT "pk_merchant_Wine" PRIMARY KEY (
        "merchant_name","wine_name"
     )
);

ALTER TABLE "wine" ADD CONSTRAINT "fk_wine_merchant_name" FOREIGN KEY("merchant_name")
REFERENCES "merchant_Wine" ("merchant_name");

ALTER TABLE "wine" ADD CONSTRAINT "fk_wine_region_id" FOREIGN KEY("region_id")
REFERENCES "region" ("region_id");

ALTER TABLE "merchant_Wine" ADD CONSTRAINT "fk_merchant_Wine_merchant_name" FOREIGN KEY("merchant_name")
REFERENCES "merchant" ("merchant_name");

ALTER TABLE "merchant_Wine" ADD CONSTRAINT "fk_merchant_Wine_wine_name" FOREIGN KEY("wine_name")
REFERENCES "wine" ("wine_name");

