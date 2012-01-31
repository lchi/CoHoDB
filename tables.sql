BEGIN;
CREATE TABLE "trade_records" (
    "id" integer  PRIMARY KEY,
    "group_id" integer,
    "strategy" varchar(20),
    "trade_date" date,
    "expiration_date" date,
    "underlyer" varchar(15),
    "type" varchar(4),
    "position" varchar(5),
    "strike" decimal,
    "spot" decimal,
    "premium" decimal,
    "quantity" integer,
    "commission" decimal,
    "industry" varchar(40),
    "trade_type" varchar (20),
    "asset_class" varchar (20),
    "notes" varchar(200) 
)
;
COMMIT;