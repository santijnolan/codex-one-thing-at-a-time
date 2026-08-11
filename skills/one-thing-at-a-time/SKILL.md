---
name: one-thing-at-a-time
description: "Turn complex or ambiguous work into an ADHD-friendly planning sequence: investigate first, present exactly one consequential plan decision at a time in plain language, record explicit approvals, close the complete agreed plan, and then execute and verify all approved work autonomously. Use when the user asks to approve a plan item by item, plan 'one thing at a time' or 'de a una', avoid an overwhelming full plan, understand causes and consequences before agreeing, and have Codex carry out everything after the plan is settled."
---

# Una cosa a la vez

Reducir la carga mental durante la planificación sin fragmentar la ejecución. Investigar con autonomía, construir el plan mediante una sola decisión abierta por vez y, cuando quede cerrado, ejecutar todo lo aprobado sin nuevas interrupciones rutinarias.

Usar el idioma y el nivel técnico del usuario.

## Contrato central

- Mantener exactamente **una decisión sustantiva abierta** por turno del usuario.
- Hacer primero toda investigación segura y pertinente. No pedirle al usuario datos que puedan encontrarse en archivos, herramientas, estado actual o fuentes conectadas.
- Preguntar únicamente por elecciones que cambien resultados, alcance, costo, riesgo, privacidad, destinatarios o comportamiento. Resolver los detalles normales de implementación con autonomía.
- No tratar silencio, entusiasmo general, “puede ser”, “creo que sí” ni una pregunta como aprobación.
- No avanzar a otra decisión mientras la actual siga dudosa. Explicar, simplificar, investigar o reformular la misma decisión hasta que quede aprobada, descartada o pospuesta.
- Respetar literalmente la versión aprobada. Cualquier cambio material posterior vuelve como una decisión nueva.
- No pedir una segunda aprobación global de elementos ya aprobados uno por uno, salvo que la integración cambie sus efectos.
- No implementar cada medida al aprobarla. Mantener separadas la fase de planificación y la fase de ejecución.
- Al cerrar el plan, ejecutar todo lo aprobado con autonomía si el usuario pidió resolver o implementar la tarea. No pedir permiso por cada acción técnica.

## Flujo

### 1. Entender antes de preguntar

1. Inferir el objetivo, las restricciones y si el usuario pidió sólo el plan o que, una vez acordado, también se ejecute.
2. Inspeccionar el estado real antes de formular medidas.
3. Separar:
   - defectos comprobados;
   - incertidumbres que pueden investigarse;
   - ideas opcionales;
   - detalles técnicos que Codex debe resolver solo.
4. Mantener internamente una cola tentativa de decisiones, pero mostrar únicamente la siguiente. Reordenarla cuando aparezca evidencia nueva.

No presentar como mejora algo que ya funciona. Si no se puede confirmar el defecto, investigar primero o identificar honestamente la propuesta como exploratoria.

### 2. Mantener un registro durable

Para trabajo largo o de varias decisiones, crear o actualizar un registro breve en la superficie privada ya establecida para el proyecto. Preferir una carpeta de decisiones, especificación existente, issue o documento operativo ya usado. Si no hay una convención apropiada, mantener el registro en el plan de la tarea hasta que haga falta persistirlo. No crear un sistema externo nuevo sólo para registrar el plan.

Guardar por decisión:

- número y título;
- problema y evidencia actuales;
- versión exacta propuesta;
- estado: `en discusión`, `aprobada`, `descartada`, `pospuesta`, `implementada` o `verificada`;
- condiciones y correcciones del usuario;
- resultado y evidencia de ejecución.

Actualizar el registro al cambiar el estado y leerlo de vuelta cuando la persistencia sea importante. Nunca perder una condición agregada por el usuario.

### 3. Presentar una tarjeta de decisión

Usar una tarjeta corta y concreta. Incluir sólo campos que aporten valor, normalmente:

```markdown
### Decisión 3 — Corregir <problema concreto>

**Problema hoy:** <qué falla y evidencia breve>

**Cambio:** <una sola medida, en lenguaje simple>

**Si la aprobás:** <consecuencia principal>
**Si no:** <qué problema o alternativa queda>
**Riesgo:** <tradeoff más importante y mitigación>

**Mi recomendación:** Aprobar / ajustar / descartar, porque <motivo honesto>.

¿La aprobás, la ajustamos o la descartamos?
```

Agregar como máximo uno o dos ejemplos concretos cuando vuelvan obvia la diferencia. Evitar tablas, puntajes y taxonomías salvo que realmente simplifiquen la decisión.

Para que responder sea liviano:

- ofrecer tres respuestas naturales: `Aprobar`, `Ajustar` o `Descartar`;
- si existe una herramienta de opciones, usarla con una sola pregunta y poner primero la recomendación;
- aceptar respuestas libres y breves;
- mostrar progreso compacto, por ejemplo `3 aprobadas · 2 por decidir`, sin infantilizar ni gamificar decisiones sensibles.

### 4. Quedarse en la misma decisión

Interpretar la respuesta así:

- **Aprobación clara:** registrar la formulación exacta y sus condiciones.
- **Aprobación condicionada:** repetir en una frase la condición incorporada y pedir confirmación sólo si cambia materialmente el resultado.
- **Duda o pregunta:** responder directamente y, si es verificable, buscar evidencia. No pasar a la siguiente medida.
- **“Explicalo más fácil”:** reducirlo a problema, cambio y un ejemplo. No introducir nuevas decisiones.
- **“¿Vos qué harías?”:** dar una recomendación sincera y una duda real si existe; no refugiarse en neutralidad artificial.
- **Rechazo:** registrar el motivo. Si el motivo revela una formulación mejor, ofrecer una versión corregida como la misma decisión, no como otra medida.
- **Posponer:** anotarla como pendiente y continuar sólo si el usuario lo pide.

Usar niveles de certeza sólo cuando ayuden. No inventar precisión numérica; explicar qué está probado y qué sigue incierto.

### 5. Cerrar el plan antes de ejecutar

Continuar decisión por decisión hasta que:

- no queden medidas sustantivas en discusión;
- estén resueltos alcance, prioridades, riesgos y consecuencias relevantes;
- esté claro qué significa terminar y cómo se verificará;
- las ideas restantes tengan rendimientos decrecientes o no estén respaldadas por evidencia.

Registrar entonces el plan como `cerrado`. Mostrar un resumen compacto de lo aprobado, descartado y pospuesto para que el usuario conserve el mapa, pero no pedir que vuelva a aprobar lo mismo.

No implementar durante esta fase. Si el usuario pide empezar antes de cerrar el plan, tratar el cambio de secuencia como la única decisión abierta.

### 6. Ejecutar todo el plan aprobado

Si el usuario pidió resolver, cambiar, construir o implementar la tarea, comenzar inmediatamente después de cerrar el plan. La aprobación individual de todas las medidas constituye la conformidad con el alcance completo; no pedir un “¿arranco?” redundante.

Durante la ejecución:

- ejecutar todo el alcance aprobado con autonomía;
- ordenar, agrupar o paralelizar acciones técnicas según dependencias y riesgo;
- resolver fallas rutinarias dentro del alcance sin molestar al usuario;
- no detenerse después de cada medida para pedir otra aprobación;
- volver al usuario sólo si aparece una consecuencia material no contemplada, una decisión nueva, un bloqueo real o una autorización que el plan no podía conceder;
- no sumar funciones “útiles” no aprobadas;
- mantener rollback o reversibilidad cuando corresponda;
- verificar componentes críticos y luego el resultado integrado;
- registrar `implementada` y `verificada` sólo con evidencia real;
- distinguir claramente `aprobado`, `implementado`, `probado`, `activo` y `verificado en uso real`.

La aprobación del plan no amplía permisos ni reemplaza límites superiores sobre envíos, producción, dinero, credenciales, privacidad o acciones irreversibles.

### 7. Cerrar en el momento correcto

Detener nuevas propuestas cuando el siguiente cambio tenga rendimiento claramente decreciente o carezca de evidencia. Decirlo con honestidad.

Al cerrar, resumir de forma compacta:

- qué quedó aprobado y descartado;
- qué se implementó y verificó;
- qué sigue pendiente o requiere evidencia natural;
- cuál es la siguiente acción concreta, si existe.

Si el usuario pidió sólo planificación, detenerse con el plan cerrado. Si pidió plan más ejecución, terminar el trabajo completo antes de devolver el cierre final.

## Guardas contra sobrecarga

- No descargar el plan completo “para contexto” salvo pedido explícito.
- No agrupar decisiones independientes en una pregunta.
- No hacer preguntas operativas que Codex pueda resolver solo.
- No implementar medidas mientras todavía se está construyendo el plan.
- No convertir la ejecución posterior en otra ronda de aprobaciones paso a paso.
- No responder una objeción presentando inmediatamente la medida siguiente.
- No esconder costos, efectos secundarios ni incertidumbre para conseguir aprobación.
- No complicar una regla humana con tablas o fórmulas si una pregunta simple representa mejor el criterio.
- No resolver un problema de calidad reduciendo silenciosamente cantidad, cobertura o utilidad; preservar el objetivo declarado y explicar el intercambio.
- No confundir “no corresponde ahora” con “no sirve”: distinguir hacer ahora, conservar para después y descartar cuando esa separación sea relevante.

## Ejemplo mínimo

```markdown
### Decisión 2 — Guardar los hallazgos útiles que no requieren acción inmediata

**Problema hoy:** al rechazar una alerta, también desaparece información útil para el informe semanal.

**Cambio:** permitir “guardar para el informe” como destino separado de “avisar ahora” y “descartar”.

**Si la aprobás:** se conserva valor sin sumar notificaciones.
**Riesgo:** puede crecer el borrador; se controla quitando duplicados antes de revisión.

**Mi recomendación:** aprobar. Corrige una pérdida comprobada sin endurecer el filtro.

¿La aprobás, la ajustamos o la descartamos?
```
