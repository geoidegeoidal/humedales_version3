# Humedales WebGIS - Visor de Humedales Urbanos y SINADER de Chile

Visor cartográfico web (WebGIS) que muestra en un mapa interactivo los **Humedales Urbanos** de Chile junto con los **establecimientos SINADER** (declaraciones de residuos), y permite realizar **geoprocesos espaciales** directamente en el navegador, sin necesidad de servidor ni instalación.

## ¿Qué ofrece?

- Mapa base oscuro (CartoDB) de todo Chile con capas interactivas:
  - **Humedales Urbanos** (polígonos, Ministerio del Medio Ambiente).
  - **SINADER 2024** (~9.100 establecimientos declarantes de residuos).
- Panel con filtros por región y toggles de visibilidad por capa.
- Popups con la información de cada entidad al hacer clic.
- **Geoprocesos integrados (100% en el navegador):**
  - **Buffer (Turf.js)**: genera zonas de influencia alrededor de los puntos (con opción de disolución y filtros por región).
  - **Intersección espacial**: cruza dos capas (Humedales, SINADER o el buffer generado) y calcula los polígonos/puntos resultantes, usando Web Worker para no congelar la interfaz.
  - Reproyección automática de coordenadas (EPSG:3857 → WGS84) con proj4js.
- **Exportación** de resultados en **GeoJSON** y **Shapefile** (`.zip`).

## Cómo usarlo

Este visor es una **aplicación 100% cliente** (HTML + JavaScript), diseñada para publicarse en GitHub Pages:

1. Abre la página en tu navegador (o utiliza GitHub Pages).
2. Activa/desactiva capas con los toggles del panel izquierdo.
3. Aplica un filtro regional si quieres trabajar una zona específica.
4. Genera un buffer sobre los establecimientos o cruza capas con el geoproceso de intersección.
5. Exporta los resultados en GeoJSON o Shapefile para usarlos en QGIS/ArcGIS.

## Tecnologías

- HTML5 + JavaScript (Vanilla, arquitectura modular con IIFEs).
- **MapLibre GL JS** para el mapa interactivo.
- **Turf.js 7.1.0** para geoprocesamiento espacial.
- **proj4js** para transformaciones de coordenadas.
- **@mapbox/shp-write** para exportación a Shapefile.
- **Web Workers** para procesar grandes volúmenes sin bloquear la interfaz.
- **IndexedDB** para almacenar en caché los resultados (el buffer generado sobrevive a recargas).

## Datos

- Humedales Urbanos: Ministerio del Medio Ambiente de Chile.
- SINADER 2024: Sistema Nacional de Declaración de Residuos, información pública agregada por establecimiento.

## Despliegue

Publicado automáticamente con **GitHub Pages** desde la rama `main` (carpeta raíz).