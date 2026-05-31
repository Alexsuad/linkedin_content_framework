<!-- File: docs/governance/checkpoints.md -->

# Checkpoints de avance del proyecto

## Propósito

Este documento define los criterios mínimos para considerar cerrada una fase o permitir el avance a la siguiente.

Su función es evitar avances prematuros, especialmente hacia agentes, skills, workflows, CLI, MCP, APIs o publicación automática sin haber cerrado antes la capa editorial-operativa y los gates mínimos.

## Principio base

El proyecto avanza bajo esta regla:

IA propone. Python verifica. Humano aprueba. Git registra.

Ningún avance importante debe considerarse cerrado solo porque un agente diga que terminó. Debe existir evidencia documental, auditoría en verde y revisión humana.

---

## Checkpoint 0 — Base del repositorio

### Para considerarlo cerrado debe existir:

- estructura base del repositorio;
- `README.md`;
- `AGENTS.md`;
- `MIGRATION_NOTES.md`;
- `docs/core/identity_contract.md`;
- `docs/core/vision.md`;
- `docs/core/scope_yes_no.md`;
- `docs/core/principles.md`;
- `.gitignore`;
- `.gitattributes`;
- `tools/audit_precode_repo.py`;
- auditoría en verde;
- commit inicial.

### Estado actual

Cerrado.

---

## Checkpoint 1 — Plan de implementación

### Para considerarlo cerrado debe existir:

- `docs/implementation_plan.md`;
- fases documentadas;
- entregables por fase;
- tareas numeradas;
- riesgos;
- reglas de no avance;
- criterio de cierre por fase;
- auditoría en verde;
- commit específico.

### Estado actual

Cerrado.

---

## Checkpoint 2 — Templates de intake

### Para considerarlo cerrado debe existir:

- `docs/templates/client_intake_template.md`;
- `docs/templates/voice_and_narrative_template.md`;
- `docs/templates/weekly_content_intake_template.md`;
- `docs/templates/input_signal_template.md`;
- auditoría en verde;
- commit específico.

### Estado actual

Cerrado.

---

## Checkpoint 3 — Contratos y Gates

### Para considerarlo cerrado debe existir:

- `docs/templates/post_output_contract.md`;
- `docs/governance/brief_sufficiency_gate.md`;
- `docs/governance/editorial_audit_gate.md`;
- `docs/governance/claims_and_risk_policy.md`;
- criterios claros de aprobación, devolución, bloqueo y riesgo;
- auditoría en verde;
- revisión humana;
- commit específico.

### Estado actual

Pendiente.

---

## Checkpoint 4 — Perfil inicial autónomo B2B

### Para considerarlo cerrado debe existir:

- `docs/use_cases/linkedin_autonomo_b2b/profile_config.md`;
- `docs/use_cases/linkedin_autonomo_b2b/voice_and_style.md`;
- `docs/use_cases/linkedin_autonomo_b2b/visual_rules.md`;
- `docs/use_cases/linkedin_autonomo_b2b/examples_good_bad.md`;
- separación clara entre perfil, canal y sector;
- auditoría en verde;
- revisión humana;
- commit específico.

### Estado actual

Pendiente.

---

## Checkpoint 5 — Arquitectura funcional

### Para considerarlo cerrado debe existir:

- `docs/architecture/functional_specialists_matrix.md`;
- inclusión explícita del Especialista de Intake y Acompañamiento del Cliente;
- mapeo de responsabilidades funcionales;
- decisión inicial sobre agente, skill, gate, regla, workflow o fase futura;
- auditoría en verde;
- revisión humana;
- commit específico.

### Estado actual

Pendiente.

---

## Checkpoint 6 — Dry runs manuales

### Para considerarlo cerrado debe existir:

- dry run de post simple TIPO 2;
- dry run de carrusel TIPO 1;
- input usado;
- salida generada;
- revisión editorial;
- revisión de claims;
- revisión visual cuando aplique;
- aprobación humana;
- traza guardada.

### Estado actual

Pendiente.

---

## Checkpoint 7 — Arquitectura agéntica mínima

### No se puede iniciar hasta que estén cerrados:

- Checkpoint 3 — Contratos y Gates;
- Checkpoint 4 — Perfil inicial autónomo B2B;
- Checkpoint 5 — Arquitectura funcional;
- Checkpoint 6 — Dry runs manuales.

### Para considerarlo cerrado debe existir:

- `docs/architecture/agent_skill_gate_matrix.md`;
- `docs/architecture/minimum_agent_architecture.md`;
- `docs/skills/skills_catalog.md`;
- `docs/workflows/workflows_catalog.md`;
- decisión explícita de qué será agente, skill, gate, regla, workflow o script determinista.

### Estado actual

Bloqueado.

---

## Checkpoint 8 — CLI, MCP e integraciones

### No se puede iniciar hasta que estén cerrados:

- arquitectura agéntica mínima;
- gates documentados;
- dry runs manuales;
- revisión humana;
- auditoría determinista ampliada.

### Fuera de alcance por ahora:

- API de LinkedIn;
- MCP;
- publicación automática;
- automatización de comentarios;
- analítica avanzada;
- aprendizaje automático basado en métricas.

### Estado actual

Bloqueado.

---

## Reglas de bloqueo

El avance debe bloquearse si ocurre cualquiera de estos casos:

- se intenta crear agentes antes de cerrar gates y dry runs;
- se intenta crear skills antes de mapear responsabilidades funcionales;
- se intenta publicar automáticamente antes de validar revisión humana;
- se intenta mover logística al núcleo general;
- se intenta convertir una frecuencia específica en regla universal del framework;
- se intenta trabajar más de un bloque a la vez sin aprobación explícitamente;
- se intenta modificar `Automatizacion_linkedin`;
- la auditoría determinista falla.

## Regla de cierre de tarea

Toda tarea debe cerrar con:

1. archivos creados o modificados;
2. resultado de auditoría;
3. resultado de `git status --short`;
4. confirmación de restricciones;
5. recomendación del siguiente paso;
6. commit humano posterior si corresponde.
