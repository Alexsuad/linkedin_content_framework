# File: MIGRATION_NOTES.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Documentar la clasificación y análisis de migración desde el repositorio fuente.
# Rol: Gobernanza y auditoría documental de migración.
# ──────────────────────────────────────────────────────────────────────

# Informe de Migración Documental Controlada

Este documento detalla la clasificación de los artefactos del repositorio original `Automatizacion_linkedin` para su transición limpia al nuevo `linkedin_content_framework`. Su objetivo es asegurar la flexibilidad del nuevo sistema y prevenir cualquier acoplamiento con la identidad de Alex o el sector logístico.

---

## 1. Archivos Fuente Revisados

Se inspeccionaron y analizaron todos los documentos del repositorio `/home/nalex/Proyectos/Automatizacion_linkedin`:
*   `AGENTS.md` (Instrucciones generales del entorno original)
*   `templates/01_input_pieza_linkedin_plantilla.md` (Plantilla de captura de datos variables)
*   `docs/linkedin/Diseno_Funcional_del_Sistema_LinkedIn.md` (Arquitectura funcional del motor)
*   `docs/linkedin/Gobernanza_Control_y_Roles_LinkedIn.md` (Reglas de gobierno y roles)
*   `docs/linkedin/Manual_Editorial_y_Operativo_LinkedIn.md` (Manual editorial)
*   `docs/linkedin/Sistema_de_publicaciones_LinkedIn.md` (Documento maestro pre-code de 8,359 líneas)
*   `docs/referencias_metodologicas/Politica_Arquitectura_Y_validacion.md` (Políticas de IA y Antigravity)
*   `docs/referencias_metodologicas/Reglas generales Antigravity.md` (Reglas de workspace)
*   `docs/referencias_metodologicas/documento_maestro_lecciones_aprendidas_y_manual_anti_errores_final.md` (Lecciones de sistemas agénticos)

---

## 2. Clasificación del Contenido

### Grupo A: Núcleo Reusable (Core)
Elementos estructurales y de proceso que aplican a cualquier perfil editorial en LinkedIn:
*   **La Regla Madre de Comunicación:** La estructura secuencial lógica `Problema → Fricción Operativa → Solución → Impacto`.
*   **El Pipeline de Transformación:** El flujo por el cual pasa una señal (Captura → Selección → Formato → Borrador → Validación Funcional → Validación Humana → Publicación → Aprendizaje).
*   **Lógica de Formatos:** Formato Tipo 1 (carrusel visual estructurado), Tipo 2 (post de texto simple directo) y Tipo 3 (storytelling basado en escenas).
*   **Estados de una Publicación:** El ciclo de vida de los estados (*Tema Detectado*, *Borrador*, *En Validación Funcional*, *En Aprobación Humana*, *Aprobado*, *Publicado*, *Cerrado*).
*   **Métricas de Negocio vs. Vanidad:** Enfoque prioritario en generar conversaciones cualificadas directas (DMs o llamadas) frente a impresiones y likes vacíos.
*   **Concepto de Validación Humana Obligatoria:** "No Flight" sin aprobación explícita.

### Grupo B: Caso de Uso Específico (Heredado / Variable)
Contenido acoplado al caso original que **no debe migrarse al núcleo general**:
*   **Identidad y Aprobador:** Alex como único aprobador estratégico e identidad central del canal principal. (Debe parametrizarse como "Responsable del Perfil Editorial / Aprobador").
*   **Sector Operativo:** Las referencias explícitas a *logística, transporte, tráfico de mercancías, almacenes, y desorden de flujos de cadena de suministro*. (Quedan acotadas al caso de uso heredado).
*   **CCT / Buyer Personas del Caso:** Referencias a *Director de Tráfico, CEO Logístico, Responsable de Almacén*. (Deben generalizarse a "Perfiles del Cliente Objetivo").
*   **Frecuencia Rígida:** La regla universal de "3 publicaciones semanales oficiales" con días exactos (Jueves = Carrusel). (Debe ser una propiedad configurable del canal).
*   **Integraciones Técnicas:** Flujos y menciones a PriceMonitor, RSVP, y desarrollos en Python de esos proyectos específicos.

### Grupo C: Referencia Metodológica
Directrices metodológicas de control y anti-errores agénticos:
*   **Arquitectura Limpia y Pre-Code:** Conceptos de "medir dos veces, cortar una" y desarrollo híbrido (IA para interpretación, herramientas deterministas para verificación estructural).
*   **Políticas de Ajuste en la Raíz:** No parchar outputs superficialmente; corregir la skill o regla que produjo el fallo.
*   **Uso de Memoria Externa:** Gestión y aislamiento de NotebookLM por cuadernos de perfiles editoriales.

---

## 3. Qué NO se debe migrar todavía

Queda prohibido migrar a la sección core del repositorio:
1.  Los posts redactados y borradores del documento maestro `Sistema_de_publicaciones_LinkedIn.md` (secciones XI a XXIII).
2.  Menciones directas de herramientas y automatizaciones ( PriceMonitor, etc.).
3.  Documentos detallados de gobernanza que no hayan sido parametrizados para abstraer el rol de Alex y el dominio logístico.

---

## 4. Riesgos de Contaminación Conceptual

*   **Riesgo de Monocultivo Temático:** Que el framework asuma que la única forma de generar autoridad es hablando de "operaciones logísticas".
    *   *Mitigación:* Crear el `identity_contract.md` y `principles.md` enfatizando que la logística es un caso de uso (ejemplo inicial) y no la identidad del sistema.
*   **Riesgo de Acoplamiento de Aprobador:** Que el flujo de gobernanza asuma que "Alex" es el único que puede validar los posts.
    *   *Mitigación:* Abstraer el rol de aprobación en la documentación general como `Responsable Editorial / Aprobador Humano`.
*   **Riesgo de Rigidez Operativa:** Convertir la estructura semanal de 3 posts y carrusel obligatorio los jueves en un dogma del sistema.
    *   *Mitigación:* Definir las frecuencias y formatos como propiedades configurables del canal editorial en `docs/templates/channel_config.md`.
