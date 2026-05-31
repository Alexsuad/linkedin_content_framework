<!-- File: docs/architecture/functional_specialists_matrix.md -->

# Matriz de especialistas funcionales

## Propósito
Definir de manera formal las responsabilidades funcionales que deben existir en el ciclo de producción, validación e intake del framework de contenido. Este documento mapea cada especialidad organizativa antes de tomar decisiones técnicas de desarrollo de software, asegurando que no se creen agentes lógicos de Inteligencia Artificial de forma prematura ni se dejen ocultas responsabilidades operativas clave.

El framework persigue un diseño eficiente:
1.  **Evitar la fragmentación:** No crear un agente o skill de código por cada tarea.
2.  **Visibilidad operativa:** Garantizar que los controles de calidad, mitidades de riesgo de claims, marcas y aprobación final tengan una sede funcional asignada.

---

## 1. Criterio para clasificar responsabilidades
Cada responsabilidad mapeada debe ubicarse de manera preliminar en uno de los siguientes componentes del sistema según su naturaleza:

*   **Agente:** Se selecciona cuando la tarea requiere criterio propio complejo, evaluación de contextos variables, razonamiento subjetivo sobre el tono o capacidad para arbitrar, devolver o bloquear el flujo de trabajo basándose en múltiples variables.
*   **Skill:** Se aplica a tareas acotadas, mecánicas, repetibles y estructuradas con entradas y salidas lógicas cerradas (ej. llamadas a APIs internas, conversiones de formato de texto o validaciones de expresiones regulares).
*   **Gate:** Puntos de control lógico que evalúan si un entregable cumple con los criterios de paso y le asignan un estado estandarizado para permitir o impedir su avance.
*   **Regla:** Directrices o restricciones transversales que el sistema debe aplicar de forma constante a lo largo de todo el pipeline (ej. regulación de las menciones de logística en el núcleo, prohibiéndolas como reglas universales pero permitiéndolas como referencias normativas o históricas de ejemplo).
*   **Workflow:** Secuencias ordenadas de pasos y orquestaciones que conectan las entradas, los agentes, las skills y los gates para procesar la información.
*   **Configuración:** Parámetros o archivos locales que definen el comportamiento de un caso de uso, canal o perfil específico sin alterar el código (ej. frecuencia de publicación).
*   **Fase futura:** Responsabilidades previstas que quedan fuera del alcance del desarrollo inicial y cuya implementación se pospone para evitar la sobrearquitectura.

---

## 2. Matriz funcional principal

| Nº | Responsabilidad funcional | Qué protege o aporta | Entrada principal | Salida esperada | Ubicación preliminar | Fase recomendada | Riesgo si se omite |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Especialista de Intake y Acompañamiento del Cliente | Calidad de las señales iniciales y recopilación estratégica de datos de marca. | Entrevistas o notas crudas del cliente. | Fichas de señales y planes semanales completos. | Rol manual (con apoyo de plantillas) | Fase 1 | Contenido genérico o inventado por falta de datos verídicos de origen. |
| 2 | Estratega de contenido / posicionamiento | Alineación del contenido con los objetivos de negocio a largo plazo. | Cuestionario de posicionamiento del cliente. | Pilares de contenido y narrativas definidos. | Configuración / Documento base | Fase 1 | Publicaciones inconexas que no construyen autoridad de marca. |
| 3 | Especialista en audiencia / cliente objetivo | Adecuación del nivel de lenguaje y temas de interés al buyer persona. | Ficha de perfil de audiencia del cliente. | Filtro de validación de audiencia. | Regla / Configuración del perfil | Fase 1 | Post que resultan demasiado técnicos o irrelevantes para el decisor de compra. |
| 4 | Curador de materia prima / investigador | Filtrado y ordenación de las ideas del intake para seleccionar insumos útiles. | Notas operativas crudas de la semana. | Ideas de posts seleccionadas y calificadas. | Rol manual / Workflow semanal | Fase 1 | Sobrecarga de borrradores basados en ideas débiles o repetidas. |
| 5 | Redactor LinkedIn | Estructuración y redacción inicial de la publicación candidata. | Ficha de señal de entrada aprobada. | Borrador estructurado de post o carrusel. | Posible agente futuro / Responsabilidad funcional | Fase 2 | Bloqueo operativo por incapacidad para generar textos consistentes. |
| 6 | Especialista de hooks | Captar la atención en el feed en los primeros tres segundos de visualización. | Copy del cuerpo del post. | Alternativas de hooks de alto impacto. | Skill de formateo / Modificador | Fase 2 | Bajas tasas de lectura del contenido por aperturas aburridas. |
| 7 | Editor de claridad y voz | Fluidez, sencillez de lectura y adecuación al estilo verbal del perfil. | Borrador crudo de la publicación. | Post con oraciones optimizadas para móviles. | Posible agente futuro / Responsabilidad funcional | Fase 2 | Textos difíciles de leer o que suenan de forma robótica y artificial. |
| 8 | Especialista en voz, tono y narrativa | Coherencia del arquetipo verbal del cliente en todo el lote de contenido. | Manual de estilo de voz del cliente. | Reporte de cumplimiento del arquetipo de voz. | Regla / Validador semántico | Fase 1 (Diseño) | Pérdida de la identidad verbal o mezcla de estilos contradictorios. |
| 9 | Especialista en marca / posicionamiento | Evitar que el post se desvíe de los temas estratégicos de la cuenta. | Directrices de posicionamiento del perfil. | Validación de pilares temáticos del post. | Regla de exclusión / Configuración | Fase 1 | Dilución del nicho de mercado del autor por hablar de temas ajenos. |
| 10 | Diseñador visual / diseñador gráfico | Soporte visual que facilite la asimilación del contenido técnico. | Copy final de la publicación. | Propuesta de diseño gráfico o esquema. | Fase futura / Proceso manual | Fase 7 | Publicaciones áridas de texto plano sobre conceptos de alta complejidad. |
| 11 | Diseñador de carruseles | Estructura y flujo narrativo slide por slide de documentos PDF. | Post de estructura secuencial. | Guion visual y de textos de cada slide. | Posible agente futuro / responsabilidad funcional (modo carrusel) | Fase 2 | Carruseles con exceso de texto o sin un flujo explicativo coherente. |
| 12 | Director de arte / imágenes | Consistencia estética y calidad de los recursos gráficos adjuntos. | Especificación visual del post. | Imagen final aprobada. | Fase futura | Fase 7 | Incorporación de imágenes de stock genéricas o de IA artificial de baja calidad. |
| 13 | Auditor editorial / calidad | Calificación objetiva de la legibilidad, formato y valor de la pieza. | Contrato de salida del post completo. | Estado de auditoría asignado. | Gate de calidad editorial | Fase 1 (Diseño) / Fase 4 (Auditoría) | Envío al aprobador de publicaciones con errores de Hook, CTA o formato. |
| 14 | Auditor de riesgo / claims | Protección legal y reputacional sobre las afirmaciones vertidas. | Borrador de post y referencias de origen. | Reporte de nivel de riesgo y claims. | Gate de claims y riesgos | Fase 1 / Fase 4 | Demandas legales, revelación de secretos o promesas falsas de ROI. |
| 15 | Especialista de formato LinkedIn | Ajuste visual de párrafos y emojis para maximizar el CTR móvil. | Borrador de post validado. | Post formateado según las reglas de visualización. | Skill de formateo visual | Fase 2 | Visualización rota en smartphones con párrafos densos de texto. |
| 16 | Analista de rendimiento / aprendizaje | Mejora continua del pipeline a partir del feedback de analítica. | Métricas del canal y DMs generados. | Ajustes de prompts y base de conocimiento. | Fase futura | Fase 7 | Repetición de errores o incapacidad para optimizar el tono según respuestas. |
| 17 | Gestor de comunidad / interacción | Activación de debates en la sección de comentarios del post publicado. | Comentarios de la audiencia en LinkedIn. | Respuestas rápidas del autor del perfil. | Fase futura / Rol manual | Fase 7 | Muerte algorítmica del post por falta de respuestas e interacción inicial. |
| 18 | Responsable de aprobación humana | Control final del contenido bajo el principio de firma manual del lote. | Publicaciones candidatas en READY_TO_APPROVE. | Firma digital / Luz verde de publicación. | Proceso manual del aprobador (adaptable según nivel de autonomía) | Fase 1 | Publicación no autorizada de contenido sensible o desalineado. |

---

## 3. Reglas específicas por responsabilidad

### 3.1 Especialista de Intake y Acompañamiento del Cliente
*   **Función:** Guía al cliente durante la recogida de información estratégica y semanal, detecta respuestas incompletas o ambiguas, y estructura las notas crudas en fichas de señales consistentes.
*   **Qué NO hace:** No genera borradores de post ni aprueba publicaciones finales de cara al canal de LinkedIn.
*   **Representación arquitectónica:** Rol funcional obligatorio de entrada, operado de forma manual apoyándose en plantillas estructuradas.
*   **Documentos relacionados:** `client_intake_template.md`, `weekly_content_intake_template.md`, `input_signal_template.md`, `brief_sufficiency_gate.md`.

### 3.2 Estratega de contenido / posicionamiento
*   **Función:** Define los pilares y narrativas transversales de la marca para asegurar que el contenido construya autoridad y relevancia comercial.
*   **Qué NO hace:** No redacta el copy de las publicaciones individuales ni diseña soportes gráficos.
*   **Representación arquitectónica:** Documento de configuración estratégica estable cargado en el contexto de generación.
*   **Documentos relacionados:** `client_intake_template.md`, `voice_and_narrative_template.md`.

### 3.3 Especialista en audiencia / cliente objetivo
*   **Función:** Valida que los problemas tratados en el post respondan a las preocupaciones y al lenguaje técnico que maneja el buyer persona definido.
*   **Qué NO hace:** No define la oferta comercial ni gestiona las interacciones o comentarios en el canal.
*   **Representación arquitectónica:** Filtros de contexto en el agente redactor y checks lógicos en la auditoría editorial.
*   **Documentos relacionados:** `client_intake_template.md`, `editorial_audit_gate.md`.

### 3.4 Curador de materia prima / investigador de contenido
*   **Función:** Evalúa la veracidad y relevancia operativa de las notas de la semana y selecciona las 3 señales de entrada aptas para redactar.
*   **Qué NO hace:** No realiza la redacción de los borradores finales ni edita el tono de voz.
*   **Representación arquitectónica:** Proceso manual del especialista agéntico apoyado por el gate de suficiencia del brief.
*   **Documentos relacionados:** `weekly_content_intake_template.md`, `brief_sufficiency_gate.md`.

### 3.5 Redactor LinkedIn
*   **Función:** Transforma el brief aprobado de la señal de entrada en un borrador de publicación que respeta la estructura de fricción y solución.
*   **Qué NO hace:** No toma la decisión final de publicación ni altera de forma autónoma los pilares estratégicos de la marca.
*   **Representación arquitectónica:** Posible agente futuro / responsabilidad funcional de redacción.
*   **Documentos relacionados:** `post_output_contract.md`, `input_signal_template.md`.

### 3.6 Especialista de hooks
*   **Función:** Redacta y optimiza de forma aislada las dos primeras líneas de la publicación para generar tensión operativa y capturar la atención en el feed.
*   **Qué NO hace:** No redacta el cuerpo de la publicación ni edita las llamadas a la acción (CTAs).
*   **Representación arquitectónica:** Skill lógica enfocada en la reescritura y optimización de hooks o subtarea del agente redactor.
*   **Documentos relacionados:** `post_output_contract.md`, `voice_and_style.md`.

### 3.7 Editor de claridad y voz
*   **Función:** Adapta el borrador crudo de la publicación para asegurar que fluya de forma natural y mantenga frases cortas optimizadas para dispositivos móviles.
*   **Qué NO hace:** No añade información o claims técnicos que no estuvieran en el brief original.
*   **Representación arquitectónica:** Posible agente futuro / responsabilidad funcional de edición de estilo o posible skill futura.
*   **Documentos relacionados:** `post_output_contract.md`, `voice_and_style.md`, `visual_rules.md`.

### 3.8 Especialista en voz, tono y narrativa
*   **Función:** Verifica la coherencia verbal de la pieza frente al arquetipo verbal del cliente y detecta desvíos de identidad.
*   **Qué NO hace:** No genera el contenido inicial ni decide los formatos gráficos a utilizar.
*   **Representación arquitectónica:** Regla lógica de exclusión de buzzwords y arquetipos prohibidos cargada en el validador.
*   **Documentos relacionados:** `voice_and_narrative_template.md`, `voice_and_style.md`, `editorial_audit_gate.md`.

### 3.9 Especialista en marca / posicionamiento
*   **Función:** Controla que los temas tratados en el borrador estén alineados estrictamente con el nicho de autoridad del perfil.
*   **Qué NO hace:** No corrige faltas de ortografía ni ajusta los espaciados visuales del post.
*   **Representación arquitectónica:** Filtro de temática cargado en la configuración local del caso de uso.
*   **Documentos relacionados:** `client_intake_template.md`, `profile_config.md`, `editorial_audit_gate.md`.

### 3.10 Diseñador visual / diseñador gráfico
*   **Función:** Crea o conceptualiza las piezas gráficas, esquemas o diagramas necesarios para dar soporte visual a las publicaciones.
*   **Qué NO hace:** No redacta el copy de los posts de texto plano ni aprueba claims de veracidad de datos.
*   **Representación arquitectónica:** Proceso manual del especialista de diseño / Fase futura de automatización.
*   **Documentos relacionados:** `visual_rules.md`, `post_output_contract.md`.

### 3.11 Diseñador de carruseles
*   **Función:** Divide y estructura los contenidos de un post de Tipo 1 en un guion estructurado slide por slide para facilitar su diseño y lectura en formato PDF.
*   **Qué NO hace:** No define la identidad corporativa de la marca ni diseña de forma directa los archivos finales.
*   **Representación arquitectónica:** Posible agente futuro / responsabilidad funcional en modo carrusel.
*   **Documentos relacionados:** `visual_rules.md`, `post_output_contract.md`.

### 3.12 Director de arte / especialista en imágenes
*   **Función:** Supervisa la consistencia estética y el cumplimiento de las políticas de riesgo visual de las imágenes adjuntas a los posts.
*   **Qué NO hace:** No realiza la redacción de los textos ni decide la frecuencia de las campañas semanales.
*   **Representación arquitectónica:** Filtro de calidad visual / Fase futura.
*   **Documentos relacionados:** `visual_rules.md`, `post_output_contract.md`.

### 3.13 Auditor editorial / calidad de contenido
*   **Función:** Califica el borrador final generado bajo el contrato de salida y le asigna un estado operativo (ej. `READY_TO_APPROVE`, `NEEDS_MINOR_EDIT`).
*   **Qué NO hace:** No edita de forma directa el texto ni interactúa comercialmente con la audiencia del cliente.
*   **Representación arquitectónica:** Gate lógico de paso con reglas de comprobación de calidad.
*   **Documentos relacionados:** `editorial_audit_gate.md`, `post_output_contract.md`.

### 14. Auditor de riesgo / reputación / claims
*   **Función:** Aplica la política de riesgos para detectar claims falsificados, datos confidenciales expuestos o tono de gurú que atente contra la marca.
*   **Qué NO hace:** No reescribe de forma autónoma el cuerpo completo de la publicación ni diseña diagramas.
*   **Representación arquitectónica:** Gate lógico y semántico de riesgos basado en la política de claims.
*   **Documentos relacionados:** `claims_and_risk_policy.md`, `post_output_contract.md`.

### 3.15 Especialista de formato LinkedIn
*   **Función:** Formatea el copy final optimizando el uso de emojis, negritas permitidas, espacios en blanco y saltos de línea para móviles.
*   **Qué NO hace:** No altera el fondo del mensaje ni añade promesas o claims de negocio.
*   **Representación arquitectónica:** Posible skill futura / Ubicación arquitectónica preliminar.
*   **Documentos relacionados:** `visual_rules.md`, `post_output_contract.md`.

### 3.16 Analista de rendimiento / aprendizaje
*   **Función:** Extrae aprendizajes a partir de la interacción real de los posts y los DMs recibidos para retroalimentar las guías de prompts.
*   **Qué NO hace:** No realiza la redacción en tiempo real de los posts ni participa en el intake semanal.
*   **Representación arquitectónica:** Fase futura de análisis de datos y orquestación de feedback.
*   **Documentos relacionados:** `weekly_content_intake_template.md`, `decision_log.md`.

### 3.17 Gestor de comunidad / interacción
*   **Función:** Propone respuestas rápidas y profesionales ante las interacciones de los usuarios en el feed de LinkedIn del autor.
*   **Qué NO hace:** No publica posts sin aprobación humana ni gestiona el intake estratégico de la marca.
*   **Representación arquitectónica:** Fase futura / Proceso manual de atención de comentarios.
*   **Documentos relacionados:** `voice_and_style.md`, `profile_config.md`.

### 3.18 Responsable de aprobación humana
*   **Función:** Valida y firma el lote de publicaciones candidatas en estado `READY_TO_APPROVE` para dar la luz verde definitiva para su publicación.
*   **Qué NO hace:** No debe realizar tareas de edición manual de formato ni comprobación ortográfica sistemática que correspondan a la auditoría interna.
*   **Representación arquitectónica:** Gate adaptativo según nivel de autonomía (firma manual obligatoria en calibración o aprobación compacta por lotes en producción).
*   **Documentos relacionados:** `principles.md`, `antigravity_task_protocol.md`, `post_output_contract.md`.

---

## 4. Responsabilidades que NO deben implementarse todavía
Las siguientes funciones estratégicas quedan fuera del alcance del desarrollo inicial y no deben ser codificadas ni automatizadas en la Fase 1 del proyecto:
-   **Publicación automática:** Ubicación arquitectónica preliminar: el flujo termina en la generación de archivos PDF o textos en formato crudo listos para el copiado manual del usuario.
-   **Integración con API de LinkedIn:** No se realizarán desarrollos ni conexiones de software con servicios externos de publicación desatendida.
-   **Uso de MCP (Model Context Protocol):** No se integrarán servidores de comunicación agéntica para la conexión de herramientas complejas externas.
-   **Automatización de comentarios:** Queda prohibido el diseño de bots de interacción automática en el feed.
-   **Analítica avanzada y dashboard de métricas:** La extracción de estadísticas de impacto de LinkedIn se realizará de forma manual.
-   **Aprendizaje automático basado en métricas:** No se implementará auto-ajuste de prompts en base a embeddings ni bases vectoriales en esta etapa.
-   **Automatización completa de imágenes:** El diseño gráfico o generación de diapositivas de carruseles se realizará por parte del especialista humano.
-   **Gestión avanzada de comunidad:** La moderación de la bandeja de mensajes privados (DMs) queda excluida de la automatización.

---

## 5. Reglas para evitar sobrearquitectura
-   **Higiene de Agentes:** No estructurar agentes independientes para cada especialista funcional de forma prematura. Se propone evaluar la agrupación de tareas de redacción, hooks y formato en responsabilidades funcionales consolidadas en la Fase 2 bajo el principio de minimalismo agéntico.
-   **Desarrollo de Skills bajo demanda:** No programar funciones o skills de software en Python hasta que sus entradas y salidas estén delimitadas y aprobadas en el catálogo de herramientas.
-   **Workflow sin código previo:** No modelar ni programar orquestaciones complejas de workflows sin haber validado manualmente la efectividad de las secuencias en la fase de dry runs.
-   **Publicación controlada:** La salida al canal se regula por niveles de autonomía y gates de calibración adaptativos, desde la aprobación manual individual en el inicio hasta firmas compactas en lotes o excepciones en fases avanzadas.
-   **Auditoría interna previa:** El aprobador humano no debe ser utilizado como filtro corrector de fallos de formato, ortografía o tono que el validador agéntico interno debe descartar con antelación.
-   **Aislamiento del Core:** No asociar las reglas del perfil `linkedin_autonomo_b2b` con las directrices generales del framework. Las reglas particulares de voz o frecuencia pertenecen a configuraciones locales.

---

## 6. Relación con auditoría agéntica y aprobación humana compacta
La orquestación de la matriz funcional garantiza una toma de decisiones eficiente para el aprobador humano:
-   **Auditoría Agéntica Fuerte:** Los gates de suficiencia, auditoría editorial y riesgos operan como filtros automatizados severos antes de la interacción con el usuario. Si un borrador tiene riesgo medio/alto o fallos formales, se bloquea y devuelve de forma interna.
-   **Aprobación Compacta por Lote:** El sistema consolida semanalmente los borradores que alcanzan el estado `READY_TO_APPROVE` y le presenta al aprobador un paquete de salida editorial-operativa único y ordenado para su firma rápida.
-   **Revisión por Excepción:** El aprobador humano solo dedicará tiempo de revisión detallada a aquellas publicaciones catalogadas como `NEEDS_HUMAN_REVIEW` debido a riesgos o decisiones estratégicas fronterizas.

---

## 7. Criterio de cierre del documento
El documento se considera completo y su gate cerrado cuando:
1.  Las 18 responsabilidades funcionales se encuentran mapeadas, asignándoles una ubicación preliminar coherente con el minimalismo agéntico.
2.  Quedan delimitadas explícitamente las funciones excluidas del alcance del desarrollo inicial.
3.  El script de verificación determinista (`tools/audit_precode_repo.py`) lo valida sin advertencias de higiene conceptual o formato.
