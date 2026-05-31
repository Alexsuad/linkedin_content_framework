# File: docs/core/scope_yes_no.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Definir los alcances y límites del proyecto actual.
# Rol: Documento de alcance del framework.
# ──────────────────────────────────────────────────────────────────────

# Matriz de Alcance (Scope YES/NO)

Este documento detalla qué componentes y capacidades entran dentro de la versión actual del framework y cuáles quedan expresamente fuera de alcance.

---

## Sí (En Alcance)

*   **Modelado Metodológico Completo:** Estructura de directorios, roles, y flujos funcionales del framework en fase pre-code.
*   **Gobernanza de Calidad (Gates):** Procedimientos manuales de validación funcional e interfaces documentales para la aprobación humana.
*   **Gestión de Perfiles Editoriales:** Definición teórica de perfiles configurables (persona, profesional independiente, empleado experto, proyecto, marca, empresa u organización).
*   **Caso de Uso Heredado:** Preservación del caso práctico de logística como plantilla de aprendizaje e histórico.
*   **Trazabilidad Operativa:** Formatos de captura de inputs (`input/`) y registro de trazas de desarrollo (`output/trace/`).

---

## No (Fuera de Alcance)

*   **Publicación Automática sin Revisión:** Prohibición absoluta de publicar directamente en LinkedIn de forma autónoma.
*   **Conexión Directa a APIs Externas:** No se integran servicios como la API de LinkedIn, Make, Zapier u otros automatizadores en esta fase.
*   **Scraping de Datos:** Exclusión de sistemas automáticos para leer interacciones, feeds o perfiles de terceros en LinkedIn.
*   **Desarrollo de Software SaaS:** El proyecto es un framework metodológico/operativo local, no una plataforma multiusuario basada en la nube.
*   **Métricas Avanzadas en Vivo:** No se conectan dashboards de visualización de datos en tiempo real de LinkedIn.
*   **Sistema Multiagente Complejo (Día 1):** No se diseñarán flujos de orquestación autónomos complejos con múltiples agentes de IA trabajando en paralelo. El control es puramente documental y secuencial.
