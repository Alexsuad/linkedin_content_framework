# File: AGENTS.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Normas de comportamiento para agentes de IA en el repositorio.
# Rol: Manual de operación del entorno de agentes.
# ──────────────────────────────────────────────────────────────────────

# Manual de Operación para Agentes de IA (AGENTS.md)

Este documento contiene las reglas de trabajo que toda Inteligencia Artificial (incluyendo subagentes y herramientas integradas) debe seguir de forma innegociable cuando actúe sobre este repositorio.

---

## 1. Protocolo de Lectura Obligatorio

Antes de auditar, proponer cambios o modificar cualquier documento, el agente debe leer obligatoriamente estos archivos en el siguiente orden:
1.  [README.md](file:///home/nalex/Proyectos/linkedin_content_framework/README.md) — Para entender la naturaleza y el estado actual del repositorio.
2.  [docs/core/identity_contract.md](file:///home/nalex/Proyectos/linkedin_content_framework/docs/core/identity_contract.md) — Para asimilar la separación conceptual entre el framework madre y los perfiles editoriales.
3.  [docs/core/principles.md](file:///home/nalex/Proyectos/linkedin_content_framework/docs/core/principles.md) — Para actuar conforme a las leyes operativas del sistema.

---

## 2. Reglas Operativas Innegociables

*   **No Contaminar el Núcleo:** Se prohíbe usar logística, Alex, transporte o cualquier caso heredado como identidad, audiencia, aprobador, frecuencia o regla universal del framework.

    Se permiten menciones normativas cuando el texto explique que esos elementos pertenecen a casos heredados, ejemplos, configuraciones específicas o referencias históricas que no deben contaminar el núcleo general.

*   **No Dogmatizar Decisiones Locales:** No conviertas los ritmos, cadencias o configuraciones del caso de uso heredado (ej. frecuencias fijas, carruseles en días específicos) en leyes universales del framework. El sistema es parametrizable.
*   **No Crear Código sin Aprobación:** Este repositorio está en fase **pre-code**. No generes scripts en Python, APIs, conectores u otros desarrollos técnicos de software hasta que la fase sea formalmente cerrada y aprobada por el usuario.
*   **No Modificar Archivos Fuera del Repositorio:** El alcance de tus tareas se limita exclusivamente a `/home/nalex/Proyectos/linkedin_content_framework`. No borres ni edites archivos fuera de esta ruta.
*   **Aislamiento del Origen:** Bajo ninguna circunstancia edites, muevas o borres archivos del repositorio fuente `/home/nalex/Proyectos/Automatizacion_linkedin`. Su uso es estrictamente de solo lectura.

---

## 3. Resolución de Conflictos

Si en la ejecución de tus tareas detectas una inconsistencia entre los documentos del framework y las necesidades de un caso de uso, no tomes la decisión de forma autónoma:
1.  Documenta la discrepancia en tu reporte.
2.  Detén el flujo de ejecución.
3.  Pide aprobación explícita al usuario para resolver el conflicto conceptual.
