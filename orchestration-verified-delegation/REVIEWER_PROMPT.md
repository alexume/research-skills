# Plantilla · Revisión externa de un prompt delegado

Usar esta plantilla **solo en `VERIFICACIÓN_COMPLETA`**, cuando se active alguno
de los criterios de revisión externa de `SKILL.md`. No usarla para tareas
`DIRECTO` ni de `DELEGACIÓN_LIGERA`.

Se entrega **idéntica** a cada revisor, en proveedores distintos. No se le dan
pistas a ninguno sobre dónde mirar: si se las das, la divergencia entre revisores
deja de medir a los modelos y mide tus pistas.

Rellena las dos rutas y pégalo tal cual.

---

Vas a revisar un prompt de tarea delegada **antes de que se lance**. No lo
escribiste tú, y ahí está tu valor: quien lo escribió no puede ver sus propios
huecos.

```
PROMPT A REVISAR:  <<ruta del fichero>>
REPOSITORIO:       <<raíz del repositorio>>
```

**No modifiques ningún fichero. No cargues datos pesados. No ejecutes el prompt.**
Lees, verificas y dictaminas.

## Lo que tienes que hacer

**1 · Verifica cada cita al repositorio, abriendo el fichero.** El prompt afirma
cosas sobre el código: números de línea, nombres de columna, valores de
vocabularios, rutas, esquemas. **Compruébalas una a una.** Una cita recordada y no
verificada es el fallo más frecuente y el más silencioso: el agente la ejecutará
como si fuera cierta.

Reporta las que **no** coinciden, con lo que dice el prompt y lo que dice el
código.

**2 · Busca el modo de fallo silencioso.** La pregunta que gobierna la revisión:

> **¿Puede este resultado salir bien por la razón equivocada?**

Un resultado excelente y vacío es peor que uno malo, porque nadie lo mira. Piensa
en circularidad, en fuentes compartidas entre los dos lados de una comparación, en
factores que se cancelan algebraicamente de la métrica, en estratos que salen
planos por construcción, en comparaciones donde el incumbente juega dentro de
muestra.

**Deriva el álgebra si la tarea calcula una métrica.** No des por bueno que mide
lo que dice medir.

**3 · Comprueba que los árbitros son aserciones y no prosa.** «Comprueba que…» no
es un árbitro; `stop()` sí. Un árbitro que no puede fallar no es un árbitro.

**4 · Busca prohibiciones con excepción.** Si el prompt dice «no hagas X» y más
abajo pide algo que exige X, el modelo cruzará por ahí y tendrá razón.

**5 · Comprueba la coherencia interna.** Definiciones usadas de dos maneras
distintas en dos párrafos, rangos que contradicen la definición que los precede,
unidades mezcladas, contratos de salida con comodines donde la existencia en disco
es árbitro.

**6 · Comprueba que no contradice los documentos canónicos** del repositorio
—reglas, plan de trabajo, decisiones firmadas—. Si el prompt y una decisión
firmada discrepan, **dilo**: puede que el error esté en el documento y no en el
prompt.

**7 · Viabilidad.** Mide los recursos que la tarea va a necesitar y compáralos con
los disponibles. Si no cabe, dilo con cifras y propón **recortes que no cambien lo
que se mide**, ordenados.

## Cómo entregarlo

- **Un dictamen primero**: ¿lanzable hoy, sí o no?
- Luego los bloqueos, **ordenados por gravedad**, cada uno con: qué dice el
  prompt, qué dice el repositorio o el razonamiento, y qué escribirías en su
  lugar.
- Después lo menor.
- Y al final, **qué está bien y conviene no tocar**. Un revisor que solo enumera
  fallos deja al autor sin saber qué conservar.

**Cita fichero y línea en cada punto.** Una objeción sin localizador no se puede
adjudicar.

**Si crees que el prompt es correcto, dilo.** No inventes objeciones para
justificar la revisión.
