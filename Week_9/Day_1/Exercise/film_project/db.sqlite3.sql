BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "django_migrations" (
	"id"	integer NOT NULL,
	"app"	varchar(255) NOT NULL,
	"name"	varchar(255) NOT NULL,
	"applied"	datetime NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_group_permissions" (
	"id"	integer NOT NULL,
	"group_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_user_groups" (
	"id"	integer NOT NULL,
	"user_id"	integer NOT NULL,
	"group_id"	integer NOT NULL,
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_user_user_permissions" (
	"id"	integer NOT NULL,
	"user_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "django_admin_log" (
	"id"	integer NOT NULL,
	"action_time"	datetime NOT NULL,
	"object_id"	text,
	"object_repr"	varchar(200) NOT NULL,
	"change_message"	text NOT NULL,
	"content_type_id"	integer,
	"user_id"	integer NOT NULL,
	"action_flag"	smallint unsigned NOT NULL CHECK("action_flag" >= 0),
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "django_content_type" (
	"id"	integer NOT NULL,
	"app_label"	varchar(100) NOT NULL,
	"model"	varchar(100) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_permission" (
	"id"	integer NOT NULL,
	"content_type_id"	integer NOT NULL,
	"codename"	varchar(100) NOT NULL,
	"name"	varchar(255) NOT NULL,
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_group" (
	"id"	integer NOT NULL,
	"name"	varchar(150) NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_user" (
	"id"	integer NOT NULL,
	"password"	varchar(128) NOT NULL,
	"last_login"	datetime,
	"is_superuser"	bool NOT NULL,
	"username"	varchar(150) NOT NULL UNIQUE,
	"last_name"	varchar(150) NOT NULL,
	"email"	varchar(254) NOT NULL,
	"is_staff"	bool NOT NULL,
	"is_active"	bool NOT NULL,
	"date_joined"	datetime NOT NULL,
	"first_name"	varchar(150) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "django_session" (
	"session_key"	varchar(40) NOT NULL,
	"session_data"	text NOT NULL,
	"expire_date"	datetime NOT NULL,
	PRIMARY KEY("session_key")
);
CREATE TABLE IF NOT EXISTS "film_app_category" (
	"id"	integer NOT NULL,
	"name"	varchar(50) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "film_app_country" (
	"id"	integer NOT NULL,
	"name"	varchar(50) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "film_app_director" (
	"id"	integer NOT NULL,
	"first_name"	varchar(50) NOT NULL,
	"last_name"	varchar(50) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "film_app_film" (
	"id"	integer NOT NULL,
	"title"	varchar(50) NOT NULL,
	"release_date"	datetime NOT NULL,
	"created_in_country_id"	integer,
	FOREIGN KEY("created_in_country_id") REFERENCES "film_app_country"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "film_app_film_available_in_countries" (
	"id"	integer NOT NULL,
	"film_id"	integer NOT NULL,
	"country_id"	integer NOT NULL,
	FOREIGN KEY("film_id") REFERENCES "film_app_film"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("country_id") REFERENCES "film_app_country"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "film_app_film_category" (
	"id"	integer NOT NULL,
	"film_id"	integer NOT NULL,
	"category_id"	integer NOT NULL,
	FOREIGN KEY("category_id") REFERENCES "film_app_category"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("film_id") REFERENCES "film_app_film"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "film_app_film_director" (
	"id"	integer NOT NULL,
	"film_id"	integer NOT NULL,
	"director_id"	integer NOT NULL,
	FOREIGN KEY("director_id") REFERENCES "film_app_director"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("film_id") REFERENCES "film_app_film"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT INTO "django_migrations" VALUES (1,'contenttypes','0001_initial','2021-03-07 12:26:11.138895');
INSERT INTO "django_migrations" VALUES (2,'auth','0001_initial','2021-03-07 12:26:11.156387');
INSERT INTO "django_migrations" VALUES (3,'admin','0001_initial','2021-03-07 12:26:11.172457');
INSERT INTO "django_migrations" VALUES (4,'admin','0002_logentry_remove_auto_add','2021-03-07 12:26:11.197950');
INSERT INTO "django_migrations" VALUES (5,'admin','0003_logentry_add_action_flag_choices','2021-03-07 12:26:11.212061');
INSERT INTO "django_migrations" VALUES (6,'contenttypes','0002_remove_content_type_name','2021-03-07 12:26:11.232971');
INSERT INTO "django_migrations" VALUES (7,'auth','0002_alter_permission_name_max_length','2021-03-07 12:26:11.248476');
INSERT INTO "django_migrations" VALUES (8,'auth','0003_alter_user_email_max_length','2021-03-07 12:26:11.263548');
INSERT INTO "django_migrations" VALUES (9,'auth','0004_alter_user_username_opts','2021-03-07 12:26:11.279536');
INSERT INTO "django_migrations" VALUES (10,'auth','0005_alter_user_last_login_null','2021-03-07 12:26:11.293835');
INSERT INTO "django_migrations" VALUES (11,'auth','0006_require_contenttypes_0002','2021-03-07 12:26:11.302226');
INSERT INTO "django_migrations" VALUES (12,'auth','0007_alter_validators_add_error_messages','2021-03-07 12:26:11.317050');
INSERT INTO "django_migrations" VALUES (13,'auth','0008_alter_user_username_max_length','2021-03-07 12:26:11.331667');
INSERT INTO "django_migrations" VALUES (14,'auth','0009_alter_user_last_name_max_length','2021-03-07 12:26:11.345646');
INSERT INTO "django_migrations" VALUES (15,'auth','0010_alter_group_name_max_length','2021-03-07 12:26:11.360409');
INSERT INTO "django_migrations" VALUES (16,'auth','0011_update_proxy_permissions','2021-03-07 12:26:11.372743');
INSERT INTO "django_migrations" VALUES (17,'auth','0012_alter_user_first_name_max_length','2021-03-07 12:26:11.388603');
INSERT INTO "django_migrations" VALUES (18,'sessions','0001_initial','2021-03-07 12:26:11.397969');
INSERT INTO "django_migrations" VALUES (19,'film_app','0001_initial','2021-03-07 13:49:20.526298');
INSERT INTO "django_content_type" VALUES (1,'admin','logentry');
INSERT INTO "django_content_type" VALUES (2,'auth','permission');
INSERT INTO "django_content_type" VALUES (3,'auth','group');
INSERT INTO "django_content_type" VALUES (4,'auth','user');
INSERT INTO "django_content_type" VALUES (5,'contenttypes','contenttype');
INSERT INTO "django_content_type" VALUES (6,'sessions','session');
INSERT INTO "django_content_type" VALUES (7,'film_app','director');
INSERT INTO "django_content_type" VALUES (8,'film_app','category');
INSERT INTO "django_content_type" VALUES (9,'film_app','film');
INSERT INTO "django_content_type" VALUES (10,'film_app','country');
INSERT INTO "auth_permission" VALUES (1,1,'add_logentry','Can add log entry');
INSERT INTO "auth_permission" VALUES (2,1,'change_logentry','Can change log entry');
INSERT INTO "auth_permission" VALUES (3,1,'delete_logentry','Can delete log entry');
INSERT INTO "auth_permission" VALUES (4,1,'view_logentry','Can view log entry');
INSERT INTO "auth_permission" VALUES (5,2,'add_permission','Can add permission');
INSERT INTO "auth_permission" VALUES (6,2,'change_permission','Can change permission');
INSERT INTO "auth_permission" VALUES (7,2,'delete_permission','Can delete permission');
INSERT INTO "auth_permission" VALUES (8,2,'view_permission','Can view permission');
INSERT INTO "auth_permission" VALUES (9,3,'add_group','Can add group');
INSERT INTO "auth_permission" VALUES (10,3,'change_group','Can change group');
INSERT INTO "auth_permission" VALUES (11,3,'delete_group','Can delete group');
INSERT INTO "auth_permission" VALUES (12,3,'view_group','Can view group');
INSERT INTO "auth_permission" VALUES (13,4,'add_user','Can add user');
INSERT INTO "auth_permission" VALUES (14,4,'change_user','Can change user');
INSERT INTO "auth_permission" VALUES (15,4,'delete_user','Can delete user');
INSERT INTO "auth_permission" VALUES (16,4,'view_user','Can view user');
INSERT INTO "auth_permission" VALUES (17,5,'add_contenttype','Can add content type');
INSERT INTO "auth_permission" VALUES (18,5,'change_contenttype','Can change content type');
INSERT INTO "auth_permission" VALUES (19,5,'delete_contenttype','Can delete content type');
INSERT INTO "auth_permission" VALUES (20,5,'view_contenttype','Can view content type');
INSERT INTO "auth_permission" VALUES (21,6,'add_session','Can add session');
INSERT INTO "auth_permission" VALUES (22,6,'change_session','Can change session');
INSERT INTO "auth_permission" VALUES (23,6,'delete_session','Can delete session');
INSERT INTO "auth_permission" VALUES (24,6,'view_session','Can view session');
INSERT INTO "auth_permission" VALUES (25,7,'add_director','Can add director');
INSERT INTO "auth_permission" VALUES (26,7,'change_director','Can change director');
INSERT INTO "auth_permission" VALUES (27,7,'delete_director','Can delete director');
INSERT INTO "auth_permission" VALUES (28,7,'view_director','Can view director');
INSERT INTO "auth_permission" VALUES (29,8,'add_category','Can add category');
INSERT INTO "auth_permission" VALUES (30,8,'change_category','Can change category');
INSERT INTO "auth_permission" VALUES (31,8,'delete_category','Can delete category');
INSERT INTO "auth_permission" VALUES (32,8,'view_category','Can view category');
INSERT INTO "auth_permission" VALUES (33,9,'add_film','Can add film');
INSERT INTO "auth_permission" VALUES (34,9,'change_film','Can change film');
INSERT INTO "auth_permission" VALUES (35,9,'delete_film','Can delete film');
INSERT INTO "auth_permission" VALUES (36,9,'view_film','Can view film');
INSERT INTO "auth_permission" VALUES (37,10,'add_country','Can add country');
INSERT INTO "auth_permission" VALUES (38,10,'change_country','Can change country');
INSERT INTO "auth_permission" VALUES (39,10,'delete_country','Can delete country');
INSERT INTO "auth_permission" VALUES (40,10,'view_country','Can view country');
INSERT INTO "auth_user" VALUES (1,'pbkdf2_sha256$216000$REnEa4pg26h5$GNcBXNRMJRGHeJMZZsaLtrM8q3bS2PrqnZtEMvC+zvE=','2021-03-08 13:34:42.482749',1,'admin','','',1,1,'2021-03-08 11:26:19.002833','');
INSERT INTO "film_app_category" VALUES (1,'horror');
INSERT INTO "film_app_category" VALUES (2,'comedy');
INSERT INTO "film_app_category" VALUES (3,'drama');
INSERT INTO "film_app_category" VALUES (4,'action');
INSERT INTO "film_app_category" VALUES (5,'documentary');
INSERT INTO "film_app_country" VALUES (1,'US');
INSERT INTO "film_app_country" VALUES (2,'UK');
INSERT INTO "film_app_country" VALUES (3,'FR');
INSERT INTO "film_app_country" VALUES (4,'CHN');
INSERT INTO "film_app_country" VALUES (5,'DE');
INSERT INTO "film_app_director" VALUES (1,'Quentin','Tartino');
INSERT INTO "film_app_director" VALUES (2,'Steven','Spielberg');
INSERT INTO "film_app_director" VALUES (3,'Tim','Burton');
INSERT INTO "film_app_director" VALUES (4,'Bora','Dagtekin');
INSERT INTO "film_app_director" VALUES (5,'Sven','Unterwald Jr');
INSERT INTO "film_app_director" VALUES (6,'Ning','Hao');
INSERT INTO "film_app_director" VALUES (7,'Lo','Wei');
INSERT INTO "film_app_director" VALUES (8,'Woody','Allan');
INSERT INTO "film_app_film" VALUES (1,'Jaws','1975-06-20 23:00:00',1);
INSERT INTO "film_app_film" VALUES (2,'Catch me if you can','2003-02-06 22:00:00',1);
INSERT INTO "film_app_film" VALUES (3,'Django Unchained','2013-01-17 19:00:00',1);
INSERT INTO "film_app_film" VALUES (4,'Edward Scissorhands','1990-12-06 20:00:00',2);
INSERT INTO "film_app_film" VALUES (5,'Fuck U Goethe','2013-10-29 18:00:00',5);
INSERT INTO "film_app_film" VALUES (6,'7 Dwarves','2006-10-24 18:00:00',5);
INSERT INTO "film_app_film" VALUES (7,'New Fist of Fury','1976-07-08 20:00:00',4);
INSERT INTO "film_app_film" VALUES (8,'Titanic','2021-03-08 08:00:00',1);
INSERT INTO "film_app_film" VALUES (9,'Burlesque','2021-03-08 00:00:00',3);
INSERT INTO "film_app_film_available_in_countries" VALUES (1,8,1);
INSERT INTO "film_app_film_available_in_countries" VALUES (2,1,1);
INSERT INTO "film_app_film_available_in_countries" VALUES (3,1,2);
INSERT INTO "film_app_film_available_in_countries" VALUES (4,1,3);
INSERT INTO "film_app_film_available_in_countries" VALUES (5,1,5);
INSERT INTO "film_app_film_available_in_countries" VALUES (6,2,1);
INSERT INTO "film_app_film_available_in_countries" VALUES (7,3,1);
INSERT INTO "film_app_film_available_in_countries" VALUES (8,3,3);
INSERT INTO "film_app_film_available_in_countries" VALUES (9,8,5);
INSERT INTO "film_app_film_available_in_countries" VALUES (10,7,4);
INSERT INTO "film_app_film_available_in_countries" VALUES (11,7,3);
INSERT INTO "film_app_film_available_in_countries" VALUES (12,7,1);
INSERT INTO "film_app_film_available_in_countries" VALUES (13,6,1);
INSERT INTO "film_app_film_available_in_countries" VALUES (14,6,2);
INSERT INTO "film_app_film_available_in_countries" VALUES (15,9,1);
INSERT INTO "film_app_film_available_in_countries" VALUES (16,9,2);
INSERT INTO "film_app_film_available_in_countries" VALUES (17,9,3);
INSERT INTO "film_app_film_available_in_countries" VALUES (18,9,5);
INSERT INTO "film_app_film_category" VALUES (1,8,2);
INSERT INTO "film_app_film_category" VALUES (2,1,1);
INSERT INTO "film_app_film_category" VALUES (3,1,4);
INSERT INTO "film_app_film_category" VALUES (4,2,3);
INSERT INTO "film_app_film_category" VALUES (5,3,3);
INSERT INTO "film_app_film_category" VALUES (6,4,2);
INSERT INTO "film_app_film_category" VALUES (7,5,2);
INSERT INTO "film_app_film_category" VALUES (8,7,3);
INSERT INTO "film_app_film_category" VALUES (9,9,3);
INSERT INTO "film_app_film_director" VALUES (1,8,1);
INSERT INTO "film_app_film_director" VALUES (2,9,2);
INSERT INTO "film_app_film_director" VALUES (3,1,2);
INSERT INTO "film_app_film_director" VALUES (4,2,2);
INSERT INTO "film_app_film_director" VALUES (5,3,1);
INSERT INTO "film_app_film_director" VALUES (6,4,3);
INSERT INTO "film_app_film_director" VALUES (7,5,4);
INSERT INTO "film_app_film_director" VALUES (8,6,5);
INSERT INTO "film_app_film_director" VALUES (9,7,7);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ON "auth_group_permissions" (
	"group_id",
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" (
	"group_id"
);
CREATE INDEX IF NOT EXISTS "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" (
	"permission_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_user_groups_user_id_group_id_94350c0c_uniq" ON "auth_user_groups" (
	"user_id",
	"group_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_groups_user_id_6a12ed8b" ON "auth_user_groups" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_groups_group_id_97559544" ON "auth_user_groups" (
	"group_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" ON "auth_user_user_permissions" (
	"user_id",
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_user_permissions_user_id_a95ead1b" ON "auth_user_user_permissions" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_user_permissions_permission_id_1fbb5f2c" ON "auth_user_user_permissions" (
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" (
	"content_type_id"
);
CREATE INDEX IF NOT EXISTS "django_admin_log_user_id_c564eba6" ON "django_admin_log" (
	"user_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "django_content_type_app_label_model_76bd3d3b_uniq" ON "django_content_type" (
	"app_label",
	"model"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_permission_content_type_id_codename_01ab375a_uniq" ON "auth_permission" (
	"content_type_id",
	"codename"
);
CREATE INDEX IF NOT EXISTS "auth_permission_content_type_id_2f476e4b" ON "auth_permission" (
	"content_type_id"
);
CREATE INDEX IF NOT EXISTS "django_session_expire_date_a5c62663" ON "django_session" (
	"expire_date"
);
CREATE INDEX IF NOT EXISTS "film_app_film_created_in_country_id_17be7cef" ON "film_app_film" (
	"created_in_country_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "film_app_film_available_in_countries_film_id_country_id_4d55666f_uniq" ON "film_app_film_available_in_countries" (
	"film_id",
	"country_id"
);
CREATE INDEX IF NOT EXISTS "film_app_film_available_in_countries_film_id_9f616132" ON "film_app_film_available_in_countries" (
	"film_id"
);
CREATE INDEX IF NOT EXISTS "film_app_film_available_in_countries_country_id_568cebcf" ON "film_app_film_available_in_countries" (
	"country_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "film_app_film_category_film_id_category_id_538c6ee4_uniq" ON "film_app_film_category" (
	"film_id",
	"category_id"
);
CREATE INDEX IF NOT EXISTS "film_app_film_category_film_id_5c0428af" ON "film_app_film_category" (
	"film_id"
);
CREATE INDEX IF NOT EXISTS "film_app_film_category_category_id_4cdf3bb1" ON "film_app_film_category" (
	"category_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "film_app_film_director_film_id_director_id_67212add_uniq" ON "film_app_film_director" (
	"film_id",
	"director_id"
);
CREATE INDEX IF NOT EXISTS "film_app_film_director_film_id_57f94c46" ON "film_app_film_director" (
	"film_id"
);
CREATE INDEX IF NOT EXISTS "film_app_film_director_director_id_6d990068" ON "film_app_film_director" (
	"director_id"
);
COMMIT;
