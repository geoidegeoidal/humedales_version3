# -*- coding: utf-8 -*-
import json
import re
import unicodedata
import pandas as pd

SRC = r"C:\JORGE\v3\gi-sinader-2024-ckan (1) (1).xlsx"
SHEET = "Datos"
OUT_GEOJSON = r"C:\JORGE\v3\sinader_2024_establecimientos.geojson"
OUT_JS = r"C:\JORGE\v3\sinader_data.js"

LAT_MIN, LAT_MAX = -60.0, -15.0
LNG_MIN, LNG_MAX = -80.0, -65.0

# Nombres canónicos oficiales de las regiones de Chile (estándar usado por Humedales)
CANONICAL_REGIONS = [
    "Arica y Parinacota",
    "Tarapacá",
    "Antofagasta",
    "Atacama",
    "Coquimbo",
    "Valparaíso",
    "Metropolitana de Santiago",
    "Libertador General Bernardo O'Higgins",
    "Maule",
    "Ñuble",
    "Biobío",
    "La Araucanía",
    "Los Ríos",
    "Los Lagos",
    "Aysén del General Carlos Ibáñez del Campo",
    "Magallanes y de la Antártica Chilena",
]


def _normalize_key(s):
    """Genera una clave normalizada: minúsculas, sin tildes, abreviaturas expandidas y cierre de apóstrofo."""
    s = unicodedata.normalize("NFKD", str(s))
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.lower()
    s = s.replace("gral.", "general").replace("gral", "general")
    s = s.replace("'", " ").replace("`", " ")
    s = re.sub(r"\s+", " ", s).strip()
    return s


# Mapa clave normalizada -> nombre canónico (también indexa cada canónico contra sí mismo)
REGION_CANON = {}
for name in CANONICAL_REGIONS:
    REGION_CANON[_normalize_key(name)] = name


def normalize_region(value):
    """Devuelve el nombre canónico de la región o el valor original si no se reconoce."""
    if pd.isna(value):
        return value
    return REGION_CANON.get(_normalize_key(value), value)


df = pd.read_excel(SRC, sheet_name=SHEET)
df["region"] = df["region"].map(normalize_region)

valid = df[
    (df["latitud"] >= LAT_MIN) & (df["latitud"] <= LAT_MAX) &
    (df["longitud"] >= LNG_MIN) & (df["longitud"] <= LNG_MAX)
].copy()

group = valid.groupby("id_vu").agg(
    id_vu=("id_vu", "first"),
    razon_social=("razon_social", "first"),
    rut_razon_social=("rut_razon_social", "first"),
    nombre_establecimiento=("nombre_establecimiento", "first"),
    rubro=("rubro", "first"),
    region=("region", "first"),
    provincia=("provincia", "first"),
    comuna=("comuna", "first"),
    latitud=("latitud", "first"),
    longitud=("longitud", "first"),
    num_declaraciones=("declaracion_id", "nunique"),
    total_toneladas=("cantidad_toneladas", "sum"),
).reset_index(drop=True)

group = group.dropna(subset=["latitud", "longitud"])

features = []
for _, r in group.iterrows():
    props = {
        "id_vu": int(r["id_vu"]) if pd.notna(r["id_vu"]) else None,
        "razon_social": r["razon_social"] if pd.notna(r["razon_social"]) else None,
        "rut_razon_social": r["rut_razon_social"] if pd.notna(r["rut_razon_social"]) else None,
        "nombre_establecimiento": r["nombre_establecimiento"] if pd.notna(r["nombre_establecimiento"]) else None,
        "rubro": r["rubro"] if pd.notna(r["rubro"]) else None,
        "region": r["region"] if pd.notna(r["region"]) else None,
        "provincia": r["provincia"] if pd.notna(r["provincia"]) else None,
        "comuna": r["comuna"] if pd.notna(r["comuna"]) else None,
        "num_declaraciones": int(r["num_declaraciones"]),
        "total_toneladas": round(float(r["total_toneladas"]), 2),
    }
    features.append({
        "type": "Feature",
        "properties": props,
        "geometry": {
            "type": "Point",
            "coordinates": [float(r["longitud"]), float(r["latitud"])],
        },
    })

geojson = {
    "type": "FeatureCollection",
    "crs": {"type": "name", "properties": {"name": "urn:ogc:def:crs:OGC:1.3:CRS84"}},
    "features": features,
}

with open(OUT_GEOJSON, "w", encoding="utf-8") as f:
    json.dump(geojson, f, ensure_ascii=False)

with open(OUT_JS, "w", encoding="utf-8") as f:
    f.write("window.sinaderData = ")
    json.dump(geojson, f, ensure_ascii=False)
    f.write(";\n")

total_ton = group["total_toneladas"].sum()
print(f"Filas originales: {len(df)}")
print(f"Filas con coords válidas: {len(valid)}")
print(f"Establecimientos (features): {len(features)}")
print(f"Total toneladas agregadas: {total_ton:,.2f}")
print(f"OK -> {OUT_GEOJSON}")
print(f"OK -> {OUT_JS}")