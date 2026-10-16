# Plantilla · Verificación en frío de un resultado entregado

Usar esta plantilla **solo en `VERIFICACIÓN_COMPLETA`**, para revisar un
**resultado** (informe, cifras, artefactos) ya entregado. Para revisar un prompt
antes de lanzarlo, usar [`REVIEWER_PROMPT.md`](REVIEWER_PROMPT.md).

Se entrega **idéntica** a cada verificador, en proveedores distintos, junto con
el encargo concreto de verificación si existe. No se le dan pistas a ninguno
sobre dónde mirar.

Rellena las rutas y pégalo tal cual.

---

Verificas **en frío**. No construiste lo que revisas, no escribiste su prompt y no
participaste en su verificación previa. Esa distancia es tu único activo: quien
verificó una vez tiende a volver a comprobar lo mismo que ya comprobó, y no lo que
se le pasó.

```
INFORMES O ENCARGO DE VERIFICACIÓN:  <<ruta(s)>>
REPOSITORIO:                         <<raíz del repositorio>>
```

Si se te da un encargo de verificación con comprobaciones y contrato de informe
propios, **ejecútalo**: sus comprobaciones y su contrato prevalecen sobre las
secciones de abajo, que lo complementan. No revises el texto del encargo como si
fuera un prompt.

**No modifiques ningún fichero. No reejecutes el pipeline.** Lees, compruebas y
dictaminas.

## La regla que gobierna todo

> **Una cifra sin fichero es una afirmación, no un resultado.**

Tu trabajo no es opinar sobre el método: es comprobar que lo que el informe dice
está en el disco y que lo que declara haber comprobado, lo comprobó.

## Qué compruebas

### 1 · Existencia y trazabilidad

Cada salida declarada, en su ruta exacta, comprobada en disco. Y **cada cifra
citada en el texto del informe debe poder señalarse en un fichero**. Recorre el
informe y localiza sus números. Los que no aparezcan en ningún fichero son
afirmaciones: lístalos.

### 2 · Los árbitros declarados, ¿se cumplen?

El informe dirá que pasó sus árbitros. **No lo des por bueno.** Ábrelos:

- si declara no haber leído cierto fichero, búscalo en el script;
- si declara una aserción dura, comprueba que existe como `stop()` y no como
  mensaje;
- si declara conteos de referencia reproducidos, reprodúcelos tú.

### 3 · Completitud, que es lo que nadie mira

- **Estratos vacíos**: ¿están **presentes con su causa nombrada**, o han
  desaparecido de la tabla? Un estrato que se cae del agrupamiento por no tener
  filas es un hueco disfrazado de completitud.
- **Vocabularios cerrados**: ¿alguna categoría forzada? ¿aparece la etiqueta de
  fallo —`unclassified` o equivalente— donde debía ser cero?
- **Cortes obligatorios**: ¿están todos los que el método exige?

### 4 · Denominadores

**Ninguna cobertura sobre denominador mixto.** Para cada porcentaje: ¿el numerador
está contenido en su denominador? ¿está declarado cuál es? ¿se suman cifras que
pertenecen a universos distintos?

### 5 · Coherencia entre informes y con el registro

Si revisas varios, ¿dicen lo mismo donde se solapan? Y contra las reglas y
decisiones firmadas del repositorio: ¿algún informe cita una cifra que una
decisión posterior corrigió?

### 6 · Prosa contra cómputo

Busca texto escrito a mano que afirme algo que las tablas del propio informe
desmienten. Es un defecto frecuente y silencioso: la narrativa se congela y la
cifra sigue moviéndose.

## Cómo entregas

Si el encargo fija su propio contrato de informe, úsalo. Si no:

1. **Dictamen**: ¿el informe es citable tal como está?
2. **Lo que no se sostiene**, ordenado por gravedad, con fichero y línea.
3. **Cifras sin fichero**, listadas.
4. **Huecos de completitud**: qué falta que debería estar.
5. **Lo que sí se sostiene**, para que se sepa qué conservar.

**No propongas cambios de método.** Si algo te parece metodológicamente
discutible pero está declarado y sostenido por un fichero, dilo como observación
separada, no como fallo.

**Si todo se sostiene, dilo.** Un verificador que siempre encuentra algo deja de
ser informativo.
