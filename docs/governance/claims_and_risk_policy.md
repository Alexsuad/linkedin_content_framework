<!-- File: docs/governance/claims_and_risk_policy.md -->

# Política de claims, reputación y riesgo

## Propósito
Definir qué afirmaciones (claims) puede hacer el sistema de contenido, qué debe evitar y cuándo debe bloquear una publicación candidata debido a la existencia de riesgos reputacionales, legales, comerciales o de pérdida de confianza de la audiencia.

Esta política actúa como un marco normativo para asegurar la veracidad de los mensajes y evitar la propagación de desinformación, promesas comerciales vacías o filtración de datos sensibles del emisor, perfil profesional, proyecto, organización representada o sus clientes, si aplica.

---

## 1. Principio general
La gobernanza del contenido se rige por el siguiente principio operativo innegociable del repositorio:

> **“No publicar sin gates, trazabilidad y aprobación según el nivel de autonomía definido.”**

Bajo esta directriz, queda terminantemente prohibido inventar resultados, clientes, cifras, retornos de inversión (ROI), testimonios de éxito, mejoras operativas o casos prácticos del emisor, perfil, proyecto u organización. La autoridad en LinkedIn se construye sobre hechos y experiencias, aprendizajes o fricciones verídicas, y cualquier desvío de la verdad fáctica es motivo directo de descarte del contenido.

---

## 2. Claims permitidos
El sistema puede generar y dar paso a publicaciones que contengan:
-   Afirmaciones basadas directamente en la experiencia de campo real del emisor, perfil profesional, proyecto, organización representada o cliente, si aplica, debidamente documentada en la señal de origen.
-   Patrones recurrentes y problemáticas comunes observadas en el sector, presentadas de forma didáctica.
-   Hipótesis y opiniones profesionales presentadas explícitamente bajo fórmulas como: *"En nuestra opinión"*, *"Consideramos como hipótesis"*, o *"Según nuestra experiencia"*.
-   Explicación de beneficios potenciales y mejoras lógicas sin presentarlos como una promesa de resultado absoluto.
-   Análisis de problemas frecuentes del día a día de profesionales, equipos, proyectos u organizaciones y recomendaciones sobre cómo abordarlos de forma estructurada.

---

## 3. Claims restringidos
Requieren un análisis y justificación detallada en la salida del gate (o pasarán a revisión por excepción) las siguientes afirmaciones:
-   Mención de porcentajes de ahorro o mejora en la eficiencia que no estén respaldados por mediciones internas contrastables.
-   Declaraciones de reducción de horas de trabajo administrativo que no hayan sido validadas mediante dry runs o auditorías previas.
-   Resultados o hitos logrados por clientes del emisor u organización representada que no cuenten con una autorización de comunicación explícita.
-   Comparaciones directas o agresivas frente a competidores específicos o metodologías alternativas del mercado.
-   Promesas de retorno de inversión (ROI) ligadas a un marco temporal cerrado o condiciones variables del mercado.
-   Afirmaciones absolutas o totalizadoras que no admitan matices lógicos en el contexto real del perfil, proyecto u organización.

---

## 4. Claims prohibidos
Quedan estrictamente prohibidos y causarán el bloqueo inmediato de la publicación los siguientes contenidos:
-   Inventar o falsificar nombres de clientes, marcas o identidades comerciales.
-   Inventar casos prácticos de implantación técnica o situaciones, experiencias o casos ficticios presentados como reales.
-   Inventar cifras de facturación, márgenes de ahorro o rendimientos del sistema.
-   Prometer resultados absolutos, no demostrados, libres de riesgo o sin esfuerzo operativo.
-   Exponer datos confidenciales, secretos profesionales, comerciales o internos del emisor, equipo, proyecto, organización o cliente, propiedad intelectual o contraseñas del cliente o de terceros.
-   Utilizar nombres propios de terceras personas o logotipos corporativos sin consentimiento expreso y por escrito.
-   Asegurar que un flujo, script o sistema ha sido probado y validado con éxito en la operación real si no existe evidencia que lo demuestre.

---

## 5. Política de casos reales
Para ilustrar problemas operativos a través de situaciones de negocio vividas en la realidad se deben seguir estas reglas:
-   **Qué se puede contar:** La naturaleza del fallo operativo, el cuello de botella organizativo, la fricción del equipo y la lógica funcional empleada para resolverlo.
-   **Qué debe anonimizarse:** Nombres de personas, nombres de empresas clientes, marcas comerciales de terceros, ubicaciones geográficas precisas e importes de facturación detallados.
-   **Detalles a eliminar:** Elementos identificativos muy particulares que permitan a un competidor o lector deducir la identidad del cliente involucrado.
-   **Mantener el valor:** El valor pedagógico del caso debe centrarse en la mecánica del error y el método de orden/solución aplicado, abstrayendo los datos de identidad.

---

## 6. Riesgos reputacionales
El auditor debe monitorizar que la redacción no degrade la imagen de marca de la cuenta. Se debe evitar:
-   **Sonar a "IA hype":** Evitar el uso de jerga superflua sobre disrupción tecnológica, automatizaciones mágicas y promesas infladas típicas de la burbuja tecnológica de IA.
-   **Sonar a "Gurú":** Evitar actitudes arrogantes de posesión de la verdad absoluta, lecciones morales de éxito y lenguaje imperativo ("Debes hacer esto hoy").
-   **Sonar a "Proveedor de scripts":** No centrar la narrativa en la programación, APIs o detalles mecánicos de código en lugar de en el valor organizativo y la solución del negocio.
-   **Sonar a "Consultor genérico":** Evitar rodeos innecesarios o palabrería de manual corporativo sin anclaje práctico en el día a día.
-   **Vender herramientas en vez de resultados:** No promocionar el uso de un software concreto como el fin en sí mismo de la autoridad de marca.
-   **Atacar competidores:** Evitar descalificaciones destructivas hacia marcas competidoras directas.
-   **Prometer más de lo demostrado:** Abstenerse de sobrepasar la evidencia empírica contenida en la señal de origen de la pieza.

---

## 7. Estados posibles
La publicación será clasificada bajo uno de los siguientes niveles de riesgo:

*   `RISK_LOW`: La pieza cumple perfectamente con las directrices de veracidad, no contiene claims sensibles ni datos de riesgo y es apta para continuar el flujo.
*   `RISK_MEDIUM`: Contiene afirmaciones de mejora operativa o porcentajes que requieren ser matizados o justificados con notas de evidencia en la traza.
*   `NEEDS_HUMAN_REVIEW`: Post que trata temas regulatorios complejos o menciones de resultados estratégicos que requieren una validación expresa del aprobador humano.
*   `BLOCKED_BY_CLAIM_RISK`: Contiene promesas falsas, claims exagerados o declaraciones de ROI inviables.
*   `BLOCKED_BY_CONFIDENTIALITY`: Se detecta riesgo de exposición directa de datos confidenciales de clientes o secretos profesionales, internos o de negocio.
*   `BLOCKED_BY_REPUTATION_RISK`: El tono del post expone la reputación de la marca, suena a gurú o vulnera gravemente el estilo estratégico de la cuenta.

---

## 8. Salida de la política
El reporte generado por este gate de riesgos debe estructurarse del siguiente modo:
*   **nivel_riesgo:** [RISK_LOW, RISK_MEDIUM, NEEDS_HUMAN_REVIEW, BLOCKED_BY_CLAIM_RISK, BLOCKED_BY_CONFIDENTIALITY o BLOCKED_BY_REPUTATION_RISK]
*   **claim_detectado:** [La frase o afirmación específica que activó la política, si aplica]
*   **motivo:** [Explicación detallada del riesgo detectado]
*   **accion_recomendada:** [Bloquear post, eliminar claim, reformular con matiz o escalar para arbitraje humano]
*   **versión_segura_sugerida:** [Propuesta de redacción alternativa de la frase o claim que mitigue el riesgo]

---

## 9. Relación con aprobación humana compacta
La salida de este gate determina el camino de aprobación final del post:
-   **Riesgo Bajo (`RISK_LOW`):** El post avanza directamente hacia el paquete de aprobación compacta, donde el aprobador humano puede firmarlo de forma ágil y masiva junto a otros posts de la semana.
-   **Riesgo Medio o Alto (`RISK_MEDIUM`, `NEEDS_HUMAN_REVIEW`):** El post se separa del lote y se escala como caso de excepción, obligando a una revisión línea por línea en el gate humano o requiriendo la modificación de los claims detectados antes de permitir su firma.
