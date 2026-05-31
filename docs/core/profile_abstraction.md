<!-- File: docs/core/profile_abstraction.md -->

# Abstracción de Perfiles Editoriales (Profile Abstraction)

Este documento actúa como la fuente de verdad conceptual del framework para definir y separar los diferentes tipos de perfil que emiten contenidos en LinkedIn. Su propósito es evitar que el núcleo general del sistema o los futuros agentes de automatización asuman por defecto una naturaleza comercial, B2B o de captación de leads.

---

## 1. Clasificación de Perfiles Editoriales

El framework reconoce de forma nativa cinco clases de perfil en LinkedIn, cada uno con reglas de tono, objetivos y niveles de institucionalidad diferenciados:

### A. `linkedin_personal_profesional` — Perfil personal profesional
*   **Descripción:** Canal individual enfocado en la visibilidad profesional de un nicho de conocimiento específico, el networking, la reputación técnica o la marca personal.
*   **Enfoque de contenido:** Compartir aprendizajes individuales, reflexiones sobre el sector, avances de proyectos o comentarios profesionales sobre eventos de interés.
*   **Exclusión:** Evita ser categorizado por defecto como "creador de contenido", "influencer" o someterse a lógicas de la *creator economy*. No requiere ofertas comerciales ni conversión de ventas.

### B. `linkedin_empleado_profesional` — Empleado profesional
*   **Descripción:** Empleado experto que comparte su criterio profesional, aprendizajes de campo y conocimiento sectorial acumulado a pie de obra.
*   **Enfoque de contenido:** Casos prácticos resueltos a nivel operativo, errores comunes del día a día técnico, y explicaciones didácticas de valor sectorial.
*   **Independencia corporativa:** Puede publicar de forma independiente o con vínculo directo a la marca empleadora (ej. apoyando campañas corporativas o aportando a la atracción de talento/employer branding), pero el framework no asume que actúa obligatoriamente como un embajador corporativo de representación.

### C. `linkedin_autonomo_b2b` — Profesional independiente B2B
*   **Descripción:** Perfil individual de un consultor, programador, diseñador u optimizador de procesos independiente que opera en mercados B2B.
*   **Enfoque de contenido:** Exposición de fricciones operativas reales, impacto de los desórdenes organizativos, aprendizajes prácticos aplicados a la empresa y metodologías de solución.
*   **Objetivos comerciales:** Puede tener objetivos de captación comercial o de generación de leads calificados, pero su comunicación debe mantener un posicionamiento de autoridad técnica y criterio libre de tácticas de venta directa, promesas mágicas de ROI o copy publicitario genérico.

### D. `linkedin_empresa` — Marca corporativa / Página de empresa
*   **Descripción:** Página oficial o canal corporativo institucional que representa a una persona jurídica, empresa o marca comercial.
*   **Enfoque de contenido:** Comunicación de capacidades técnicas y de infraestructura, hitos corporativos, atracción de talento (employer branding), cultura organizativa e institucional.
*   **Objetivos del canal:** Construcción de reputación corporativa a largo plazo, confianza de marca, y relación estratégica con audiencias clave del sector.

### E. `linkedin_organizacion` — Organización, comunidad o institución
*   **Descripción:** Canal representativo de fundaciones, asociaciones, comunidades técnicas, iniciativas de carácter público, proyectos colectivos, o instituciones educativas.
*   **Enfoque de contenido:** Educación de la audiencia, divulgación de causas, noticias del sector sin fines lucrativos y fomento de la participación comunitaria o colectiva.

---

## 2. Campos Variables por Perfil

Para garantizar la modularidad del sistema, la configuración de cada caso de uso debe delimitar de forma aislada los siguientes campos variables:

*   **Objetivo editorial:** El beneficio que busca el perfil con su presencia (ej. visibilidad técnica, confianza institucional, captación B2B, difusión social).
*   **Tipo de audiencia:** A quién se dirige prioritariamente el contenido (ej. decisores de compras, colegas del sector, reclutadores, público general).
*   **Acción o reacción esperada:** El resultado deseado tras la lectura (ej. debate en comentarios, mensajes privados de consulta, suscripción a comunidad, postulación de talento).
*   **Nivel comercial:** Rango de intención comercial, que varía desde nulo (perfiles personales/organizaciones) hasta estratégico indirecto (profesionales B2B).
*   **Tipo de CTA (Call to Action):** La llamada a la acción recomendada (conversacional, técnica, informativa).
*   **Métricas relevantes:** Los indicadores clave de éxito (ej. interacciones cualificadas en comentarios, mensajes privados de interés técnico, descargas de recursos corporativos).
*   **Riesgos de tono:** Desviaciones específicas a vigilar en el canal (ej. parecer soberbio en marca personal, aburrido/acartonado en página de empresa, o vendedor en perfil autónomo).
*   **Nivel de institucionalidad:** Grado de representación formal corporativa exigido al copy (desde tono individual e informal hasta declarativas de prensa institucionales).

---

## 3. Regla Constitucional de Diseño Agéntico

Se establece una regla obligatoria e innegociable para toda la arquitectura agéntica del framework:

> **Ningún agente, skill o workflow futuro debe asumir por defecto que el perfil tiene cliente, oferta, lead, conversión, buyer persona o intención comercial. Esos campos solo se activan si el perfil o caso de uso los define explícitamente.**

El núcleo general y las plantillas operan de forma neutra y amplia. Toda terminología orientada a la comercialización se considera una especialización exclusiva del caso de uso correspondiente y no se integrará en la lógica por defecto del sistema.
