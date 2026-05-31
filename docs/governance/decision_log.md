<!-- File: docs/governance/decision_log.md -->

# Registro de Decisiones

Este documento registra de forma histórica, estable y secuencial las decisiones metodológicas, de gobernanza y de diseño técnico adoptadas en el repositorio. Su propósito es garantizar la trazabilidad del desarrollo y evitar derivas conceptuales o acoplamientos innecesarios.

---

## Decisión 001: Arquitectura Híbrida de Gobernanza y Control de Publicación

- **Fecha:** 2026-05-31
- **Estado:** Aprobada
- **Contexto:** Se requiere establecer un balance claro entre el poder creativo y de redacción de los sistemas de Inteligencia Artificial y la responsabilidad final sobre la reputación y veracidad del contenido publicado en los canales del cliente (LinkedIn).
- **Decisión:** Adoptar una arquitectura de gobernanza híbrida regida por el principio constitucional: *“IA propone. Python verifica. Humano aprueba. Git registra”*. De manera explícita, se define el siguiente principio operativo innegociable:
  
  > **“No publicar sin gates, trazabilidad y aprobación según el nivel de autonomía definido.”**
  
  Queda prohibido cualquier tipo de publicación autónoma, automática o desatendida en LinkedIn. Todo contenido final debe pasar por una fase de auditoría interna (agéntica y determinista) y requerir la firma y confirmación explícita del aprobador humano.
- **Consecuencias:** 
  - Todo borrador debe ir acompañado de una traza documental completa desde la señal de origen hasta su validación.
  - El sistema de automatización debe diseñar gates técnicos infranqueables que no permitan la salida de información sin la firma digital o de control del aprobador humano.

---

## Decisión 002: Desacoplamiento de Sector y Perfil Editorial respecto al Núcleo del Framework

- **Fecha:** 2026-05-31
- **Estado:** Aprobada
- **Contexto:** El análisis del repositorio de origen (`Automatizacion_linkedin`) reveló un acoplamiento estricto a las particularidades de un único sector industrial (logística y transporte) y a una persona individual (Alex). Esto limita la escalabilidad y reutilización del sistema para otros clientes.
- **Decisión:** Mantener una separación conceptual estricta y absoluta entre el núcleo general del framework (`docs/core/`, `docs/architecture/` y `docs/governance/`) y los perfiles de uso. Los documentos generales del Core deben ser agnósticos respecto al sector y al aprobador humano final. Las particularidades sobre tonos, temáticas y canales pertenecen exclusivamente a las plantillas y a las carpetas de perfiles configurados en los casos de uso (`docs/use_cases/`).
- **Consecuencias:**
  - El script de verificación automática del repositorio (`tools/audit_precode_repo.py`) auditará y bloqueará cualquier intento de introducir términos relacionados con el caso heredado de logística o el aprobador de prueba en las carpetas principales del núcleo.
  - La gobernanza y los gates de calidad deben redactarse en términos funcionales y genéricos adaptables mediante archivos de configuración locales.

---

## Decisión 003: Enfoque Pre-code y Priorización del Pipeline Manual

- **Fecha:** 2026-05-31
- **Estado:** Aprobada
- **Contexto:** Existe una tendencia natural a iniciar la codificación de agentes de IA, clases en Python, conectores y scripts de automatización de forma prematura. Esto incrementa los costes de desarrollo, la complejidad y el riesgo de diseñar software sobre procesos manuales inestables o mal definidos.
- **Decisión:** Mantener el repositorio bajo la fase pre-code durante toda la definición del pipeline documental de intake, gobernanza y arquitectura funcional (Fase 1 y Fase 3 del plan). No se permite escribir código de software de la aplicación, crear agentes de IA, definir scripts de ejecución o instalar librerías externas hasta haber completado los checkpoints correspondientes y haber validado manualmente el proceso mediante simulaciones controladas (Dry Runs - Fase 5).
- **Consecuencias:**
  - Toda la Fase 1 y la Fase 3 se centrarán en la especificación funcional y el diseño de plantillas en formato Markdown.
  - La única excepción de desarrollo de código permitida es la extensión del script de verificación determinista local (`tools/audit_precode_repo.py`) para validar estructuralmente los documentos de gobernanza antes de pasar a la definición técnica.
