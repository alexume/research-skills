---
name: orchestration-verified-delegation
description: "Delegar tareas de investigación con control proporcional al riesgo. Distingue ejecución directa, delegación ligera y verificación completa; prepara encargos concretos para agentes baratos, revisa sus artefactos contra el repositorio y reserva árbitros, revisión externa y trazabilidad extensa para resultados frágiles o citables. Invócala al delegar, orquestar, revisar prompts o informes, gestionar una cola o handoff, o decidir cuánto control necesita una tarea."
---

# Delegación verificable y proporcional

Método para usar agentes sin convertir la orquestación en el producto. El control
debe ser proporcional al daño que puede causar un error silencioso.

> **Una cifra sin fichero es una afirmación, no un resultado.**

> **Verificar contra el repositorio, no contra el informe del agente.**

## 1. Separar papel y nivel

Tomar dos decisiones distintas antes de actuar:

1. **Papel:** `ORQUESTAR` una tarea o `REVISAR` un prompt/resultado ajeno.
2. **Nivel:** `DIRECTO`, `DELEGACIÓN_LIGERA` o `VERIFICACIÓN_COMPLETA`.

No inferir el nivel por el nombre del proyecto ni por la existencia de una cola.
Elegir el nivel más bajo que cubra un riesgo concreto y decir en una frase por qué.

| Nivel | Cuándo | Coste documental |
|---|---|---|
| **DIRECTO** | Tarea corta, reversible, acotada y más barata de ejecutar que de delegar | Ningún prompt, handoff, manifiesto o log nuevo por defecto |
| **DELEGACIÓN_LIGERA** | Ejecución mecánica y acotada que un agente barato puede hacer con entradas y salidas claras | Encargo breve, 2–5 controles ligados a riesgos reales y revisión de artefactos |
| **VERIFICACIÓN_COMPLETA** | Puede salir bien por una razón equivocada, produce evidencia citable o es cara de repetir | Ciclo completo, árbitros, revisión independiente cuando corresponda y cierre trazable |

**Regla económica:** delegar solo si el coste de especificar y comprobar es menor
que el de ejecutar directamente.

### Supervisión de hitos

La revisión global se realiza al cerrar un hito, cambiar un contrato entre etapas
o encontrar contradicciones que afecten a varias tareas. No se exige para cada
encargo. Comprobar que entradas, transformaciones, salidas y usos analíticos
siguen siendo coherentes. El proyecto asigna los modelos concretos para la
coordinación cotidiana, la ejecución y esta supervisión.

Cada tarea delegada recibe una revisión proporcional inmediata antes de que su
salida alimente otra tarea. La verificación completa global se reserva para el
cierre del hito; una tarea intermedia la recibe antes de ser consumida solo si
cambia población, medición o comparabilidad, produce evidencia citable o presenta
un riesgo material de fallo silencioso. El cierre global no sustituye la revisión
local, y la revisión local no obliga a repetir el ciclo completo.

### Ejemplos de triaje

- Guardar una tabla desde una URL oficial ya identificada, en una adquisición
  puntual: `DIRECTO`; conservar el fichero y una nota mínima de fuente y fecha,
  sin crear un script por defecto.
- Automatizar una adquisición recurrente, una API o varias descargas coordinadas:
  `DELEGACIÓN_LIGERA` si delegar aporta valor.
- Extraer columnas, hacer `distinct()` y escribir un inventario:
  `DELEGACIÓN_LIGERA`.
- Corregir una ruta o un nombre ya diagnosticado: `DIRECTO`.
- Decidir si dos categorías históricas son conceptualmente agregables:
  decisión de autor o modelo fuerte; no delegarla como operación mecánica.
- Validar identidades aritméticas que retroalimentarán extracción o producir una
  medida publicada: `VERIFICACIÓN_COMPLETA`.

Escalar un nivel si aparece dependencia circular, clasificación ambigua sin
válvula, comparación entre derivados de la misma fuente, alto coste de
reejecución o una cifra destinada a publicación.

## 2. Modo `DIRECTO`

Ejecutar con la skill sustantiva pertinente. Mantener únicamente la higiene del
repositorio: entradas explícitas, salidas explícitas, datos raw inmutables y
controles básicos dentro del script.

No crear por defecto:

- prompt de tarea;
- registro de árbitros;
- hashes o identificadores hash;
- manifiesto de objetos;
- doble ejecución;
- modos artificiales de ejecución;
- informe o handoff específico;
- commit separado por microtarea.

La reproducibilidad vive en el código y en los artefactos que la tarea necesita,
no en documentos paralelos.

## 3. Modo `DELEGACIÓN_LIGERA`

Usarlo para separar planificación/revisión costosa de ejecución barata sin pagar
el protocolo completo.

La existencia de una cola serializada no convierte una tarea en verificación
completa. Para delegación ligera, utilizar los cinco campos del encargo mínimo
y 2–5 controles. No heredar secciones adicionales salvo que cubran un riesgo
identificado.

### Encargo mínimo

Escribir en el chat o en un fichero solo si el proyecto ya usa una cola:

1. **Objetivo:** una transformación observable.
2. **Consume:** rutas o fuentes exactas.
3. **Produce:** script y salidas exactas.
4. **No hacer:** límites metodológicos y de alcance.
5. **Comprobar:** entre 2 y 5 condiciones que pueden fallar de verdad.

Añadir una válvula simple: si la fuente, el esquema o una categoría necesaria no
coincide con lo observado, parar y describir la discrepancia; no inventar.

No fabricar como prerrequisito un contrato que la tarea pretende descubrir. Si
el objetivo es inventariar un esquema desconocido, conservar nombres y valores
observados y elevar solo las ambigüedades; exigir una lista cerrada únicamente si
el autor ya la proporcionó.

### Controles apropiados

Preferir controles como:

- la fuente oficial y su URL quedan registradas;
- el raw no se modifica;
- las columnas requeridas existen;
- el resultado tiene la clave esperada sin duplicados;
- las filas no clasificables se conservan como incidencias;
- el script vuelve a producir la salida desde las entradas declaradas.

No exigir hashes, cuatro modos, dos rondas, quince checks, tripwire, árbitros
numerados o revisión de dos proveedores salvo que un riesgo específico los
justifique. No convertir precisión decimal, blancos o ceros en subsistemas si el
esquema observado no demuestra que sean un problema.

### Revisión ligera

Cuando el agente termine:

1. Abrir el script y las salidas, no aceptar solo su resumen.
2. Comprobar los 2–5 controles acordados.
3. Inspeccionar una muestra de filas y los conteos principales.
4. Confirmar que no escribió fuera del alcance.
5. Corregir o aceptar; actualizar la cola existente solo si ya existe.

No pedir una segunda ejecución idéntica como prueba de calidad. Reejecutar una
vez solo cuando haga falta demostrar reproducibilidad o tras una corrección.

## 4. Modo `VERIFICACIÓN_COMPLETA`

Aplicar el ciclo completo únicamente cuando lo exige el modo de fallo:

```
ESTADO      verificar disco y git
COLA        identificar tarea, dependencias y decisiones de autor
PROMPT      especificar alcance, salidas y árbitros falsables
REVISIÓN    externa cuando dispara §6
LANZAR      delegar y esperar el informe
VERIFICAR   comprobar contra código y artefactos
REGISTRAR   guardar cada hecho una sola vez
CERRAR      ejecutar aceptación pertinente y commitear cuando proceda
```

### Los cinco papeles

En proyectos que ya operan con protocolo completo, mapear por contenido:

| Papel | Contiene | No contiene |
|---|---|---|
| **Reglas** | decisiones canónicas y prohibiciones | estado diario |
| **Plan / cola** | estado de tareas, orden, dependencias y criterios de cierre | resultados detallados |
| **Handoff** | resumen vigente y punto de reentrada, con enlaces a la cola | cola o método duplicados |
| **Prompts** | un encargo por tarea delegada | resultados |
| **Cifras** | resultados citables y su procedencia | decisiones de autor |

No crear estos cinco papeles para habilitar una tarea ligera. Si ya existen,
actualizar solo el papel que realmente cambia. Un hecho tiene un sitio; en los
demás se usa un puntero.

La cola contiene estado, dependencias y criterio de cierre; el handoff resume el
punto de reentrada y enlaza la cola; las decisiones sustantivas viven en su
registro canónico. Separar el diagnóstico histórico del estado vigente.

Antes de preparar un encargo, consultar las decisiones y mappings que gobiernan
la tarea. Reabrir una decisión solo ante evidencia nueva o contradicción concreta,
indicando qué la pone en cuestión; cualquier enmienda sustantiva sigue §8.
Consultar lo pertinente, sin releer toda la documentación en cada turno.

Si falta la ruta del proyecto o hay varios subproyectos con sus propios papeles,
identificar primero la unidad de trabajo. Si el proyecto aún no sabe qué etapa o
producto necesita, usar `orchestration-research-workflow`; esta skill empieza
cuando existe una tarea concreta.

### Prompt completo

Usar las ocho partes solo en este nivel:

1. Estado inicial relevante; incluir `pwd`/HEAD solo si hay riesgo de árbol o
   rama equivocados.
2. Qué se mide y qué no.
3. Modo de fallo silencioso.
4. Reglas duras y decisiones reservadas.
5. Script y salidas exactas.
6. Pasos analíticos y su finalidad.
7. Árbitros falsables ligados a riesgos.
8. Qué no hacer y contrato del informe final.

Un árbitro debe poder fallar la tarea. No usar “comprueba que…” como sustituto de
una aserción ejecutable. No inventar umbrales sin fundamento sustantivo.

El troceado por modos, los presupuestos de memoria y los resultados parciales se
añaden solo si la escala computacional lo requiere. Una tarea pequeña debe poder
ejecutarse de principio a fin con una llamada normal.

## 5. Fallos silenciosos que obligan a escalar

Buscar especialmente:

| Fallo | Diagnóstico mínimo |
|---|---|
| **Fuente compartida** | comprobar si los dos lados descienden del mismo dato |
| **Cancelación algebraica** | derivar la métrica antes de interpretarla |
| **Evaluación dentro de muestra** | separar construcción y evaluación |
| **Eje sin poder discriminante** | medir cobertura y variación |
| **Denominador mixto** | declarar numerador, denominador y universo |
| **Categoría forzada** | conservar una salida `unmapped`/`unclassified` |
| **Prosa obsoleta** | contrastar narrativa con tablas generadas |
| **Estrato ausente** | mostrarlo con causa, no eliminarlo silenciosamente |

## 6. Revisión externa

Exigir revisión independiente cuando se cumpla cualquiera de estas condiciones:

1. Una medida central puede validarse aparentemente por dependencia entre sus
   entradas o referencias.
2. Una decisión de medición cambia sustancialmente población, comparabilidad o
   interpretación.
3. El resultado va a sostener una afirmación central en un documento firmado.
4. Un fallo silencioso sería materialmente costoso de detectar o reparar.

Una correlación exploratoria, una tabla descriptiva o una figura no requieren
revisión independiente por su tipo de operación. Aplicar el nivel de control
correspondiente a su uso y riesgo.

Extracción, conteo, descarga desde fuente ya resuelta y clasificación contra lista
cerrada con válvula tampoco la requieren por defecto; comprobar si su uso activa
alguna de las condiciones anteriores. Una descarga puntual ya resuelta puede ser
`DIRECTO`; si se delega una ejecución mecánica, basta la revisión ligera.

Al revisar un prompt, abrir las citas al repositorio, buscar modos de fallo
silenciosos, comprobar que las restricciones son coherentes y verificar que la
escala es viable. Al revisar un resultado, reproducir cifras desde los ficheros,
examinar el código y confirmar que incidencias y estratos vacíos no desaparecen.

Dos proveedores independientes pueden aportar valor en resultados realmente
frágiles. No convertirlos en requisito rutinario. Cuando se justifique esa doble
revisión, entregar a ambos revisores las mismas instrucciones: de
[`REVIEWER_PROMPT.md`](REVIEWER_PROMPT.md) para revisar un prompt y de
[`COLD_VERIFIER.md`](COLD_VERIFIER.md) para verificar en frío un resultado
entregado.

## 7. Ejecución y cierre

En `VERIFICACIÓN_COMPLETA`, quien orquesta no ejecuta la parte sustantiva que
después debe verificar. En `DIRECTO` sí ejecuta. En `DELEGACIÓN_LIGERA` puede
preparar el encargo y revisar personalmente el artefacto sencillo.

Mientras corre una tarea larga, observar solo señales de salud. No interpretar
salidas transitorias. Evitar agentes concurrentes que escriban el mismo fichero.

### Fallos y reintentos

Antes de repetir un encargo fallido, clasificar la causa: especificación
defectuosa, ejecución incorrecta, entorno, fuente insuficiente o decisión
metodológica pendiente. Corregir la especificación cuando corresponda.

Tras dos intentos fallidos por la misma causa, revisar el diagnóstico y el reparto
de trabajo antes de lanzar un tercero. No aumentar controles ni cambiar de modelo
automáticamente. Esta revisión no exige un nuevo registro ni aprobación para
correcciones ya autorizadas.

### Cierre de correcciones

Una corrección queda cerrada cuando se actualizan el artefacto afectado y sus
consumidores inmediatos necesarios para el hito. Registrar la corrección en el
handoff no sustituye esa actualización.

Si un consumidor no se regenera todavía, marcarlo explícitamente como
desactualizado y conservar la tarea pendiente en la cola existente. No
presentarlo como resultado vigente. Actualizar consumidores dentro del alcance
autorizado; si quedan fuera, declarar la dependencia pendiente sin ampliar el
encargo por cuenta propia.

Cerrar de forma proporcional:

- **DIRECTO:** salida comprobada y resumen breve.
- **DELEGACIÓN_LIGERA:** artefactos revisados, controles básicos y cola existente
  actualizada si corresponde.
- **VERIFICACIÓN_COMPLETA:** árbitros comprobados contra disco, cifras trazables,
  suite pertinente en verde y commit intencional si el flujo del proyecto lo
  requiere.

No crear commits, logs o documentación solo para demostrar que la skill se usó.
Si el proyecto ya mantiene un registro de skills, añadir una sola entrada; no
crear el registro para una tarea ligera.

## 8. Decisiones de autor

La skill no decide qué categoría histórica es canónica, qué variables se pueden
agregar ni qué resultado se publica. Separar la ejecución mecánica de esas
decisiones. Registrar una decisión solo cuando el autor la toma, con razón,
fecha, alcance y lo que no promete.
