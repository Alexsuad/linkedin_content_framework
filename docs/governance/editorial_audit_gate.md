<!-- File: docs/governance/editorial_audit_gate.md -->

# Gate de auditoría editorial

## Propósito
Evaluar si una publicación candidata estructurada bajo el contrato de salida es clara, útil, coherente con el perfil editorial de la cuenta y apta para ser presentada ante el aprobador humano o programada para su publicación en LinkedIn.

Este gate no pretende reemplazar la firma final y el criterio editorial estratégico del responsable humano. Su función es actuar como una auditoría interna automatizada y operativa que clasifique los borradores, limpie errores formales y asigne de forma precisa el nivel de preparación de cada pieza.

---

## 1. Qué evalúa
El gate realiza comprobaciones específicas en los siguientes aspectos de la redacción:
-   **Hook:** Eficacia y atractivo de las primeras líneas para detener el scroll del lector en el feed.
-   **Claridad:** Facilidad de lectura, uso de vocabulario comprensible y longitud adecuada de las oraciones.
-   **Utilidad:** Aporte de valor práctico o de aprendizaje real para la audiencia.
-   **Alineación con la audiencia:** Adaptación del nivel técnico y de las temáticas a los intereses del buyer persona objetivo.
-   **Voz y tono:** Cumplimiento riguroso del arquetipo verbal y consistencia de estilo sin desvíos.
-   **Estructura:** Desarrollo coherente del flujo lógico (Problema -> Fricción -> Solución -> Impacto).
-   **CTA (Llamada a la acción):** Claridad, naturalidad y ausencia de enfoques excesivamente comerciales.
-   **Potencial de conversación:** Capacidad del post para incentivar comentarios cualificados y debates.
-   **Lectura móvil:** Adecuación visual del espaciado y saltos de línea para pantallas de smartphones.
-   **Adecuación al formato:** Correspondencia entre el contenido y las reglas de diseño del Tipo de publicación elegido.

---

## 2. Criterios mínimos
Para que una publicación sea calificada positivamente, debe cumplir de forma estricta los siguientes checks editoriales:
-   Debe nacer inequívocamente de un problema o fricción operativa real del negocio, no de abstracciones o teorías.
-   Debe comprenderse con facilidad por perfiles de negocio, evitando jerga excesivamente especializada salvo que el perfil lo exija.
-   No debe sonar a texto corporativo genérico, impersonal o autogenerado por un LLM.
-   No debe abrir la publicación hablando de la tecnología o herramientas (ej. "nuestro script en Python..."), sino de la solución funcional o el problema de negocio.
-   Debe reforzar de manera explícita el posicionamiento del autor (ej. el profesional con experiencia de campo).
-   Debe cerrar con una llamada a la acción coherente y alineada con la estrategia comercial del canal.
-   Debe tener la capacidad de generar conversación y debate en el área de comentarios de LinkedIn.

---

## 3. Estados posibles
Tras la auditoría editorial, el borrador se catalogará en uno de los siguientes estados:

*   `READY_TO_APPROVE`: La publicación cumple todos los estándares de redacción, estilo y formato y se encuentra lista para el gate de firma humana.
*   `READY_TO_SCHEDULE`: Post firmado por el aprobador humano que ha superado todos los controles y está listo para programarse en el canal.
*   `NEEDS_MINOR_EDIT`: El contenido es sólido pero requiere correcciones menores (ej. faltas ortográficas, espaciado visual o ajuste de hooks) que el propio sistema puede corregir.
*   `NEEDS_HUMAN_REVIEW`: El post es formalmente correcto pero trata un tema estratégico límite o sensible, requiriendo revisión humana.
*   `BLOCKED_BY_BRAND_MISMATCH`: Desalineación grave con el tono de voz de la marca, uso de expresiones prohibidas o adopción de arquetipos excluidos (influencer de LinkedIn, gurú de ventas, IA genérica).
*   `BLOCKED_BY_FORMAT_RISK`: Inconsistencias visuales graves, falta de slides en carruseles o estructura de párrafos densa e ilegible para móviles.
*   `DISCARDED_NOT_USEFUL`: La calidad general de la redacción es deficiente o la idea central no aporta ningún valor estratégico a la cuenta.

---

## 4. Auditorías internas recomendadas
El sistema híbrido (agentes y scripts) ejecutará de forma secuencial las siguientes comprobaciones específicas:
1.  **Auditoría de claridad:** Análisis de longitud de frases, legibilidad de párrafos y uso de conectores naturales.
2.  **Auditoría de voz:** Comparación semántica del texto contra los términos preferidos y las buzzwords prohibidas de la marca.
3.  **Auditoría de audiencia:** Comprobación de que el lenguaje está nivelado con la madurez técnica del buyer persona definido.
4.  **Auditoría de formato LinkedIn:** Validación visual del formateo (sin bloques densos de texto, hooks limpios de emojis y llamadas a la acción directas).
5.  **Auditoría de potencial de conversación:** Evaluación de la CTA final para asegurar que fomenta respuestas naturales y profesionales.

---

## 5. Cuándo NO escalar al humano
Para optimizar el flujo operativo, se resolverán internamente y sin molestar al aprobador humano las siguientes incidencias:
-   Ajustes de espaciados de líneas, eliminación de saltos de carro dobles repetidos o corrección de erratas tipográficas.
-   Alineación de hashtags y formateo estético del texto.
-   Reducción de oraciones muy largas para mejorar el flujo de lectura móvil.
-   Sustitución de buzzwords prohibidas aisladas por sinónimos permitidos definidos en la guía de voz.

---

## 6. Cuándo SÍ escalar al humano
Se requiere la intervención por excepción del aprobador humano cuando:
-   Exista una duda razonable sobre si el post vulnera la identidad de marca o el posicionamiento comercial.
-   Se detecte una desviación del tono de voz que afecte al fondo estratégico del mensaje y no pueda corregirse de manera automática.
-   El contenido trate temas sensibles del mercado que puedan generar controversia en el sector.
-   La llamada a la acción (CTA) deba ser redefinida por razones comerciales urgentes.
-   Exista riesgo de mala interpretación del mensaje por parte de la audiencia o la competencia.
-   El borrador esté formalmente correcto en cuanto a estructura y ortografía, pero sea estratégico y argumentalmente débil.

---

## 7. Salida del gate
El reporte de auditoría editorial emitido para cada borrador debe contener:
*   **estado:** [READY_TO_APPROVE, NEEDS_MINOR_EDIT, NEEDS_HUMAN_REVIEW, BLOCKED_BY_BRAND_MISMATCH, BLOCKED_BY_FORMAT_RISK o DISCARDED_NOT_USEFUL]
*   **evaluacion_breve:** [Análisis cualitativo del hook, cuerpo y cierre]
*   **cambios_sugeridos:** [Anotaciones de reescritura para corregir el tono o formato si corresponde]
*   **riesgo:** [Bajo, Medio, Alto. Justificación en caso de riesgo reputacional]
*   **accion_recomendada:** [Paso a seguir en el pipeline, ej: Devolver al redactor o enviar a revisión humana]
