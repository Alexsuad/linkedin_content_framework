<!-- File: docs/governance/brief_sufficiency_gate.md -->

# Gate de suficiencia del brief

## Propósito
Determinar si la información de entrada contenida en una señal editorial individual es suficiente para generar una publicación útil, clara y segura. El brief es suficiente cuando permite evaluar la veracidad, valor de la información, trazabilidad de la señal y coherencia con el perfil editorial.

Este gate funciona como un filtro de calidad previo a la redacción. Su objetivo es impedir que el sistema de generación de contenido (ya sean redactores humanos o agentes de IA) avance a partir de señales débiles, ambiguas, incompletas o inventadas que puedan degradar la autoridad de la marca o generar incoherencias.

---

## 1. Qué evalúa
El gate somete la señal de entrada a una revisión sistemática en las siguientes áreas críticas:
-   **Problema real:** Identificación de un fallo, ineficiencia o fricción, aprendizaje, postura, historia o experiencia profesional verificable.
-   **Audiencia:** Claridad sobre quién sufre ese problema y cuál es su nivel de relación con el tema (si aplica).
-   **Contexto:** Circunstancias y escenario práctico donde ocurre la fricción.
-   **Fuente:** Origen trazable de la información dentro de la actividad, experiencia, contexto o intención comunicativa del perfil.
-   **Evidencia:** Datos de soporte, testimonios anonimizados, capturas u observaciones del perfil, actividad o contexto que sustenten el hecho.
-   **Riesgo:** Potencial vulneración de la confidencialidad del cliente o la reputación de la marca.
-   **Objetivo:** Qué se pretende que la audiencia aprenda, reconozca o realice a partir de esta publicación.
-   **Formato sugerido:** Adecuación lógica entre el tema y la estructura de comunicación seleccionada.

---

## 2. Entradas requeridas
Para realizar la evaluación, el gate requiere la consolidación y cruce de datos de los siguientes documentos base:
*   [client_intake_template.md](file:///home/nalex/Proyectos/linkedin_content_framework/docs/templates/client_intake_template.md) (Propuesta de valor, audiencia objetivo y temas prohibidos).
*   [voice_and_narrative_template.md](file:///home/nalex/Proyectos/linkedin_content_framework/docs/templates/voice_and_narrative_template.md) (Límites en el tono y arquetipos prohibidos).
*   [weekly_content_intake_template.md](file:///home/nalex/Proyectos/linkedin_content_framework/docs/templates/weekly_content_intake_template.md) (Planificación y prioridades de la semana de trabajo).
*   [input_signal_template.md](file:///home/nalex/Proyectos/linkedin_content_framework/docs/templates/input_signal_template.md) (La ficha estructurada de la señal individual con la fricción e impacto).

---

## 3. Preguntas de validación
El auditor (agente o humano) debe responder a los siguientes checks objetivos sobre la señal evaluada:
*   ¿El problema u observación de partida está descrito de forma clara y sin ambigüedades?
*   ¿Sabemos con precisión quién (qué rol o perfil profesional) vive ese problema?
*   ¿La señal proviene de una fuente o evento real, experiencia, aprendizaje o postura del emisor y no de una idea abstracta o teórica del LLM?
*   ¿Existe suficiente contexto operativo detallado para redactar el post sin necesidad de inventar diálogos, datos o soluciones?
*   ¿El impacto de la fricción (tiempo perdido, sobrecostes, frustración) está explicado de forma realista y sin exagerar?
*   ¿Se respeta la confidencialidad de clientes y proyectos según las políticas estratégicas?
*   ¿El formato sugerido (Tipo 1, 2 o 3) tiene sentido lógico con la complejidad de la explicación?

---

## 4. Estados posibles
Tras la evaluación, el gate clasificará la señal en uno de los siguientes estados:

*   `READY_TO_DRAFT`: La señal cumple todos los requisitos de completitud y veracidad y es declarada apta para iniciar la fase de redacción del borrador.
*   `NEEDS_CLARIFICATION`: La señal contiene una buena idea o hecho real, pero carece de detalles críticos sobre el contexto, la solución práctica o el impacto. Se devuelve al especialista.
*   `BLOCKED_BY_BRIEF`: Faltan datos esenciales de la fricción o no hay coherencia entre la señal y la planificación estratégica de la cuenta. El avance queda congelado.
*   `DISCARDED_NOT_USEFUL`: La idea es genérica, no aporta valor real al posicionamiento, carece de anclaje operativo verídico o trata temas prohibidos. La señal se archiva y se cancela su proceso.

---

## 5. Cuándo escalar al Especialista de Intake y Acompañamiento del Cliente
La señal debe ser escalada de forma obligatoria al Especialista de Intake ante los siguientes escenarios:
-   Cuando la información provista originalmente por el responsable del perfil / emisor en el intake semanal sea escueta o incoherente.
-   Cuando existan contradicciones entre la solución técnica planteada y el manual de posicionamiento de la marca.
-   Cuando falte el contexto necesario para redactar la pieza de manera honesta y natural.
-   Cuando el problema descrito sea tan genérico que obligue al redactor a rellenar el texto con buzzwords o frases vacías.
-   Cuando la señal trate un tema etiquetado como sensible o de alto riesgo reputacional.
-   Cuando no se proporcione ninguna fuente real ni evidencia de soporte que justifique la veracidad de la situación.

---

## 6. Salida del gate
El reporte de salida generado por este gate debe incluir de forma estructurada:
*   **estado:** [READY_TO_DRAFT, NEEDS_CLARIFICATION, BLOCKED_BY_BRIEF o DISCARDED_NOT_USEFUL]
*   **motivo:** [Justificación breve y objetiva del estado asignado]
*   **campos_faltantes:** [Lista de campos de la señal de entrada vacíos o insuficientes, si aplica]
*   **preguntas_de_aclaracion:** [Preguntas específicas y dirigidas a resolver la falta de información con el responsable del perfil / emisor]
*   **recomendacion:** [Sugerencia operativa para la corrección o rediseño de la señal]

---

## 7. Criterio de cierre
Una señal se considera formalmente aprobada y su gate cerrado para pasar a redacción cuando:
1.  Se haya emitido una salida del gate con el estado `READY_TO_DRAFT`.
2.  No existan advertencias de bloqueos o riesgos de confidencialidad pendientes.
3.  La traza de auditoría de este gate se almacene correctamente en el historial operativo de la señal.
Queda terminantemente prohibido iniciar borradores de post a partir de briefs que se encuentren en estado bloqueado o pendiente de aclaración.
