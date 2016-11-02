from django.contrib import admin
from rubro.models import Rubro, VariedadRubro,TipoRubro
# Register your models here.
#=====Rubro =====================
admin.site.register(Rubro)
admin.site.register(VariedadRubro)

admin.site.register(TipoRubro)

"""001
BEGIN;
CREATE TABLE "rubro_rubro" ("id" serial NOT NULL PRIMARY KEY, "nombre" varchar(50) NOT NULL UNIQUE, "nombre_cientifico" varchar(100) NOT NULL UNIQUE, "tolerancia_humedad" double precision NOT NULL, "diferencia_humedad" double precision NOT NULL, "tolrancia_impuerezas" double precision NOT NULL, "foto" varchar(100) NOT NULL);
CREATE TABLE "rubro_tiporubro" ("id" serial NOT NULL PRIMARY KEY, "nombre" varchar(50) NOT NULL UNIQUE, "descripcion" text NOT NULL, "rubro_id" integer NOT NULL);
CREATE TABLE "rubro_variedadrubro" ("id" serial NOT NULL PRIMARY KEY, "nombre" varchar(50) NOT NULL UNIQUE, "descripcion" text NOT NULL, "rubro_id" integer NOT NULL);
CREATE INDEX "rubro_rubro_nombre_60df47ae_like" ON "rubro_rubro" ("nombre" varchar_pattern_ops);
CREATE INDEX "rubro_rubro_nombre_cientifico_438b355b_like" ON "rubro_rubro" ("nombre_cientifico" varchar_pattern_ops);
ALTER TABLE "rubro_tiporubro" ADD CONSTRAINT "rubro_tiporubro_rubro_id_642bd555_fk_rubro_rubro_id" FOREIGN KEY ("rubro_id") REFERENCES "rubro_rubro" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "rubro_tiporubro_1a6ebb11" ON "rubro_tiporubro" ("rubro_id");
CREATE INDEX "rubro_tiporubro_nombre_68c53c34_like" ON "rubro_tiporubro" ("nombre" varchar_pattern_ops);
ALTER TABLE "rubro_variedadrubro" ADD CONSTRAINT "rubro_variedadrubro_rubro_id_46576cdd_fk_rubro_rubro_id" FOREIGN KEY ("rubro_id") REFERENCES "rubro_rubro" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "rubro_variedadrubro_1a6ebb11" ON "rubro_variedadrubro" ("rubro_id");
CREATE INDEX "rubro_variedadrubro_nombre_d1c8d9a_like" ON "rubro_variedadrubro" ("nombre" varchar_pattern_ops);

COMMIT;


BEGIN;
CREATE TABLE "rubro_rubro" 
("id" serial NOT NULL PRIMARY KEY, "nombre" varchar(50) NOT NULL UNIQUE,
"nombre_cientifico" varchar(100) NOT NULL UNIQUE, 
"tolerancia_humedad" double precision NOT NULL, 
"diferencia_humedad" double precision NOT NULL, 
"tolrancia_impuerezas" double precision NOT NULL, 
"foto" varchar(100) NOT NULL);






CREATE TABLE "rubro_tiporubro" ("id" serial NOT NULL PRIMARY KEY, "nombre" varchar(50) NOT NULL UNIQUE, "descripcion" text NOT NULL, "rubro_id" integer NOT NULL);
CREATE TABLE "rubro_variedadrubro" ("id" serial NOT NULL PRIMARY KEY, "nombre" varchar(50) NOT NULL UNIQUE, "descripcion" text NOT NULL, "rubro_id" integer NOT NULL);
CREATE INDEX "rubro_rubro_nombre_60df47ae_like" ON "rubro_rubro" ("nombre" varchar_pattern_ops);
CREATE INDEX "rubro_rubro_nombre_cientifico_438b355b_like" ON "rubro_rubro" ("nombre_cientifico" varchar_pattern_ops);
ALTER TABLE "rubro_tiporubro" ADD CONSTRAINT "rubro_tiporubro_rubro_id_642bd555_fk_rubro_rubro_id" FOREIGN KEY ("rubro_id") REFERENCES "rubro_rubro" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "rubro_tiporubro_1a6ebb11" ON "rubro_tiporubro" ("rubro_id");
CREATE INDEX "rubro_tiporubro_nombre_68c53c34_like" ON "rubro_tiporubro" ("nombre" varchar_pattern_ops);
ALTER TABLE "rubro_variedadrubro" ADD CONSTRAINT "rubro_variedadrubro_rubro_id_46576cdd_fk_rubro_rubro_id" FOREIGN KEY ("rubro_id") REFERENCES "rubro_rubro" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "rubro_variedadrubro_1a6ebb11" ON "rubro_variedadrubro" ("rubro_id");
CREATE INDEX "rubro_variedadrubro_nombre_d1c8d9a_like" ON "rubro_variedadrubro" ("nombre" varchar_pattern_ops);

COMMIT;
"""