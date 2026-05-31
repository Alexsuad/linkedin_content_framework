<!-- File: docs/governance/antigravity_task_protocol.md -->

# Protocolo de trabajo con Antigravity

## Propósito
Definir cómo deben solicitarse, ejecutarse y cerrarse las tareas realizadas con Antigravity dentro de este repositorio.

Antigravity no debe trabajar con instrucciones vagas ni ambiguas que puedan inducir a derivas conceptuales o cambios no controlados en el repositorio. Quedan expresamente prohibidas instrucciones del tipo:
- "mejora todo";
- "revisa todo el proyecto";
- "crea lo que falte";
- "optimiza la arquitectura completa";
- "continúa donde vamos" sin indicar fase, bloque y archivos autorizados.

---

## 1. Principio base

El desarrollo del framework se rige por la siguiente regla constitucional de gobernanza híbrida:

> **IA propone. Python verifica. Humano aprueba. Git registra.**

La aprobación humana es la última línea de defensa y control de calidad. No obstante, esta aprobación no debe convertirse en una sobrevalidación operativa que asfixie el flujo. Durante la fase de desarrollo y calibración inicial se permite y promueve un mayor nivel de revisión y ajuste manual para refinar los criterios, pero el diseño final del sistema debe tender hacia una auditoría agéntica interna automatizada y robusta, complementada por una aprobación humana compacta y de alto nivel.

---

## 2. Formato obligatorio de cada tarea para Antigravity

Toda nueva asignación de trabajo o instrucción dirigida al asistente Antigravity debe estructurarse obligatoriamente bajo los siguientes parámetros:

- **Objetivo:** Definición exacta de lo que se quiere lograr.
- **Fase del plan:** Identificación de la fase actual del plan de implementación en la que se encuadra la tarea.
- **Bloque de trabajo:** Bloque específico del cronograma al que pertenece.
- **Archivos a leer:** Lista cerrada de archivos necesarios como contexto de entrada.
- **Archivos autorizados para crear o modificar:** Lista estricta de rutas de archivos sobre las que se permite la escritura.
- **Archivos prohibidos:** Lista de rutas críticas del proyecto que no deben ser alteradas bajo ningún concepto en esta tarea.
- **Contexto permitido:** Límites de la información y fuentes de datos que pueden usarse (e.g. restringirse a las señales reales de entrada).
- **Restricciones explícitas:** Reglas especiales o de no avance aplicables a la tarea.
- **Salida esperada:** Descripción del entregable y de los entregables documentales o técnicos.
- **Comandos de verificación:** Comandos y scripts de auditoría obligatorios a ejecutar para validar el resultado.
- **Criterio de cierre:** Definición objetiva de cuándo se considera completada la tarea.
- **Indicación de no hacer commit:** Recordatorio explícito de que no se deben realizar confirmaciones en Git de forma autónoma.

---

## 3. Reglas de alcance

Para garantizar la estabilidad del repositorio y prevenir la degradación de la arquitectura pre-code, se establecen los siguientes límites operativos innegociables para Antigravity:

- **Secuencialidad:** Trabajar únicamente un bloque del plan de implementación por vez. No se permite solapar fases o bloques.
- **Cierre del bloque:** No avanzar al siguiente bloque sin haber validado y cerrado formalmente el actual.
- **Modificación estricta:** No crear ni modificar archivos que no hayan sido explícitamente autorizados en el formato de la tarea.
- **Aislamiento externo:** No tocar ni alterar el repositorio fuente heredado de automatización LinkedIn.
- **Especialización agéntica:** No diseñar ni crear agentes de IA antes de que la Fase 1 (Intake y Gobernanza) esté formalmente cerrada.
- **Dependencia lógica de skills:** No escribir ni proponer clases o funciones de skills de software sin haber mapeado previamente la matriz de responsabilidades funcionales.
- **Orden documental:** No diseñar workflows agénticos antes de completar y validar los documentos de control y templates base.
- **Control de herramientas:** No invocar ni configurar servidores o herramientas MCP sin una decisión de arquitectura explícitamente registrada y aprobada.
- **Aislamiento de APIs:** No conectar servicios externos ni APIs de publicación hasta que la fase técnica y de seguridad correspondiente sea aprobada por el usuario.
- **Control de Git:** No realizar commits ni pushes automáticos. Git es la traza soberana que el usuario aprueba de forma explícita.

---

## 4. Reglas para tareas documentales

Al redactar, ampliar o refinar la documentación del repositorio, Antigravity debe aplicar las siguientes directrices:

- **Higiene de Markdown:** Mantener un formato Markdown limpio, sin HTML complejo innecesario, consistente en el uso de títulos, listas y bloques de código.
- **Trazabilidad de archivo:** Incluir siempre al inicio del documento un comentario HTML indicando la ruta exacta del archivo (ej. `<!-- File: ruta/al/archivo.md -->`).
- **No redundancia conceptual:** Evitar repetir el marco conceptual, la visión general o la justificación metodológica en cada plantilla o documento específico. Cada archivo debe enfocarse exclusivamente en su propósito operativo.
- **Respeto a las sedes de información:** Si un dato o regla ya pertenece a un archivo específico (ej. la voz del perfil en `voice_and_style.md`), los demás documentos deben enlazar o hacer referencia a él en lugar de duplicar su contenido.
- **Pureza del Núcleo (Core):** No contaminar el núcleo metodológico general (`docs/core/`, `docs/architecture/` o `docs/governance/`) con terminología particularizada de logística, menciones a personas individuales (como Alex) o ritmos específicos de publicación semanal.
- **Niveles de abstracción:** Mantener clara la división entre el núcleo general, el canal de comunicación (LinkedIn), el caso de uso específico, el perfil editorial configurado y el sector industrial de aplicación.

---

## 5. Reglas para auditoría agéntica

Las auditorías que realicen los especialistas agénticos del framework sobre las piezas de contenido propuestas deben ser objetivas y estar estructuradas bajo criterios específicos de aceptación. Deben evaluar de forma independiente:

1. **Suficiencia de brief:** Verificar que el insumo crudo (señal de entrada) cuente con los datos necesarios de problema, fricción, solución e impacto antes de iniciar la redacción.
2. **Calidad editorial:** Comprobar la coherencia narrativa y que el texto no resulte genérico o impersonal.
3. **Voz y tono:** Garantizar la alineación exacta con el arquetipo de voz configurado para el perfil editorial.
4. **Audiencia:** Asegurar que el mensaje y el nivel técnico del post están dirigidos adecuadamente a la audiencia objetivo definida.
5. **Claims y reputación:** Validar que los datos, porcentajes o promesas de valor estén debidamente justificados y no impliquen riesgos legales o de marca.
6. **Formato LinkedIn:** Revisar la estructura de párrafos cortos, uso de espacios, hooks iniciales y llamadas a la acción típicas del canal.
7. **Riesgo visual:** Evaluar la disposición visual del post (longitud, saltos de línea, uso moderado de emojis y negritas) o la legibilidad de los slides si es un carrusel.
8. **Estado de publicación:** Asignar una traza clara sobre el ciclo de vida del borrador.

Para evitar retroalimentaciones vagas o comentarios de texto libre difíciles de procesar por el sistema, la auditoría debe clasificar obligatoriamente la pieza en uno de los siguientes estados estandarizados:

- `READY_TO_APPROVE`: La pieza cumple todos los criterios formales y de calidad y está lista para el gate de aprobación humana.
- `READY_TO_SCHEDULE`: Post aprobado por el humano y listo para programarse en el canal.
- `NEEDS_MINOR_EDIT`: Requiere pequeños ajustes visuales o de redacción que no alteran el fondo conceptual.
- `NEEDS_HUMAN_REVIEW`: Pieza de alta calidad pero que trata un tema sensible o al borde de la política de riesgos, requiriendo arbitraje humano directo.
- `BLOCKED_BY_BRIEF`: El insumo original carece de información de soporte suficiente para poder redactarse.
- `BLOCKED_BY_CLAIM_RISK`: Contiene declaraciones exageradas, falsas o datos confidenciales no publicables.
- `BLOCKED_BY_VISUAL_RISK`: Estructura visualmente rota, excesivo uso de emojis, negritas inapropiadas o formateo incompatible con LinkedIn.
- `BLOCKED_BY_BRAND_MISMATCH`: Desalineación grave con el tono, valores o la narrativa estratégica definida en la cuenta editorial.

---

## 6. Reglas para aprobación humana

El diseño del flujo operativo debe proteger la soberanía y el tiempo del aprobador humano:

- **Fase de calibración:** Durante el desarrollo inicial, la revisión humana constante y detallada es obligatoria para ajustar los prompts y las reglas del sistema.
- **Delegación progresiva:** El objetivo final del sistema es que el aprobador humano no tenga que intervenir en micro-decisiones de redacción o comprobaciones de formato que el sistema puede automatizar.
- **Aprobación compacta:** El sistema debe agrupar y preparar paquetes de aprobación limpios (borrador final, traza de origen, checks en verde de auditoría interna y justificación de claims).
- **Concentración en decisiones críticas:** La aprobación humana debe reservarse para el visto bueno final sobre el lote de publicación o para dirimir excepciones de riesgo etiquetadas como `NEEDS_HUMAN_REVIEW`.
- **Publicación controlada:** La automatización de la publicación solo podrá implementarse en fases posteriores, asegurando que existen gates técnicos infranqueables en el CLI que impidan la salida de contenido no firmado por el aprobador humano.

---

## 7. Verificación obligatoria antes de cerrar una tarea

Al finalizar el trabajo de una tarea y antes de devolver el control al usuario, Antigravity debe ejecutar y reportar un checklist de verificación final que incluya:

1. **Archivos creados o modificados:** Lista de rutas afectadas.
2. **Resumen de cambios:** Breve descripción técnica de los cambios realizados.
3. **Resultado de la auditoría local:** Ejecución del script `python3 tools/audit_precode_repo.py` en limpio.
4. **Resultado de Git:** Estado corto del control de versiones (`git status --short`).
5. **Confirmación de restricciones:** Declaración explícita de haber respetado los límites y archivos prohibidos de la tarea.
6. **Recomendación del siguiente paso:** Propuesta de la siguiente tarea lógica en el plan de implementación.

---

## 8. Plantilla breve de instrucción para Antigravity

Para solicitar un trabajo a Antigravity, el usuario o el script orquestador debe usar la siguiente plantilla estructurada:

```md
# Tarea: [Nombre de la Tarea]

- **Objetivo:** [Descripción del resultado final deseado]
- **Fase:** [Fase de docs/implementation_plan.md, ej. Fase 1]
- **Bloque:** [Bloque de trabajo, ej. Bloque 3]
- **Archivos a leer:**
  - [Identity Contract](docs/core/identity_contract.md)
  - [Input Signal Template](docs/templates/input_signal_template.md)
- **Archivos autorizados:**
  - [Ruta 3](docs/governance/file3.md)
- **Archivos prohibidos:**
  - [Ruta 4](docs/core/principles.md)
- **Restricciones:** [Indicar reglas de no avance, palabras prohibidas, etc.]
- **Salida esperada:** [Formato y contenido del entregable]
- **Verificación:** [Comando de auditoría o validación]
- **Commit:** No hacer commit. Presentar cambios y esperar confirmación del aprobador humano.
```
