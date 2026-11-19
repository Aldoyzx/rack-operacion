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

## Dependencias

Ninguna instalación. Carga desde CDN, solo cuando hace falta:
- Fuentes Inter y JetBrains Mono (Google Fonts).
- `xlsx` 0.18.5 (cdnjs) para leer archivos de Excel.
