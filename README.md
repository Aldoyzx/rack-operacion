# Rack · Operación

Herramienta personal para la zona de rack de un almacén: recibo y slotting, mapa de calor por posición, reportes operativos, seguridad del rack (daños e inspecciones), revisión diaria de ubicaciones, rotación ABC/XYZ, vencimientos FEFO y bitácora de auditoría con huella SHA-256.

Es **un solo archivo HTML**, sin servidor ni instalación.

## Cómo usarlo

1. Abre `index.html` en el navegador (escritorio o celular).
2. Entra con una cuenta de demostración o con **Usar con mis datos reales**.

### Cuentas de demostración

Contraseña de todas: `Rack2026!`

| Rol | Correo |
|---|---|
| Auxiliar | aquispe@almacen.demo |
| Jefe | lramos@almacen.demo |
| Analista | cvega@almacen.demo |
| Gerente | jsalas@almacen.demo |
| Administrador | admin@almacen.demo |

> Las cuentas demo son solo para validar: el código es visible, así que **no protegen datos reales**.

## Datos

- **Todos los datos de la demostración son ficticios** (almacén, SKU, proveedores, capacidades, daños e inspecciones).
- Con datos reales, el reporte del WMS se carga en la pestaña **Datos** (Excel, CSV o copiar y pegar).
- Lo que se guarda en el dispositivo (demo, inspecciones, revisión diaria) se puede **exportar e importar como respaldo JSON** desde **Datos → Respaldo**.
- Los datos de referencia de la industria (ISO 6780, GS1, WERC, ANSI MH16.1, guías de fabricantes) son **referencias generales, no datos de la operación**; con datos reales vienen apagados.

## Seguridad del rack

Las frecuencias de inspección y severidades toman como referencia ANSI MH16.1 (Estados Unidos). En Perú el marco general es la Ley 29783 de Seguridad y Salud en el Trabajo y su reglamento: confirmar con el área de SST y con el fabricante del rack.

## Navegación

- La cabecera (título, usuario, colores y tema) solo se ve al inicio; al bajar aparece una barra delgada con el botón **☰** y la vista actual.
- En celular y tablet las vistas están en el menú **☰ Menú**; en escritorio también como pestañas.
- El menú incluye quién entró, la leyenda de colores, el tema y **Salir**.

## Seguridad y normas

Una herramienta no se "certifica" en ISO: las normas se certifican en la organización. Lo que sí hace esta página es **aplicar los controles que le corresponden**, para que la operación pueda alinearse con ellas.

| Norma / guía | Qué aplica la página |
|---|---|
| **ISO/IEC 27001:2022** (Anexo A) | 5.15 / 5.18 control de acceso por rol (auxiliar, jefe, analista, gerente, admin) · 8.5 autenticación con PBKDF2-SHA256, bloqueo tras 5 intentos y cierre por 30 min de inactividad · 8.13 respaldo exportable con huella SHA-256 · 8.15 bitácora encadenada con SHA-256 y verificación · 8.24 criptografía estándar del navegador (Web Crypto) · 8.28 codificación segura (ver abajo) |
| **OWASP** (codificación segura) | Política de contenido (CSP) que solo permite el script propio y las fuentes/librerías declaradas · todo texto externo se escapa antes de mostrarse · celdas CSV que empiezan con `= + - @` se neutralizan (inyección CSV) · claves `__proto__`/`constructor` descartadas al importar · validación de tamaño y formato en cada carga |
| **Ley 29733** y su reglamento (D.S. 016-2024-JUS), Perú | Los datos quedan en el dispositivo o en la base del usuario; no se envían a terceros · la página no pide más datos personales que nombre y rol · `Referrer-Policy: no-referrer` |
| **ISO 45001** y **Ley 29783** (SST, Perú) | Reportes con severidad de daño, bloqueo automático de posiciones en rojo, inspecciones con recordatorio y evidencia fotográfica. Frecuencias de referencia: ANSI MH16.1; confirmar con SST y el fabricante del rack |
| **ISO 6780** | Medidas de parihuela de referencia (1200×1000, 1200×800, 48×40 in) para validar el hueco del rack |
| **WCAG 2.2 AA** (ISO/IEC 40500 es la versión 2.0) | Contraste en ambos temas, foco visible, controles de al menos 44 px en el menú, navegación con teclado (Esc cierra, el foco no sale del menú abierto), respeto de "reducir movimiento" |

### Límites conocidos

- Las cuentas de demostración son de **validación**: el código es visible, así que no protegen datos reales. Para un uso real con varias personas, el control de acceso debe estar en un servidor.
- La librería de Excel (`xlsx` 0.18.5, cdnjs) se carga sin integridad SRI; conviene agregarla tras verificar su huella.

### Si cambias el JavaScript

La CSP permite solo el script con la huella exacta. Después de editar `index.html`, ejecuta:

```bash
python3 tools/csp.py index.html
```

Si no, GitHub Pages bloquea el script y la página no arranca.

## Dependencias

Ninguna instalación. Carga desde CDN, solo cuando hace falta:
- Fuentes Inter y JetBrains Mono (Google Fonts).
- `xlsx` 0.18.5 (cdnjs) para leer archivos de Excel.
