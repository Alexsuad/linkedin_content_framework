# File: docs/core/identity_contract.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Establecer las bases de identidad y límites del framework.
# Rol: Contrato canónico de diseño conceptual.
# ──────────────────────────────────────────────────────────────────────

# Contrato de Identidad (Identity Contract)

Este documento define la naturaleza del proyecto y establece límites de diseño estrictos para evitar derivas conceptuales o acoplamientos innecesarios.

---

## 1. Declaración de Identidad

Este proyecto es:
*   **Un Framework para LinkedIn:** Diseñado específicamente para optimizar la preparación y validación de publicaciones en LinkedIn como canal principal de comunicación profesional.
*   **Un Sistema Flexible y Parametrizable:** El núcleo del framework está desacoplado de cualquier sector industrial o perfil personal.
*   **Un Motor de Producción Controlada:** Su objetivo es garantizar la trazabilidad, orden y control de calidad de las publicaciones.

---

## 2. Límites Conceptuales Innegociables

### A. Sector-Agnóstico (No específico para Logística)
*   **El canal es LinkedIn.**
*   La logística, el transporte u otros sectores específicos son **casos de uso** o perfiles editoriales configurados en el framework, no la identidad del motor.
*   Las reglas de redacción y selección temática generales no deben asumir de forma fija que el negocio pertenece al sector logístico.

### B. Perfil-Agnóstico (No exclusivo para Alex)
*   El framework opera sobre perfiles editoriales variables.
*   Las menciones a "Alex" en la gobernanza heredada se abstraen como **Aprobador Humano / Propietario del Perfil Editorial**.
*   El sistema debe poder configurarse para profesionales independientes, empleados expertos, marcas, proyectos colectivos u organizaciones.

### C. No es un Publicador Autónomo (Revisión Humana Obligatoria)
*   Este framework **no publica de forma autónoma en LinkedIn**.
*   No interactúa directamente con APIs de publicación de forma desatendida.
*   Cada pieza de contenido debe pasar obligatoriamente por un **gate de validación humana** (el Aprobador) antes de salir.

---

## 3. Síntesis Operativa

`linkedin_content_framework` es una herramienta metodológica para:
1.  **Capturar** señales reales de negocio (fricciones, aprendizajes).
2.  **Estructurar** y redactar borradores aplicando la Regla Madre (`Problema -> Fricción -> Solución -> Impacto`).
3.  **Auditar** la calidad editorial, la claridad del mensaje, el formato y la alineación estratégica de forma interna.
4.  **Someter** el resultado a la confirmación de un Aprobador Humano responsable del perfil.
5.  **Aprender** del feedback para retroalimentar la base de conocimientos.
