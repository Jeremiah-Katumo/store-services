BEGIN;
--
-- Create model Cart
--
CREATE TABLE "storeapp_cart" ("cart_id" char(32) NOT NULL PRIMARY KEY, "created" datetime NOT NULL, "completed" bool NOT NULL);
--
-- Create model Category
--
CREATE TABLE "storeapp_category" ("title" varchar(200) NOT NULL, "category_id" char(32) NOT NULL PRIMARY KEY, "slug" varchar(50) NOT NULL);
--
-- Create model Product
--
CREATE TABLE "storeapp_product" ("name" varchar(200) NOT NULL, "description" text NULL, "discount" bool NOT NULL, "image" varchar(100) NULL, "old_price" real NOT NULL, "slug" varchar(50) NOT NULL, "id" char(32) NOT NULL PRIMARY KEY, "inventory" integer NOT NULL, "top_deal" bool NOT NULL, "flash_sales" bool NOT NULL, "category_id" char(32) NULL REFERENCES "storeapp_category" ("category_id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model Customer
--
CREATE TABLE "storeapp_customer" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" bigint NOT NULL UNIQUE REFERENCES "core_user" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Add field featured_product to category
--
CREATE TABLE "new__storeapp_category" ("title" varchar(200) NOT NULL, "category_id" char(32) NOT NULL PRIMARY KEY, "slug" varchar(50) NOT NULL, "featured_product_id" char(32) NULL UNIQUE REFERENCES "storeapp_product" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "new__storeapp_category" ("title", "category_id", "slug", "featured_product_id") SELECT "title", "category_id", "slug", NULL FROM "storeapp_category";
DROP TABLE "storeapp_category";
ALTER TABLE "new__storeapp_category" RENAME TO "storeapp_category";
CREATE INDEX "storeapp_product_slug_84725928" ON "storeapp_product" ("slug");
CREATE INDEX "storeapp_product_category_id_5c530b9c" ON "storeapp_product" ("category_id");
CREATE INDEX "storeapp_category_slug_b311ee12" ON "storeapp_category" ("slug");
--
-- Create model Cartitems
--
CREATE TABLE "storeapp_cartitems" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "quantity" integer NOT NULL, "cart_id" char(32) NULL REFERENCES "storeapp_cart" ("cart_id") DEFERRABLE INITIALLY DEFERRED, "product_id" char(32) NULL REFERENCES "storeapp_product" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Add field owner to cart
--
CREATE TABLE "new__storeapp_cart" ("cart_id" char(32) NOT NULL PRIMARY KEY, "created" datetime NOT NULL, "completed" bool NOT NULL, "owner_id" bigint NOT NULL REFERENCES "storeapp_customer" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "new__storeapp_cart" ("cart_id", "created", "completed", "owner_id") SELECT "cart_id", "created", "completed", NULL FROM "storeapp_cart";
DROP TABLE "storeapp_cart";
ALTER TABLE "new__storeapp_cart" RENAME TO "storeapp_cart";
CREATE INDEX "storeapp_cartitems_cart_id_bf210fc8" ON "storeapp_cartitems" ("cart_id");
CREATE INDEX "storeapp_cartitems_product_id_2469422e" ON "storeapp_cartitems" ("product_id");
CREATE INDEX "storeapp_cart_owner_id_cbb678a3" ON "storeapp_cart" ("owner_id");
COMMIT;
