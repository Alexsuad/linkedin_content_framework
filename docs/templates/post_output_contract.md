<!-- File: docs/templates/post_output_contract.md -->

# Contrato de salida de publicación

## Propósito
Definir qué debe entregar el sistema cuando genera una publicación candidata para LinkedIn o para otro canal futuro configurable. 

Este contrato no constituye una publicación final lista para copiar y pegar de forma aislada. Define el paquete de salida editorial-operativa mínimo necesario para que una pieza candidata pueda ser auditada, evaluada por los gates internos, aprobada por el responsable del perfil, programada o devuelta para corrección.

---

## 1. Identificación de la pieza
*   **post_id:** [ID único de la publicación, ej: POST-2026-0045]
*   **fecha_creacion:** [Fecha de generación del borrador, AAAA-MM-DD]
*   **canal:** [LinkedIn u otro canal de publicación configurable]
*   **perfil_editorial:** [Referencia al perfil de configuración, ej: linkedin_autonomo_b2b]
*   **caso_de_uso:** [Caso de uso o sector de aplicación del contenido]
*   **tipo_publicacion:** [Ej: Post de texto, Carrusel visual, Storytelling]
*   **estado_actual:** [Estado operativo en el pipeline del post]

## 2. Entrada usada
*   **input_signal_id:** [ID único de la señal real de origen en input/, ej: SIG-2026-0012]
*   **weekly_intake_id:** [ID del intake semanal de planificación, ej: WEEK-2026-22]
*   **fuente_principal:** [Origen del dato: Sesión de alineación, caso práctico, nota operativa, profesional o comercial]
*   **nivel_confianza_fuente:** [Bajo, Medio, Alto. Determina la necesidad de verificación adicional]
*   **requiere_anonimizacion:** [Sí / No. Indica si se deben proteger nombres u otros datos sensibles]

## 3. Objetivo editorial
*   **objetivo_principal:** [Qué busca lograr el post en la audiencia, ej: Posicionamiento técnico]
*   **audiencia_objetivo:** [Audiencia objetivo o perfil profesional de destino en LinkedIn]
*   **pilar_editorial:** [Pilar narrativo al que se asocia, ej: Orden operativo]
*   **mensaje_central:** [La idea o enseñanza principal que debe retener el lector]
*   **tipo_de_conversacion_esperada:** [Ej: interacciones cualificadas, respuestas, guardados, visitas al perfil, mensajes privados u otra acción esperada según el perfil]

## 4. Contenido generado
*   **hook:** [Línea o líneas iniciales del post destinadas a captar la atención en el feed]
*   **cuerpo_publicacion:** [Desarrollo de la idea aplicando la estructura de fricción y solución]
*   **cierre:** [Reflexión final o resumen breve]
*   **cta:** [Llamada a la acción coherente, ej: Pregunta abierta o invitación a debatir]
*   **hashtags_opcionales:** [Hashtags de marca o temáticos autorizados]
*   **variantes_si_aplica:** [Variantes alternativas de hook o cierre si el perfil lo requiere]

## 5. Formato
*   **formato_sugerido:** [TIPO_1 (Carrusel), TIPO_2 (Post de texto directo), TIPO_3 (Storytelling) u otros futuros]
*   **motivo_formato:** [Justificación editorial del formato elegido para esta idea]
*   **requiere_imagen:** [Sí / No. Indica si se requiere una imagen de soporte]
*   **requiere_carrusel:** [Sí / No. Indica si se requiere el diseño de un guion de diapositivas]
*   **numero_slides_si_aplica:** [Número estimado de slides en caso de ser carrusel]

## 6. Capa visual si aplica
*   **descripcion_visual:** [Detalle conceptual del diseño, gráficos, colores o diagramas necesarios]
*   **objetivo_visual:** [Qué función cumple el soporte gráfico, ej: Facilitar lectura paso a paso]
*   **riesgo_visual:** [Bajo, Medio, Alto. Evaluación de sobrecarga de texto o desalineación visual]
*   **estado_visual:** [Pendiente de diseño, En producción visual, Aprobado visualmente]
*   **observaciones_visuales:** [Directrices específicas para el diseñador o la skill de generación gráfica]

## 7. Auditoría interna
*   **resultado_brief_sufficiency_gate:** [Aprobado / Bloqueado / Excepcionado]
*   **resultado_editorial_audit_gate:** [Aprobado / Bloqueado / Ajustes menores]
*   **resultado_claims_and_risk_policy:** [Aprobado (Bajo Riesgo) / Bloqueado / Requiere revisión]
*   **riesgo_general:** [Bajo, Medio, Alto]
*   **estado_recomendado:** [Clasificación de salida del sistema, ej: READY_TO_APPROVE]

## 8. Aprobación humana compacta
*   **requiere_aprobacion_humana:** [Sí / No. Por defecto Sí según la decisión constitucional]
*   **motivo_aprobacion:** [Razón por la que se somete al gate humano, ej: Flujo regular o tema sensible]
*   **accion_sugerida:** [Aprobar publicación, Rechazar para edición, Descartar]
*   **aprobador_sugerido:** [Nombre del responsable del perfil editorial]
*   **fecha_limite_revision:** [Fecha y hora límite sugerida para la revisión, AAAA-MM-DD HH:MM]

## 9. Decisión final
*   **decision:** [Aprobado / Devuelto para ajustes / Rechazado y Descartado]
*   **aprobado_por:** [Aprobación o confirmación del responsable del perfil]
*   **fecha_decision:** [Fecha y hora del registro de la decisión, AAAA-MM-DD HH:MM]
*   **motivo_rechazo_si_aplica:** [Comentarios específicos del aprobador si la pieza fue devuelta]
*   **siguiente_accion:** [Ej: Programar publicación, Volver al redactor con anotaciones]

---

## 10. Criterio mínimo de completitud
El paquete de salida editorial-operativa se considera completo y apto para ser evaluado por los auditores si cumple estrictamente con:
1.  Todos los campos de las Secciones 1, 2, 3 y 5 completamente rellenados.
2.  El contenido de la Sección 4 redactado en su totalidad (no se admiten placeholders ni texto incompleto).
3.  Si el formato sugerido es TIPO_1 (Carrusel), la Sección 6 debe detallar la descripción de cada slide o el guion visual respectivo.
4.  La traza de la señal de origen (`input_signal_id`) debe existir y estar activa en el repositorio.
5.  Cualquier borrador que no cumpla con estos mínimos será clasificado automáticamente como `BLOCKED_BY_FORMAT_RISK` y devuelto al redactor antes de entrar en los gates de gobernanza.
