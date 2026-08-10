# Bitácora de Desarrollo - Contrato

Este documento funcionará como una bitácora central y contrato de desarrollo para mantener sincronizados a todos los agentes de programación que trabajen en este proyecto.

## Principios y Reglas (KISS)
- **Carpeta de Trabajo Oficial:** La única carpeta de trabajo autorizada para este proyecto es `c:\JORGE\v3\`. Todos los archivos y modificaciones deben realizarse exclusivamente en este directorio.
- **Mantener el código estúpidamente simple (KISS):** Evitar sobreingeniería o scripts innecesariamente complejos.
- **Single Source of Truth:** Este archivo es la fuente de verdad de lo que se está construyendo.
- **INSTRUCCIÓN OBLIGATORIA:** TODO agente de inteligencia artificial que modifique el código, añada archivos o realice cualquier cambio, tiene la OBLIGACIÓN ESTRICTA de registrar detalladamente sus acciones en la sección "Historial de Cambios" de esta bitácora antes de dar por finalizada su tarea.

## Historial de Cambios

### 2026-08-07 - Inicialización del Proyecto
- **Agente:** Antigravity
- **Acciones:**
  - Configuración inicial de `index.html` con estructura HTML5 base.
  - Inclusión de CDNs para **Tailwind CSS** (estilos) y **MapLibre GL JS** (mapas).
  - Configuración del body con fondo oscuro (`bg-slate-950`), texto claro y contenedor central a pantalla completa (`h-screen w-full`).
  - Creación de este documento `contrato.md` como bitácora de desarrollo en la ruta raíz.

### 2026-08-08 - Instanciación de Mapa Base (Chile & CartoDB Dark)
- **Agente:** Antigravity (Desarrollador Web Espacial)
- **Acciones:**
  - Actualización del id del contenedor principal a `map` (`<div id="map">`).
  - Adición del bloque `<script>` de inicialización en Vanilla JS al final del `<body>`.
  - Instanciación de `maplibregl.Map` apuntando al elemento `#map`.
  - Configuración del mapa base oscuro de CartoDB (`dark-matter-gl-style`).
  - Centrado de la vista en Chile (coordenadas `[-71.543, -35.6751]`) con zoom inicial de `4`.

### 2026-08-08 - Corrección de Visibilidad del Mapa
- **Agente:** Antigravity (Desarrollador Web Espacial)
- **Acciones:**
  - Definición explícita de estilo CSS `#map { width: 100vw; height: 100vh; }` para evitar contenedores con altura 0px.
  - Cambio de la URL de estilo remoto a un objeto de estilo inline con tiles de CartoDB Dark Matter (`https://*.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}.png`), solucionando bloqueos CORS al abrir el archivo directamente con protocolo `file://`.
  - Adición de listener `window.addEventListener('load', () => map.resize())` para asegurar el ajuste de dimensiones y renderizado inmediato en pantalla.

### 2026-08-08 - Configuración Directa para Renderizado Web
- **Agente:** Antigravity (Desarrollador Web Espacial)
- **Acciones:**
  - Reestructuración completa y simplificación directa de `index.html`.
  - Configuración del CSS del lienzo con `position: absolute; top:0; bottom:0; width:100%; height:100%;` para garantizar el viewport completo instantáneo.
  - Implementación del estilo oficial vectorial CartoDB Dark Matter (`https://basemaps.cartocdn.com/gl/dark-matter-gl-style/style.json`).
  - Adición de controles de navegación MapLibre (`NavigationControl`).

### 2026-08-08 - Análisis de Datos Espaciales (Atributos GeoJSON)
- **Agente:** Antigravity (Analista de Datos Espaciales)
- **Acciones:**
  - Registro de `c:\JORGE\v3\` como carpeta de trabajo oficial en las reglas del contrato.
  - Lectura e inspección mediante Python de la estructura de atributos del dataset GeoJSON nacional (`Humedales Urbanos (1).geojson` con 107 entidades).
  - Documentación del esquema completo de campos (atributos, tipos de datos y valores de ejemplo).

### 2026-08-08 - Filtro Regional Desplegable y Zoom Automático
- **Agente:** Antigravity (Desarrollador Frontend & Espacial)
- **Acciones:**
  - Creación de un panel lateral UI en `index.html` con diseño oscuro moderno (Tailwind CSS, glassmorphism).
  - Incorporación de un menú desplegable clásico (`<select id="region-select">`) poblado dinámicamente con las regiones extraídas del atributo `region`.
  - Carga y renderizado de la capa GeoJSON `Humedales Urbanos (1).geojson` con estilos de relleno (`#06b6d4`, opacidad 0.45) y contorno (`#22d3ee`).
  - Implementación del filtrado dinámico MapLibre (`map.setFilter`) según la región seleccionada.
  - Algoritmo de cálculo de Bounding Box (`calculateBbox`) en Vanilla JS para realizar zoom automático e interactivo (`map.fitBounds`) a la extensión espacial de la región filtrada.
  - Inclusión de Popups informativos interactivos al hacer clic en cualquier humedal.

### 2026-08-08 - Solución a Bloqueo CORS en Protocolo Local (file://)
- **Agente:** Antigravity (Desarrollador Web Espacial)
- **Acciones:**
  - Generación mediante Python del script `humedales_data.js` que asigna el conjunto de datos GeoJSON a la variable global `window.humedalesData`.
  - Inclusión de `<script src="humedales_data.js"></script>` en `index.html`.
  - Eliminación total del bloqueo CORS al abrir el archivo directamente con doble clic (`file:///C:/JORGE/v3/index.html`) en navegadores como Chrome o Edge.
  - Mantenimiento de mecanismo de fallback con `fetch` para compatibilidad con servidores web.

### 2026-08-08 - A/B Testing UI: Creación de indexv2.html con "Neón Chips"
- **Agente:** Antigravity (Desarrollador Frontend & Espacial)
- **Acciones:**
  - Creación del archivo alternativo `indexv2.html` a partir de `index.html` para pruebas de A/B testing.
  - Implementación de un grupo horizontal de botones ("Neón Chips") con scroll horizontal suave en la barra superior.
  - Aplicación de diseño **Glassmorphism** (`bg-slate-900/85 backdrop-blur-xl border border-slate-800`).
  - Definición del efecto de resplandor neón (`box-shadow: 0 0 16px rgba(6, 182, 212, 0.7)`) para la clase `.neon-chip-active` del chip seleccionado.
  - Conexión mediante Vanilla JS para alternar el chip activo y aplicar al instante el filtro `map.setFilter` y el encuadre espacial `map.fitBounds` a la región correspondientes.
  - Mantenimiento del dataset sin problemas CORS mediante `humedales_data.js`.

### 2026-08-08 - Finalización A/B Testing: Selección Definitiva de index.html
- **Agente:** Antigravity (Desarrollador Frontend & Espacial)
- **Acciones:**
  - Conclusión del A/B testing por decisión del usuario.
  - Selección definitiva de `index.html` (Panel Lateral con Menú Desplegable Clásico) como interfaz oficial del proyecto.
  - Eliminación manual del archivo `indexv2.html` confirmada y registrada en la bitácora.

### 2026-08-08 - Rediseño del Popup de Humedales con Flat Design
- **Agente:** Antigravity (Desarrollador Frontend & Espacial)
- **Acciones:**
  - Reconstrucción del popup de clic en humedales (`map.on('click', 'humedales-fill')`) bajo el paradigma **Flat Design**.
  - Anulación del diseño por defecto de MapLibre inyectando CSS que sobreescribe `.maplibregl-popup-content`:
    - Superficie sólida de un solo color (`#f8fafc`), `border-radius: 0`, `box-shadow: none`, `border: 1px solid #0f172a`.
    - Sin gradientes, brillo, textura ni profundidad simulada; los bordes se definen por cambio de color.
  - Recoloración sólida del triángulo del popup (`.maplibregl-popup-tip`) para los 4 anclajes (`top/bottom/left/right`), manteniendo el borde por contraste contra el mapa oscuro.
  - Rediseño del botón de cierre (`.maplibregl-popup-close-button`) como cuadrado plano sin sombra, con estados `hover` (`#e2e8f0`), `active` (`#cbd5e1`) y anillo de foco visible (`focus-visible`).
  - Nueva estructura interna semántica con bloques de color para jerarquía:
    - `.flat-popup__header`: bloque sólido oscuro (`#0f172a`) con texto claro (`#f8fafc`) y glifo geométrico simple de un solo color (`#0e7490`).
    - `.flat-popup__body`: bloque claro sólido con filas (`Código`, `Comuna`, `Superficie`, `Proceso`) separadas por líneas de `1px solid #e2e8f0`.
    - `.flat-popup__link`: botón sólido (`#0e7490` / texto `#ffffff`) como affordance por color, con estados `hover` (`#155e75`), `active` (`#164e63`) y anillo de foco visible.
  - Cumplimiento de contraste de texto ≥ 4.5:1 (pares verificados: `#0f172a/#f8fafc`, `#0e7490/#f8fafc`, `#ffffff/#0e7490`).
  - Elementos interactivos identificables sin sombras: affordance por color, estados hover/pressed y anillos de foco visibles.

### 2026-08-08 - Rediseño UI Completo con Flat Design (Arquitecto UI)
- **Agente:** Antigravity (Arquitecto UI / Desarrollador Frontend & Espacial)
- **Acciones:**
  - Aplicación de un rediseño completo de `index.html` bajo el paradigma **Flat Design** como sistema de diseño global (no solo popup).
  - **Eliminación del CDN de Tailwind CSS** y de todo el estilo glassmorphism previo (transparencias, `backdrop-blur`, `shadow-2xl`, `rounded-2xl`, `rounded-full`) en favor de CSS puro y plano (KISS, menos dependencias).
  - Nuevo sistema de diseño en CSS puro con superficies de **relleno sólido de un solo color** (sin gradientes, brillo, textura ni profundidad simulada):
    - Panel lateral `.flat-panel`: superficie sólida `#0f172a` con `border: 1px solid #475569`, `box-shadow: none`, `border-radius: 0`.
    - Encabezado `.flat-panel__header`: bloque de color sólido `#0e7490` con texto `#ffffff` (jerarquía por bloques de color) y glifo geométrico simple de un solo color (`#22d3ee`).
    - Etiquetas `.flat-panel__label`: tipografía sans-serif limpia, mayúsculas con `letter-spacing`, color `#22d3ee`.
  - **Desplegable `.flat-select`**: superficie sólida `#1e293b`, `appearance: none`, flecha geométrica SVG de un solo color (`#22d3ee`) como `background-image` (glifo, no gradiente), `border: 1px solid #475569`, estado `hover` por cambio de color de borde y anillo de foco visible (`focus-visible`).
  - **Contador `.flat-panel__stat`**: bloque sólido `#1e293b` con borde `1px solid #475569`; valor en bloque sólido `#0e7490` con texto blanco (affordance por color, sin sombras).
  - **Controles de mapa (override de MapLibre)**: `.maplibregl-ctrl-group` y `.maplibregl-ctrl-attrib` rediseñados como superficies sólidas claras (`#f8fafc`) con `border: 1px solid #0f172a`, `box-shadow: none`, `border-radius: 0`; botones con estados `hover` (`#e2e8f0`), `active` (`#cbd5e1`) y anillo de foco visible.
  - Tipografía global sans-serif limpia (`'Segoe UI', system-ui, ...`) y cuerpo en `#0f172a` con texto `#f8fafc`.
  - **Contraste 4.5:1 garantizado** en todos los pares de color utilizados: `#0f172a/#f8fafc` (~17.5:1), `#22d3ee/#0f172a` (~9.9:1), `#94a3b8/#1e293b` (~6.6:1), `#ffffff/#0e7490` (~5.4:1), `#cffafe/#0e7490` (~4.7:1).
  - Todos los elementos interactivos (desplegable, botón de cierre, enlace, controles de mapa) son identificables **sin sombras**: affordance por color, estados hover/pressed visibles y anillos de foco visibles.
  - Se preserva íntegra la lógica espacial (filtro regional, `fitBounds`, popups flat) sin cambios funcionales.

### 2026-08-09 - Incorporación del Dataset SINADER 2024 como Capa GeoJSON
- **Agente:** Antigravity (Desarrollador Web Espacial / Analista de Datos Espaciales)
- **Acciones:**
  - Conversión del dataset `gi-sinader-2024-ckan (1) (1).xlsx` (hoja `Datos`, 241.687 declaraciones de residuos del SINADER año 2024) a un GeoJSON de puntos a partir de los campos `latitud` y `longitud`.
  - **Agregación por establecimiento (`id_vu`)**: se generó un feature Point por cada establecimiento único (9.101 features), conservando por requerimiento del usuario la **sumatoria de toneladas** (`total_toneladas`), el número de declaraciones (`num_declaraciones`) y los metadatos principales (`razon_social`, `nombre_establecimiento`, `rubro`, `region`, `provincia`, `comuna`).
  - Filtrado de coordenadas inválidas fuera del rango chileno (latitud `-60..-15`, longitud `-80..-65`): 241.461 registros válidos de 241.687.
  - Archivos generados:
    - `sinader_2024_establecimientos.geojson` (~3,98 MB, FeatureCollection CRS84).
    - `sinader_data.js` (~3,98 MB) que asigna el dataset a `window.sinaderData` para eliminar bloqueos CORS en protocolo `file://`, siguiendo el patrón existente de `humedales_data.js`.
    - `convert_sinader.py`: script reutilizable de conversión y agregación (KISS, pandas/openpyxl).
  - **Integración en `index.html`** (manteniendo el Flat Design):
    - Carga de `<script src="sinader_data.js">` y de la capa de puntos `sinader-points` (círculos `#f59e0b` con contorno `#0f172a`).
    - Panel con **Toggles de visibilidad de capas** (Humedales Urbanos y SINADER 2024), ambas capas visibles a la vez por decisión del usuario.
    - Segundo contador de estadísticas (`Establecimientos SINADER`) junto al existente de humedales.
    - Filtro regional desplegable ahora se puebla con las regiones de **ambos** datasets (16 regiones del SINADER) y aplica `map.setFilter` simultáneamente a las capas de humedales y SINADER.
    - Zoom automático (`calculateBbox` + `map.fitBounds`) calculado sobre las entidades combinadas de ambas capas para la región seleccionada.
    - Popup Flat Design propio para los establecimientos SINADER (Razón Social, Rubro, Comuna, Declaraciones, Toneladas 2024) al hacer clic.
    - Funciones auxiliares nuevas: `setLayerVisible` (visibilidad por toggle) y `updateVisibleCounts` (actualización de contadores según toggle y región).
  - Actualización de título de la página y encabezado del panel para reflejar ambos datasets.
  - Verificación: sintaxis del JS inline validada con `node --check` y estructura del GeoJSON validada con Python.

### 2026-08-09 - Normalización de Nombres de Región (SINADER 2024)
- **Agente:** Antigravity (Analista de Datos Espaciales)
- **Problema:** El campo `region` del dataset SINADER usaba abreviaturas/grafías distintas a los nombres oficiales usados por Humedales (`Aysén del Gral. Carlos Ibañez del Campo` vs `Aysén del General Carlos Ibáñez del Campo`; `Libertador Gral. Bernardo O'Higgins` vs `Libertador General Bernardo O'Higgins`), lo que generaba opciones duplicadas aparentes en el desplegable del filtro regional.
- **Acciones:**
  - Adición en `convert_sinader.py` de una lista `CANONICAL_REGIONS` con los 16 nombres oficiales de las regiones de Chile y de la función `normalize_region` (con clave normalizada `_normalize_key`: minúsculas, sin tildes vía NFKD, expansión de `Gral.` → `General`, colapso de espacios y normalización de apóstrofos).
  - Aplicación de `df["region"].map(normalize_region)` antes de la agregación por establecimiento.
  - Regeneración de `sinader_2024_establecimientos.geojson` y `sinader_data.js` (9.101 features por establecimiento; por diseño los 16 grupos mapean 1:1 al canónico sin variantes residuales).
  - Verificación: 16 opciones únicas en el desplegable combinado (Humedales + SINADER), sin duplicados.

### 2026-08-09 - Módulo de Exportación Cliente (GeoJSON + Shapefile)
- **Agente:** Antigravity (Desarrollador WebGIS Senior)
- **Contexto:** El visor se aloja en GitHub Pages sin backend; toda la exportación se resuelve 100% en el navegador.
- **Acciones:**
  - **Dependencias JS (CDN):**
    - `@mapbox/shp-write@0.4.3/shpwrite.js` vía unpkg (expone `window.shpwrite`, usa `shpwrite.zip(fc, {outputType:'blob'})` → `Promise<Blob>` y **empaqueta JSZip 3.x internamente**, por lo que no se requiere un CDN adicional de JSZip).
    - Se descartó `shp-write@0.3.2` por incompatibilidad conocida: su build de navegador llama `zip.generate({compression:'STORE'})` sin `type`, lo que lanza `"No output type specified"` con el JSZip 3.x empaquetado.
  - **Módulo `ExportModule` (IIFE, KISS, en `index.html`):**
    - `collectSelected()`: captura la selección activa usando la **API nativa de MapLibre** (`map.getFilter(id)` + `map.getLayoutProperty(id, 'visibility')`) y re-evalúa la misma expresión sobre los stores en memoria (`geojsonStore`/`sinaderStore`), garantizando captura precisa e independiente del viewport/zoom.
    - `featureMatches()`: evaluador KISS de expresiones de filtro (`==`, `!=`, `any`, `all`; filtro nulo = todo).
    - `exportGeoJSON()`: serializa la selección a `FeatureCollection` y descarga como Blob `application/geo+json`.
    - `exportShapefile()`: invoca `shpwrite.zip()` con `folder`/`types` (separando `establecimientos_sinader` puntos y `humedales_urbanos` polígonos en archivos distintos dentro del .zip) y `compression:'DEFLATE'`.
    - `setBusy()`/spinner: manejo de estado asíncrono; muestra spinner durante la compresión ZIP y deshabilita ambos botones mientras exporta.
    - `updateState()`: **deshabilita los botones si el filtro resulta nulo/vacío** y muestra el conteo de entidades listas; se sincroniza desde `updateVisibleCounts()` en cada cambio de región o toggle.
    - `triggerDownload()` + `fileName()`: descarga por objeto URL con nombre `seleccion_<region>_<fecha>.(geojson|zip)`.
  - **UI/UX (Flat Design consistente):** botones `.flat-btn` con estados hover/active/focus, estado `:disabled` sólido gris, fila de estado `.flat-export-status` y spinner CSS plano (cuadrado rotatorio `@keyframes flat-spin`); bloque "Exportar Selección" nuevo en el panel lateral junto a los contadores.
  - **Verificación funcional real (Node + JSZip):** con la selección regional "Biobío" (16 MultiPolygon humedales + 525 Point SINADER) el `.zip` resultante contiene `.shp/.shx/.dbf/.prj` de ambas geometrías; SHP magic `0x270A` (9994 BE), DBF dBase III `0x03` y PRJ WGS84 validados. JS inline validado con `node --check`.

### 2026-08-09 - Selector de Capa para Exportación
- **Agente:** Antigravity (Desarrollador WebGIS Senior)
- **Motivo:** El módulo de exportación descargaba ambas capas sin indicar cuál era; requerido un selector que permita elegir la capa a descargar.
- **Acciones:**
  - Adición del desplegable `export-layer-select` (valores: `all`="Ambas capas", `humedales`="Humedales Urbanos", `sinader`="SINADER 2024 (Establecimientos)") en el bloque "Exportar Selección" del panel, reutilizando la clase `.flat-select` existente (Flat Design).
  - Refactor de `ExportModule`:
    - `selectedLayer()`: lee el valor vigente del selector.
    - `collectSelected()`: ahora filtra por la capa seleccionada (`all`/`humedales`/`sinader`) manteniendo la captura nativa vía `map.getFilter`/`map.getLayoutProperty` y el respeto a los toggles de visibilidad.
    - `layerName()`: nombre legible de la capa para el estado y el nombre de archivo.
    - `fileName()`: incorpora la capa al nombre (`seleccion_humedales_urbanos_<region>_<fecha>`).
    - `updateState()`: el mensaje de estado ahora indica qué capa se exportará (p. ej. `16 entidades (Humedales Urbanos)`); listener `change` en el selector para refrescar contador/estado al instante.
  - **Verificación funcional (Node + shp-write):** para región "Biobío" se validaron los tres escenarios: `humedales` (16 MultiPolygon, zip con `humedales_urbanos.{shp,shx,dbf,prj}`), `sinader` (525 Point, zip con `establecimientos_sinader.*`) y `all` (541 entidades, ambos juegos de archivos en el zip). JS inline validado con `node --check`.

### 2026-08-09 - Módulo de Buffer / Áreas de Influencia (Turf.js) + Caché IndexedDB
- **Agente:** Antigravity (Desarrollador WebGIS Senior)
- **Contexto:** Geoproceso estrictamente client-side para GitHub Pages (serverless, sin backend).
- **Acciones:**
  - **Dependencias JS (CDN):**
    - `@turf/turf@7.1.0/turf.min.js` vía jsDelivr (expone `window.turf` con `buffer` y `dissolve`; verificado en el bundle). En el módulo se usa en el hilo principal y, opcionalmente, dentro de un **Web Worker** vía `importScripts` del mismo CDN.
  - **UI (Flat Design consistente) en `index.html`:** bloque "Buffer (Turf.js)" en el panel lateral con:
    - Input numérico `.flat-input` para el **radio en metros** (default 500).
    - Toggle `buffer-dissolve` para alternar **disolver (unir polígonos)** vs. entidades individuales.
    - Desplegable `buffer-context` (`.flat-select`) con dos contextos: **"Solo datos filtrados en el mapa"** (respeta filtro regional y toggles de MapLibre) y **"Dataset completo en memoria"**.
    - Botones Generar/Limpiar + descargas **GeoJSON** y **Shapefile (.zip)** con spinner de estado.
  - **Módulo `BufferModule` (IIFE, KISS):**
    - `collectSourceFeatures()`: captura las entidades según contexto usando la API nativa de MapLibre (`map.getFilter` / `map.getLayoutProperty`) cuando el contexto es `filtered`, o los stores completos en `full`.
    - `runBuffer()`: **asíncrono con Web Worker** (Blob + `importScripts(TURF_CDN)`), timeout de 30s y **fallback al hilo principal** si el Worker no está disponible (file://, CSP, etc.).
    - `bufferInMainThread()` + worker: `turf.buffer(fc, radius, {units:'meters'})` y `turf.dissolve` cuando está activo.
    - `explodeMultiPolygons()`: **corrección crítica** — `turf.dissolve` en v7 exige estrictamente `Polygon` y falla con `MultiPolygon`; se explotan los MultiPolygons en Polygons individuales antes de disolver (aplica tanto en main thread como en worker).
    - **Caché IndexedDB** (`webgis-buffer-cache`, store `buffers`): el resultado se guarda con clave = firma de parámetros (`cacheKey()`: contexto, radio, dissolve, región y filtros/visibilidad de MapLibre). En un segundo llamado con los mismos parámetros **no se recalcula**; se recupera de IndexedDB (evita recálculo y mantiene la UI fluida).
    - `renderResult()`: agrega las capas `buffer-fill` / `buffer-line` (fuente `buffer-src`) en tono violeta (#a78bfa/#8b5cf6), reutilizando `setData` si ya existen.
    - `exportGeoJSON()` / `exportShapefile()`: descargan el buffer **vigente desde caché**; Shapefile empaquetado con `shpwrite.zip()` (`folder:'buffer'`, `types` unificados a `buffer`, `outputType:'blob'`, `compression:'DEFLATE'`).
    - `updateButtons()`: deshabilita descargas si no hay buffer generado; `setBusy()` maneja spinner asíncrono durante cálculo/compresión.
  - **Verificación funcional real (Node + turf@7.1.0 + shp-write):**
    - Contexto `filtered` (región "Biobío", 541 entradas): buffer individual = 541 features; dissolved = 149 features (Polygon).
    - Contexto `full` (9.208 entradas): buffer individual = 9.208; dissolved = 2.546 features (Polygon).
    - Exportación del buffer dissolved a `.zip`: contiene `buffer/buffer.{shp,shx,dbf,prj}`, SHP magic `0x270A` (9994 BE) validado.
    - JS inline validado con `node --check`.

### 2026-08-09 - Módulo de Intersección Espacial (Turf.js + Worker + proj4)
- **Agente:** Antigravity (Arquitecto de Software / Desarrollador WebGIS Senior)
- **Contexto:** Geoproceso estrictamente client-side para GitHub Pages (serverless). El usuario selecciona dinámicamente dos capas (A base / B recorte) y el visor ejecuta la intersección topológica respetando filtros regionales y toggles de visibilidad vigentes.
- **Esquema de arquitectura (separación de responsabilidades):**
  ```
  UI (index.html, Flat Design)
    ├─ Panel "Intersección Espacial": selects A/B, contexto, botones, estado,
    │   barra de progreso y notificaciones Toast (flat-toast-wrap).
    │
    ├─ [IntersectModule] (orquestador / capa de aplicación)
    │   ├─ collectLayerFeatures()  → respeta filtro+visibilidad vía API nativa MapLibre
    │   ├─ generate()              → validación CRS → despacho → caché → render
    │   ├─ renderResult()          → capas MapLibre (intersect-fill/line/points)
    │   ├─ exportGeoJSON()/exportShapefile() → .geojson y .zip (.shp/.shx/.dbf/.prj)
    │   └─ setBusy/showProgress/Toast → estados de carga y retroalimentación
    │
    ├─ [CrsModule] (validación CRS)
    │   └─ detect() + normalizeTo4326()  → estándar único EPSG:4326 (proj4 opcional)
    │
    ├─ [Cache] IndexedDB "webgis-intersect-cache" → clave = firma de parámetros
    │
    └─ Núcleo de intersección (funciones PURAS serializables, KISS/SRP)
        ├─ geomBBox / bboxIntersects           → pre-filtrado espacial (malla bbox)
        ├─ cleanTopology (buffer(0))           → saneo de errores topológicos
        ├─ explodePolygonParts                 → MultiPolygon → Polygon (requisito polygon-clipping)
        ├─ pointSegFraction/projectOnLine/positionAt/linePartBetween
        │                                     → recorte de líneas por polígono
        └─ intersectCollectionsRaw             → despacho por par de tipos geométricos
           └── Se ejecuta en: (a) Web Worker Blob + importScripts(turf CDN), o
               (b) hilo principal por lotes (chunks async) si el Worker no está
               disponible (file://, CSP); progreso real en ambos caminos.
  ```
- **Lógica de la intersección (despacho por tipos geométricos, `intersectCollectionsRaw`):**
  - `punto ∩ polígono` y su espejo `polígono ∩ punto` → `turf.booleanPointInPolygon` con pre-filtrado por bbox (resultado puntual).
  - `polígono ∩ polígono` → `turf.intersect({GeoJSON de AMBAS geometrías en UN solo FeatureCollection})`; ante error topológico se sanea con `buffer(0)` y se reintenta; `explodePolygonParts` descompone MultiPolygons (mismo refinamiento ya aplicado a `turf.dissolve`).
  - `línea ∩ polígono` y su espejo → recorte por intersecciones (`turf.lineIntersect` sobre el contorno) + test de punto medio; resultado lineal con preservación de vértices.
  - `línea ∩ línea` → puntos de cruce (`turf.lineIntersect`, dedupe por coordenada).
  - `punto ∩ línea` y su espejo → `turf.booleanPointOnLine`.
  - `punto ∩ punto` → sin topología definida; advertencia documentada en `stats.note`.
  - Manejo riguroso de errores topológicos: conteo de entidades descartadas (`skipped`), geometrías saneadas (`cleaned`), sin excepciones que rompan el flujo; toasts de éxito/advertencia/error.
- **CRS (CrsModule):**
  - Detección por miembro `crs` (nombres EPSG/URN) + heurística por extensión del bbox (±180/±90 → 4326; ±20037508 → 3857).
  - Estandarización SÓLO a EPSG:4326 (WGS84) — idéntico al CRS nativo de GeoJSON/MapLibre y del `.prj` de exportación; evita distorsiones métricas en los predicados puntuales.
  - Reproyección 3857→4326 con **proj4** (CDN cdnjs, dependencia de refuerzo): si no está disponible se opera bajo supuesto de coordenadas geográficas (advertido).
- **Aislamiento del procesamiento pesado (SRP):**
  - Web Worker creado desde Blob con `importScripts('...turf.min.js')`; las funciones puras del núcleo se serializan con `.toString()` (sin duplicación de lógica) y se re-ejecutan dentro del Worker.
  - Timeout de 60 s y fallback automático al hilo principal por **lotes asíncronos** (chunks + `await setTimeout(0)`) que mantienen la UI responsiva y reportan progreso (barra `flat-progress`).
  - Caché IndexedDB con firma de parámetros (capas, contexto, región, filtros/visibilidad MapLibre, tipos y flags de transformación) — un segundo llamado idéntico no recalcula.
- **Exportación (obligatoria GeoJSON + Shapefile):**
  - `GeoJSON` → Blob `application/geo+json` (caso `export-*`).
  - `Shapefile` → `shpwrite.zip(fc, { folder:'interseccion', types:{ point/multipoint → interseccion_puntos, line/multiline → interseccion_lineas, polygon/multipolygon → interseccion_poligonos }, outputType:'blob', compression:'DEFLATE' })` → `.zip` con `.shp/.shx/.dbf/.prj` separados por tipo de geometría (evita colisiones en resultados mixtos puntos/líneas/polígonos).
- **UI/UX (Flat Design consistente):**
  - Selectores intuitivos de capa A/B con contexto (filtrado vs. dataset completo), bloque al final del panel junto a Buffer.
  - Estados de carga: spinner plano + barra de progreso + mensajes de estado con `aria-live`.
  - **Sistema de notificaciones Toast** (`.flat-toast--success/error/warning/info`): retroalimentación en los 3 caminos (éxito, admonición, error); botón de cierre y autodesvanecimiento.
  - Resultado renderizado en verde esmeralda (`#10b981`) para diferenciarlo de humedales (`#06b6d4`) y buffer (`#a78bfa`); `fitBounds` automático al resultado.
- **Dependencias JS (CDN) y justificación metodológica:**
  - `@turf/turf@7.1.0` (jsDelivr): suite completa de geoprocesamiento ya presente en el proyecto; se reutiliza para predicados (`booleanPointInPolygon`, `booleanPointOnLine`), operaciones (`intersect`, `lineIntersect`, `polygonToLine`, `buffer`) y helpers. **Advertencia metodológica:** `turf.intersect` en 7.1.0 requiere UN único `FeatureCollection` con ambas geometrías (un segundo argumento se interpreta como `options`) y exige `Polygon` (no `MultiPolygon`) — corregido con `explodePolygonParts` y la firma correcta, constatado en la verificación.
  - `proj4js@2.14.0` (cdnjs): transformaciones de coordenadas (3857→4326). Seleccionado por ser el estándar de facto client-side; opcional si los datos ya son 4326.
  - `@mapbox/shp-write@0.4.3` (unpkg): empaqueta JSZip internamente; genera `.shp/.shx/.dbf/.prj` 100% client-side. Se descartó `shp-write@0.3.2` (incompatibilidad JSZip 3.x).
  - Sin backend: todos los geoprocesos y exportaciones se resuelven en el navegador (serverless/GitHub Pages).
- **Verificación funcional real (Node):**
  - Núcleo (`intersectCollectionsRaw` + helpers extraídos del HTML): `punto∩polígono` sintético (2/3 dentro), `polígono∩polígono` MultiPolygon superpuesto (cuadrado 2×2 correcto), `línea∩polígono` (recorte correcto), `línea∩línea` (cruce en [2,2]), `punto∩línea` (sobre la línea), saneo topológico `buffer(0)` sobre bowtie auto-intersectado, y pipeline con centroide inyectado (1 resultado, confirma el flujo punto∩polígono).
  - Control de realidad del dato: en todo el país `SINADER ∩ Humedales` = 0 establecimientos dentro de polígonos de humedales (resultado genuino del dataset; el control con centroide inyectado demuestra que el pipeline no está roto).
  - **Web Worker real (worker_threads):** 1.500 puntos × polígono procesado en thread aislado → 66 intersecciones, 1.434 descartados, mensajes de progreso funcionando (serialización `.toString()` válida).
  - Exportación Shapefile: `.zip` con `interseccion/interseccion_puntos.{shp,shx,dbf,prj}` y `interseccion_poligonos.{shp,shx,dbf,prj}`; SHP magic `0x0000270A` (9994 BE) y PRJ WGS84 validados.
  - CRS: FC declarado EPSG:3857 reproyectado a 4326 (lon ≈ -64,68 verificado); datos reales detectados como 4326 sin transformación; heurística ±180/±90 correcta.
  - JS inline validado con `node --check` (sin errores).

### 2026-08-09 - Scroll Vertical del Panel Lateral (Fix UI)
- **Agente:** Antigravity (Desarrollador Frontend & Espacial)
- **Problema:** El panel lateral izquierdo (`.flat-panel`) sobrepasa los límites verticales de la pantalla conforme se añadieron los bloques de Exportación, Buffer e Intersección, quedando contenido inaccesible por debajo del viewport.
- **Acciones:**
  - Contención del panel al viewport: `max-height: calc(100vh - 24px)` + `display: flex; flex-direction: column` en `.flat-panel`.
  - Encabezado fijo (no se desplaza): `flex: 0 0 auto` en `.flat-panel__header`.
  - Cuerpo desplazable: `overflow-y: auto` + `flex: 1 1 auto` en `.flat-panel__body`, de modo que solo el contenido de los bloques scrollee.
  - Scrollbar Flat Design: `::-webkit-scrollbar` (track `#0f172a`, thumb `#475569`) y `scrollbar-width: thin; scrollbar-color` para Firefox, sin redondeos ni sombras (consistente con el sistema de diseño).
  - Sin cambios en la lógica espacial ni en el HTML.

### 2026-08-09 - Buffer como Capa Seleccionable en la Intersección Espacial
- **Agente:** Antigravity (Arquitecto de Software / Desarrollador WebGIS Senior)
- **Motivo:** El módulo de intersección solo permitía elegir entre Humedales y SINADER; requerido poder usar el **buffer generado** (geoproceso Turf.js) como capa base (A) o de recorte (B).
- **Acciones:**
  - **Exposición del resultado del buffer (API privada → pública):** en `BufferModule` se añadieron `bufferVersion` (contador de cambios) y `onBufferChange` (callback de notificación), con `notifyChange()` invocado tras `generate()` y `clearBuffer()`. Nuevos accesores públicos en el `return`: `getCurrentResult()`, `getBufferVersion()`, `setOnBufferChange(fn)` — permiten a otros módulos consumir el FeatureCollection vigente sin acoplarse a la UI del buffer.
  - **Opciones "Buffer generado (Turf.js)"** en los selectores de la intersección: `<option value="buffer" disabled>` en `intersect-layer-a` y `intersect-layer-b` (inicialmente deshabilitada).
  - **`LAYER_CONFIG`** del módulo de intersección ampliado con `buffer: { label..., store: () => BufferModule.getCurrentResult(), filterLayerId: null }`.
  - **`collectLayerFeatures`** trata `buffer` como capa **materializada**: se devuelve tal cual (sin filtro regional, sin toggles de visibilidad, independiente del contexto), a diferencia de las capas vivas Humedales/SINADER.
  - **Suscripción `syncBufferOption()`** en `IntersectModule.init()`: habilita/deshabilita la opción buffer en tiempo real al generarse o limpiarse; si el buffer desaparece mientras estaba seleccionado, se revierte el selector a un valor válido (A→humedales, B→sinader) y se limpia la intersección vigente.
  - **Clave de caché** de la intersección ampliada con `bufferVersion`: al regenerar o limpiar el buffer, la firma cambia y **se invalida automáticamente** la intersección cacheadA que lo usara.
  - **Validación defensiva** en `generate()`: si se selecciona `buffer` sin resultado vigente, advertencia "Primero genera un buffer en el geoproceso..." con toast y aborta.
  - Etiqueta y nombre de archivo de exportación reflejan la capa buffer ("Buffer generado (Turf.js)").
  - **Verificación funcional real (Node):**
    - API del buffer: `getCurrentResult()` nullable inicial, `getBufferVersion()` = 0, suscripción sin error; integración verificada en el script (LAYER_CONFIG, cache key, suscripción).
    - Datos reales (Biobío): buffer de 300 m sobre el centroide de "Laguna Amalia" (Polygon) ∩ humedal real (MultiPolygon) → 1 intersección, área = 2,326 ha, atributos `_origen: "Buffer generado (Turf.js)"` y `_recorte: "Humedales Urbanos"` correctos.
    - `buffer ∩ SINADER Biobío` (polígono × punto) → 0 resultados (ningún establecimiento dentro del buffer, resultado genuino).
    - JS inline validado con `node --check` (sin errores).

### 2026-08-09 - Análisis de Estrategia de Visualización (Dashboard interactivo centrado en el mapa)
- **Agente:** Antigravity (Arquitecto Frontend / Experto en Visualización de Datos)
- **Contexto/Decisión contractual:** La dimensión analítica de la capa SINADER para gráficos es el campo **`rubro`** (19 categorías). **Humedales queda tal cual**, sin cambios ni gráficos propios en esta fase. Etapa totalmente analítica: **no se escribió código**; la propuesta está pendiente de validación del usuario.
- **Diagnóstico de la capa `sinader_2024_establecimientos.geojson` (9.101 puntos):**
  - Atributos: `id_vu, razon_social, rut_razon_social, nombre_establecimiento, rubro, region (16), provincia, comuna, num_declaraciones (1–12), total_toneladas`.
  - `rubro` con cola larga: Otras actividades (1.968), Comercio minorista (1.653), Ind. manufactureras (1.269), Pesca y acuicultura (970), Construcción (758).
  - `total_toneladas` con sesgo extremo: suma 11,5 M t, max 1.231.125 t, p90 = 1.332 t → exige escala log/ECharts o top-N.
  - El GeoJSON es un **agregado anual sin dimensión temporal** → series de tiempo descartadas en v1 (requeriría reconstrucción desde el XLSX con 241.687 declaraciones).
- **Gráficos propuestos (pendientes de validación):**
  1. Barras horizontales: rubros rankeados por toneladas totales (héroe, clic = filtro cruzado por rubro).
  2. Barras horizontales: nº de establecimientos por rubro (complemento, muestra divergencia peso vs. frecuencia).
  3. Scatter: `total_toneladas` (log) × `num_declaraciones`, color por rubro (revela outliers industriales).
- **Layout propuesto:** panel izquierdo intacto; nueva **columna derecha colapsable** `.flat-dash` (~360 px) con 3 tarjetas Flat; al colapsar el mapa recupera 100vw.
- **Arquitectura cross-filtering (KISS, 100% cliente):** `FilterStore` central (estado `{region, toggles, rubro}`) + pub/sub manual con dos suscriptores: **MapSync** (`map.setFilter`) y **ChartSync** (re-agrega desde `sinaderStore.features` con el evaluador `featureMatches` existente; se consolidará el duplicado de este evaluador en los 3 módulos). El mapa nunca es la fuente de verdad de los gráficos.
- **Librería elegida: ECharts** (CDN, `window.echarts`, funcional en `file://`). Justificación: canvas para 9.101 puntos, escala log nativa, dataZoom, tooltips; Chart.js descartado (sin log axis ni sampling robustos, exige plugins).
- **Coherencia de diseño:** heredar token por token el palette Flat actual (literales `#0f172a #1e293b #475569 #22d3ee #0e7490 #f8fafc #94a3b8 #f59e0b`), opcionalmente promovidos a `:root` como alias para consumo de ECharts. Sin gradientes, sin sombras, radius 0, focus rings `#22d3ee`.

### 2026-08-09 - Implementación del Dashboard SINADER (ECharts 5 + Cross-Filter 100% Cliente)
- **Agente:** Antigravity (Arquitecto Frontend / Desarrollador WebGIS)
- **Decisión del usuario:** no limitarse a la dimensión rubro; se implementan estadísticas asociadas a **toneladas y rubros**. **Humedales sin cambios**, tal como estaba.
- **Dependencia JS (CDN):** `echarts@5.5.1/dist/echarts.min.js` vía jsDelivr (expone `window.echarts`). Serverless, funcional en `file://`, mismo patrón de CDN que maplibre/shp-write/turf. Justificación registrada en la entrada analítica previa.
- **Estado central cross-filtering (KISS):** en el bloque de inicialización de `index.html`:
  - `dashRubro` (top-level): ÚNICA variable de estado compartida entre mapa y gráficos.
  - `matchFilter(feature, expr)`: evaluador único de expresiones MapLibre (`==`,`!=`,`any`,`all`).
  - `buildSinaderFilter()`: expresión combinada **región + rubro** para la capa SINADER.
  - `applyRegionalFilters()`: **MapSync** — propaga la expresión vigente a `map.setFilter` (SINADER: región+rubro; Humedales: solo región). Toda mutación de filtro pasa por aquí.
- **Módulo `Dashboard` (IIFE, ECharts 5):**
  - **Chart 1 · Barras horizontales** "Toneladas por rubro" (data-ink máximo, orden desc, color estable por rubro vía `RUBRO_MASTER`/palette Flat). **Clic en barra = filtro cruzado por rubro**.
  - **Chart 2 · Barras horizontales** "Establecimientos por rubro" (complemento; revela divergencia peso vs. frecuencia). **Clic en barra = filtro por rubro**.
  - **Chart 3 · Scatter** `total_toneladas` (eje log) × `num_declaraciones`, color por rubro (detecta outliers industriales). Leyenda scroll: **clic en ítem de leyenda = filtro por rubro**; **clic en punto = filtro por rubro**.
  - **KPIs:** Establecimientos, Toneladas 2024, Rubros activos y Top por toneladas, calculados con la expresión vigente.
  - **Chip de rubro activo** con botón de limpiar; nota de estado (`dash-note`) que explica filtros vigentes o advertencias.
  - **ChartSync**: `refresh()` re-agrega SIEMPRE desde `sinaderStore.features` con la expresión vigente (el mapa nunca es la fuente de verdad) y aplica `setOption` (diff) sin recrear instancias.
  - Panel **colapsable** `.flat-dash--collapsed` (botón «/» en el encabezado); al colapsar el mapa recupera todo el viewport.
- **Cableado en las funciones existentes:**
  - `filterAndZoomRegion`: ahora usa `applyRegionalFilters()` (preserva el rubro al cambiar de región) y ajusta el `fitBounds` con `right: 392` para no tapar el dashboard.
  - `updateVisibleCounts`: el contador SINADER del panel izquierdo respeta región+rubro y al final dispara `Dashboard.refresh()` + `ExportModule.updateState()`.
  - Clic en `sinader-points`: muestra popup y además fija el rubro del establecimiento (`Dashboard.setRubro(props.rubro, false)`) — dirección **mapa → gráficos**.
  - `Dashboard.init()` se invoca tras `IntersectModule.init()` en `map.on('load')`.
- **UI/UX (Flat Design estricto):** superficies sólidas `#0f172a`/`#1e293b`, bordes `#475569`, radius 0, sin sombras, etiquetas `#22d3ee`, focus rings visibles; charts sin gradientes, tooltips `#1e293b`/borde `#475569`, ejes `#94a3b8`, gridlines `#1e293b`.
- **Verificación:**
  - JS inline validado con `node --check` (exit 0, 128 KB extraídos).
  - Prueba funcional del núcleo con datos reales (Node): todo país = 9.101 est./11.517.611 t/19 rubros; rubro Minería = 167 est./1.034.212 t; Biobío+Minería = 0 (resultado genuino); Biobío solo = 525 est./17 rubros. Filtro combinado `['all', región, rubro]` correcto.
  - Humedales intacto (sin cambios funcionales ni visuales).

### 2026-08-09 - Persistencia del Buffer en Caché (IndexedDB) y Mensaje de Error Específico
- **Agente:** Antigravity (Desarrollador WebGIS Senior)
- **Problema:** Al usar el buffer generado como capa en la intersección aparecía el mensaje genérico "Una de las capas no tiene entidades (revisa filtros o toggles)". Diagnóstico con harness de reproducción (`repro_test.js`): `collectLayerFeatures` funciona correctamente; el mensaje se disparaba porque (1) `currentResult` del buffer solo vive en memoria y **se pierde al recargar la página** (caché de resultados por firma ≠ buffer vigente), o (2) la cola vacía era en realidad la **otra capa** (toggle off / filtro regional sin entidades) y el mensaje no indicaba cuál.
- **Acciones:**
  - **Cache del BufferModule con `remove(key)`** (DELETE en transaction `readwrite`) y exposición en el `return { get, set, remove }`.
  - **Persistencia del buffer vigente bajo clave fija `LAST_KEY = '__last_generated__'`** en la store `buffers` de `webgis-buffer-cache`: se escribe en `generate()` tras el cálculo y se elimina en `clearBuffer()` (al limpiar, se borra también de la caché).
  - **`restoreLastBuffer()`**: al `init()` del módulo, si existe un buffer persistido se restaura como `currentResult`, se renderiza **sin `fitBounds`** (nuevo parámetro `renderResult(fc, doFit)`, evita salto de zoom al cargar), se actualizan botones/estado y se notifica a la intersección. Así el buffer sobrevive recargas y sigue disponible como capa A/B.
  - **Mensaje de error específico** en `IntersectModule.generate()`: ahora indica el **nombre real de la capa vacía** (`LAYER_CONFIG[emptyKey].label`) y según el caso sugiere: "Regenera un buffer..." (si la vacía es `buffer`), "Revisa filtros, región o el toggle de visibilidad de esa capa" (contexto filtrado) o "El dataset está vacío" (contexto full).
- **Verificación:**
  - `node --check inline.js` (script extraído, longitud 106.882): sin errores.
  - Harness `repro_test.js` vuelto a correr: escenarios A–E correctos (buffer 1 entidad, SINADER oculto por toggle devuelve 0, contexto full devuelve datasets completos, buffer con `getCurrentResult` null → 0 entidades con sugerencia de regenerar).
- **Nota:** El resto de la caché de resultados (por firma de parámetros) no cambia; solo se añadió la clave de persistencia `__last_generated__`.

### 2026-08-09 - Publicación del Proyecto en GitHub (Git + GitHub Pages)
- **Agente:** Antigravity (Desarrollador WebGIS Senior)
- **Acciones:**
  - **Control de versiones (git):** repositorio local inicializado en `C:\JORGE\v3` con rama `main`. Configuración de identidad git (`user.name = geoidegeoidal`, `user.email = geoidegeoidal@users.noreply.github.com` solo si no existía previamente).
  - **`.gitignore`** creado: excluye el Excel bruto `gi-sinader-2024-ckan (1) (1).xlsx` (43 MB, no necesario para la web publicada y conservado solo en local) con `Thumbs.db`, `Desktop.ini`, `.DS_Store`, `*.log`.
  - **README.md** creado: portada de presentación del proyecto (qué ofrece el visor, cómo usarlo, datos, tecnologías, despliegue).
  - **Repositorio remoto:** `humedales_version3` (público) en la cuenta `geoidegeoidal` vía `gh repo create`. Commit inicial `5e0e54a` ("Mapa inicial: visor WebGIS de Humedales Urbanos y SINADER de Chile") con 9 archivos (3.984 líneas) y `push` a `origin/main`.
  - **GitHub Pages activado desde CLI** (`gh api repos/geoidegeoidal/humedales_version3/pages -X POST`, source branch `main`, path `/`, build legacy): URL pública asignada `https://geoidegeoidal.github.io/humedales_version3/`. Build compilado correctamente (`status: built`).
  - **Verificación en vivo:** respuestas HTTP `200` para la página principal, `humedales_data.js` y `sinader_data.js`.
  - La cuenta `geoidegeoidal` ya estaba autenticada con `gh` (keyring, protocolo https, scopes 'gist','read:org','repo','workflow'); no se requirió `gh auth login` interactivo.
- **Flujo de actualización futura:** cada cambio se publica con `git add -A && git commit -m "..."` + `git push`; GitHub Pages se reconstruye automáticamente.
