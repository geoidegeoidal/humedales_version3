# Humedales WebGIS
**Humedales urbanos y establecimientos SINADER de Chile**

Explora ambas capas, filtra por región y realiza **buffers e intersecciones espaciales en el navegador**. Exporta los resultados para continuar el trabajo en QGIS o ArcGIS.

**[Inicio rápido](#inicio-rápido) · [Operaciones](#operaciones) · [Datos](#datos) · [Tecnologías](#tecnologías)**

> **Alcance:** es un visor exploratorio. La proximidad o intersección espacial entre establecimientos y humedales no demuestra por sí sola un impacto ambiental.

## Inicio rápido

No hay un paso de compilación ni un backend propio. Para usar una copia local, sirve los archivos desde la raíz del repositorio en lugar de abrir `index.html` con `file://`.

Con **Git y Python 3** disponibles:

```bash
git clone https://github.com/geoidegeoidal/humedales_version3.git
cd humedales_version3
python -m http.server 8000 --bind 127.0.0.1
```

Abre **http://127.0.0.1:8000/**. En Windows, si tu instalación usa el lanzador `py`, puedes sustituir `python` por `py -3`.

**Requiere conexión para los recursos externos:** las capas están incluidas en el repositorio, pero el mapa base de CARTO y varias bibliotecas se cargan desde servicios/CDN. Ejecutar los geoprocesos en el navegador no equivale a disponer de un visor completamente offline.

## Primer recorrido

1. **Explora:** activa o desactiva Humedales Urbanos y SINADER desde el panel.
2. **Delimita:** aplica el filtro regional para trabajar en una zona.
3. **Consulta:** selecciona una entidad del mapa para revisar sus atributos.
4. **Analiza:** genera un buffer o selecciona las capas que quieres intersectar.
5. **Exporta:** descarga la selección o el resultado en GeoJSON o Shapefile.

## Operaciones

| Operación | Qué permite | Qué revisar |
| :--- | :--- | :--- |
| **Capas y filtros** | Mostrar humedales y establecimientos; filtrar por región | Visibilidad y filtros activos antes de exportar |
| **Buffer** | Crear zonas de influencia alrededor de puntos, con opción de disolución | Distancia, región y capa de origen elegidas |
| **Intersección** | Cruzar Humedales, SINADER o un buffer generado | Tipos de geometría de las entradas y entidades resultantes |
| **GeoJSON** | Descargar datos para continuar el análisis en otro SIG | Atributos, coordenadas y alcance del resultado |
| **Shapefile** | Descargar un ZIP con los archivos del formato | Extraer el conjunto completo antes de abrirlo en un SIG |

El visor incorpora transformación de coordenadas **EPSG:3857 → WGS84** con proj4js. Los procesos pesados utilizan Web Workers; su duración y el consumo de memoria dependen del volumen y la complejidad de los datos.

## Datos

| Capa | Fuente | Archivos incluidos |
| :--- | :--- | :--- |
| **Humedales Urbanos** | Ministerio del Medio Ambiente de Chile | [GeoJSON](Humedales%20Urbanos%20%281%29.geojson) · [carga JavaScript](humedales_data.js) |
| **SINADER 2024** | Sistema Nacional de Declaración de Residuos; datos agregados por establecimiento | [GeoJSON](sinader_2024_establecimientos.geojson) · [carga JavaScript](sinader_data.js) |

Las capas representan los archivos versionados del proyecto, no una consulta en tiempo real a los sistemas de origen. Revisa su cobertura, fecha y atributos antes de utilizarlas para decisiones o informes.

## Tecnologías

| Componente | Función |
| :--- | :--- |
| **HTML + JavaScript** | Aplicación estática organizada con módulos IIFE |
| **MapLibre GL JS** | Navegación cartográfica y capas interactivas |
| **Turf.js 7.1.0** | Geoprocesamiento espacial |
| **proj4js** | Transformación de coordenadas |
| **@mapbox/shp-write** | Exportación a Shapefile |
| **Web Workers** | Trabajo de geoprocesamiento fuera del hilo principal |
| **IndexedDB** | Caché local de resultados, incluido el buffer generado |

La caché pertenece al navegador y al sitio desde el que lo abres. No sustituye una exportación de los resultados que quieras conservar.

## Estructura y publicación

- [`index.html`](index.html): interfaz, mapa y lógica de la aplicación.
- `humedales_data.js` y `sinader_data.js`: capas cargadas por el visor.
- Archivos `.geojson`: fuentes versionadas.
- [`convert_sinader.py`](convert_sinader.py): preparación de los datos SINADER.

El proyecto puede publicarse como sitio estático en **GitHub Pages**, desde la rama `main` y la carpeta raíz. Mantén juntos `index.html` y los archivos de datos para que funcionen las rutas relativas.
