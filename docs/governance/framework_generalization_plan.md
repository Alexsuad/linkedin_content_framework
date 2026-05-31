<!-- File: docs/governance/framework_generalization_plan.md -->

# Plan de Generalización Editorial del Framework LinkedIn

Este documento establece la planificación formal para el **Bloque de Abstracción y Generalización Editorial del Framework**. Su propósito es corregir el sesgo comercial y de nicho del primer caso de uso (`linkedin_autonomo_b2b`) antes de iniciar el diseño de agentes de IA, skills de código, workflows lógicos u otras automatizaciones.

---

## 1. Propósito del bloque

El propósito de este bloque de trabajo es desacoplar conceptualmente el núcleo metodológico del framework de cualquier fin estrictamente mercantil, B2B o de captación de leads. Al corregir el sesgo de primer caso en esta etapa de diseño documental (fase pre-code), garantizamos que la posterior implementación de software y agentes lógicos herede una arquitectura verdaderamente flexible, agnóstica y escalable a cualquier tipo de perfil profesional en LinkedIn.

---

## 2. Diagnóstico de origen

El framework de contenidos se concibió originalmente con vocación general y parametrizable (Sector-Agnóstico y Perfil-Agnóstico, según el `identity_contract.md`). Sin embargo, su primera traza práctica y la validación a través de los Dry Runs Manuales Tipo 1 y Tipo 2 se realizaron utilizando el perfil de prueba `linkedin_autonomo_b2b`. 

Esto provocó que terminologías comerciales, B2B, métricas de captación de leads y metodologías de ventas se colaran de forma implícita en la estructura de gobernanza, templates e instrucciones generales del core del repositorio. Corregir esto no invalida el valor metodológico de los dry runs ejecutados, pero exige elevar una capa de abstracción conceptual superior en el núcleo general.

---

## 3. Problema raíz

El núcleo general del framework (incluyendo la visión, los principios, las directrices y las plantillas base) no debe asumir por defecto que el usuario del sistema:
*   Vende un servicio o producto.
*   Tiene clientes o busca "leads".
*   Opera exclusivamente en el sector B2B (Business to Business).
*   Representa a una entidad jurídica o empresa.
*   Requiere llamadas a la acción (CTA) orientadas a la conversión comercial.
*   Debe definir un "Buyer Persona".
*   Tiene una oferta de entrada o propuesta comercial estructurada.

---

## 4. Principio rector

Para resolver la generalización, el framework se regirá por la siguiente ley de diseño conceptual:

> **“El core define conceptos amplios. Los casos de uso especializan esos conceptos.”**

A continuación, se detalla la correspondencia conceptual entre la capa abstracta (Core) y las capas especializadas de los casos de uso:

*   **Capa Core:** Audiencia objetivo (o perfil de lector de interés).
    *   *Caso de Uso Autónomo B2B:* Decisores de compras B2B (directores de operaciones, gerentes).
    *   *Caso de Uso Empleado Experto:* Colegas del sector, reclutadores, líderes de opinión.
*   **Capa Core:** Acción o reacción esperada (el resultado de la lectura).
    *   *Caso de Uso Autónomo B2B:* Conversación directa en privado, agendamiento de diagnóstico.
    *   *Caso de Uso Marca Corporativa (Empresa):* Descarga de recursos, employer branding, atracción de talento.
*   **Capa Core:** Propuesta de valor o enfoque del perfil.
    *   *Caso de Uso Autónomo B2B:* Resolución de cuellos de botella mediante rediseño de procesos.
    *   *Caso de Uso Personal Profesional:* Visibilidad técnica, posicionamiento en un nicho de conocimiento específico, networking.

---

## 5. Lo que NO se debe rehacer

Este bloque de generalización actúa de forma quirúrgica sobre la semántica y los supuestos editoriales. No se modificará la estructura técnica y metodológica ya validada:
*   La **estructura de carpetas** del repositorio (`docs/core/`, `docs/governance/`, `docs/templates/`, `docs/use_cases/`).
*   La **separación estricta** entre la capa core y la capa de casos de uso.
*   Los **gates de gobernanza** existentes (`brief_sufficiency_gate.md`, `editorial_audit_gate.md`).
*   La **política de seguridad y claims** (`claims_and_risk_policy.md`).
*   La estructura de control y metadatos de `post_output_contract.md`.
*   La **matriz funcional** de roles y la lógica de aprobación humana.
*   Las **auditorías deterministas** ya implementadas (`audit_precode_repo.py`, `audit_conceptual_contamination.py`, `audit_editorial_language.py`).
*   El perfil de uso de referencia `linkedin_autonomo_b2b` y las evidencias de dry runs ya consolidadas.

---

## 6. Tareas planificadas del bloque

Este bloque de trabajo se estructurará en las siguientes tareas secuenciales de edición documental:

### Tarea 1 — Crear abstracción de perfiles
Crear el archivo raíz de gobernanza `docs/core/profile_abstraction.md` que catalogue y diferencie teóricamente las necesidades del canal según el perfil del emisor. Debe definir como mínimo:
*   `linkedin_personal_profesional` (marca personal general, red de contactos).
*   `linkedin_empleado_profesional` (visibilidad técnica, marca empleadora).
*   `linkedin_autonomo_b2b` (autoridad operativa, generación de leads).
*   `linkedin_empresa` (página corporativa, reputación de marca, reclutamiento).
*   `linkedin_organizacion` (ONGs, comunidades, asociaciones sin ánimo de lucro).

### Tarea 2 — Generalizar core y plantillas
Modificar y limpiar los términos de sesgo comercial en el core y en las plantillas de entrada/salida. 
*   **Archivos a editar:** `docs/core/vision.md`, `docs/core/identity_contract.md`, `README.md`, `AGENTS.md`, `docs/core/principles.md`, `docs/core/scope_yes_no.md`, `docs/templates/client_intake_template.md` (renombrado conceptualmente en el contenido como *intake de perfil o proyecto*), `docs/templates/input_signal_template.md`, `docs/templates/post_output_contract.md` y `docs/implementation_plan.md`.
*   **Modificaciones semánticas:** Reemplazar "cliente" por "usuario/perfil", "buyer persona" por "audiencia objetivo", "oferta" por "propuesta de valor/siguiente acción deseada", "conversión" por "reacción o interacción cualificada".

### Tarea 3 — Crear perfiles alternativos mínimos
Asegurar el soporte conceptual mediante la creación de los subdirectorios y ficheros README base para los perfiles alternativos:
*   `docs/use_cases/linkedin_empleado_profesional/README.md`
*   `docs/use_cases/linkedin_empresa/README.md`
*   `docs/use_cases/linkedin_personal_profesional/README.md`
Cada archivo detallará el propósito del perfil, el tipo de usuario, los objetivos, riesgos de tono y su diferencia frente al caso autónomo B2B.

### Tarea 4 — Diversificar ejemplos
Editar `docs/use_cases/linkedin_autonomo_b2b/examples_good_bad.md` para introducir ejemplos ilustrativos adicionales de hooks, fricciones y CTA que provengan de otros contextos prácticos (reputación profesional, alineación del equipo, marca empleadora), evitando la uniformidad exclusiva de temas logísticos u operativos.

### Tarea 5 — Etiquetar evidencias existentes de dry runs
Añadir notas introductorias en:
*   `docs/evidence/dry_runs/tipo_2_post_simple/dry_run_001.md`
*   `docs/evidence/dry_runs/tipo_1_carrusel/dry_run_001.md`
Estableciendo explícitamente que estas trazas documentales son registros específicos del perfil `linkedin_autonomo_b2b` y no constituyen el estándar único o la plantilla universal del framework general.

### Tarea 6 — Validaciones del proceso
Ejecutar todos los scripts de validación del repositorio para confirmar que las modificaciones respetan el estado pre-code y no generan contaminación.

---

## 7. Criterios de aceptación del bloque

El bloque de abstracción y generalización se considerará completado con éxito únicamente si cumple con:
1.  Las plantillas base y el núcleo general admiten ser completados por cualquier perfil (persona, empleado, empresa u organización) sin obligar a definir variables de venta o conversión comercial.
2.  El perfil `linkedin_autonomo_b2b` queda reubicado conceptualmente como un caso de uso específico de referencia y no como la identidad del framework.
3.  Existen los archivos README base de los perfiles alternativos definidos en la Tarea 3.
4.  La biblioteca de ejemplos de buen/mal comportamiento del contenido está diversificada conceptualmente.
5.  Los scripts de auditoría (`audit_precode_repo.py`, `audit_conceptual_contamination.py`, `audit_editorial_language.py`) se ejecutan con éxito y devuelven `EXIT 0`.

---

## 8. Riesgos

*   **Abstracción excesiva:** Diluir tanto los términos que el framework se vuelva inútil, genérico o difícil de entender para los redactores lógicos.
    *   *Mitigación:* Mantener ejemplos prácticos de especialización en cada caso de uso para guiar el flujo.
*   **Rotura del caso autónomo B2B:** Modificar de forma inadecuada el core de manera que afecte la viabilidad de la redacción ya probada en los dry runs.
    *   *Mitigación:* Realizar pruebas de auditoría continua tras cada edición menor.
*   **Sobrediseño prematuro de perfiles alternativos:** Intentar detallar en profundidad las reglas de marca personal o de empresa corporativa antes de consolidar el core.
    *   *Mitigación:* Limitar los README de los casos alternativos a descripciones mínimas operativas.

---

## 9. Reglas de ejecución

*   Se prohíben los reemplazos masivos automatizados globales (ej. no usar comandos `sed` o expresiones de reemplazo ciego sobre todo el repositorio). Cada cambio en los documentos debe ser evaluado línea por línea.
*   No se tocarán los casos de uso especializados durante la generalización del core, salvo las adiciones explícitas especificadas en las tareas.
*   Durante este bloque, **no se creará código de software**, agentes lógicos, skills, servidores MCP o flujos CLI. El enfoque sigue siendo estrictamente documental y de gobernanza pre-code.

---

## 10. Siguiente paso después del bloque

Una vez consolidada esta generalización y cerrada de forma oficial, el proyecto estará listo para:
1.  Diseñar y ejecutar un dry run de prueba no comercial (ej. para el perfil `linkedin_empleado_profesional`) y validar que el framework generalizado responde con éxito a otros objetivos.
2.  Evaluar qué aprendizajes editoriales y reglas semánticas se incorporan permanentemente a futuras skills agénticas.
3.  Retomar de forma segura el diseño de la arquitectura agéntica de software.
