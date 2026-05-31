<!-- File: docs/use_cases/linkedin_autonomo_b2b/visual_rules.md -->

# Reglas visuales — LinkedIn autónomo B2B

## Propósito
Definir cuándo usar imágenes, carruseles u otros elementos gráficos para las publicaciones del perfil `linkedin_autonomo_b2b`. Este documento establece pautas objetivas para asegurar la legibilidad, el impacto visual y la coherencia estética del contenido en LinkedIn.

---

## 1. Principio visual
El uso de soportes visuales en este perfil responde a una ley de funcionalidad:
-   La imagen o el carrusel debe mejorar de forma directa la comprensión del mensaje, aumentar la autoridad técnica o simplificar la visualización de un flujo complejo.
-   Queda prohibido el uso de recursos visuales con propósitos meramente decorativos o estéticos que distraigan al lector del núcleo del copy.

---

## 2. Cuándo usar post sin imagen
El formato de texto simple (sin imagen) es la opción preferente en los siguientes escenarios:
-   Cuando el mensaje es directo, conceptual y no requiere datos estructurados de soporte.
-   Cuando la idea se comprende perfectamente solo a través de la lectura del copy.
-   Para publicaciones basadas en reflexiones cortas, opiniones profesionales breves o descripciones rápidas de una escena cotidiana de oficina.
-   Cuando no existe una estructura lógica o proceso visual que justifique el uso de gráficos.

---

## 3. Cuándo usar carrusel
El formato de carrusel (documento PDF multipágina en LinkedIn) es ideal para desglosar ideas estructuradas:
-   **Procesos secuenciales:** Pasos ordenados para realizar una optimización.
-   **Esquemas de "Antes y Después":** Visualización del estado desordenado frente al estado con sistema.
-   **Checklists operativos:** Puntos clave para verificar el estado de un departamento.
-   **Comparaciones de alternativas:** Matrices donde se evalúan los pros y contras de dos enfoques.
-   **Marcos de decisión:** Flujogramas lógicos de toma de decisiones.
-   **Errores y correcciones:** Mostrar de forma visual una práctica incorrecta y su correspondiente alternativa de orden.
-   **Secuencias explicativas:** Temas complejos que requieren división en diapositivas sencillas.

---

## 4. Cuándo usar imagen simple
Se empleará una única imagen adjunta al post únicamente cuando:
-   Refuerce de manera instantánea y directa un concepto del texto (ej. un gráfico de control simple).
-   Acompañe la explicación técnica (ej. una captura de pantalla de un panel de control anonimizado).
-   La idea a transmitir se resuma en un único impacto visual que no amerite el despliegue de múltiples slides.
-   El gráfico no compita con la lectura del texto principal.

---

## 5. Riesgos visuales
Para proteger la credibilidad del perfil, el auditor visual debe descartar las piezas que presenten:
-   **Imágenes de stock genéricas:** Fotografías impersonales de personas sonriendo en oficinas limpias o apretones de manos corporativos.
-   **Imágenes generadas por IA artificiales:** Diseños en 3D saturados de color, rostros con deformaciones típicas de algoritmos antiguos o gráficos fantasiosos.
-   **Exceso de texto en las slides:** Carruseles con párrafos densos que dificulten la lectura en pantallas móviles.
-   **Estética de gurú:** Diseños con tipografías gigantescas y colores chillones enfocados en la autopromoción del autor.
-   **Diseño corporativo frío:** Gráficos institucionales complejos de entender que carezcan de dinamismo.
-   **Promesas visuales exageradas:** Diagramas que prometan soluciones universales simplistas.
-   **Gráficos sin fuente o procedencia:** Datos numéricos mostrados en barras o sectores sin justificación.

---

## 6. Regla para TIPO 1, TIPO 2 y TIPO 3
Los formatos configurables del framework se asocian de forma regular con las siguientes reglas visuales:
-   **TIPO 1 (Carrusel):** Se estructura siempre mediante un guion visual detallado slide por slide. Cada slide debe contener una sola idea y una jerarquía tipográfica limpia.
-   **TIPO 2 (Texto simple):** Excluye por defecto las imágenes para potenciar la fuerza de la palabra directa.
-   **TIPO 3 (Storytelling):** Permite el uso de texto simple o, excepcionalmente, de una imagen muy discreta (ej. captura anonimizada del caso) si aporta veracidad histórica al relato.

---

## 7. Auditoría visual mínima
Cada entregable visual debe ser evaluado internamente bajo los siguientes parámetros lógicos:
1.  **Legibilidad:** ¿El texto es legible desde un teléfono móvil sin necesidad de zoom?
2.  **Jerarquía:** ¿Se distingue claramente el título del slide del texto complementario?
3.  **Coherencia con la voz:** ¿Los colores y estilos gráficos transmiten sobriedad y profesionalismo?
4.  **Utilidad:** ¿El gráfico aporta claridad al proceso explicado en el copy?
5.  **Riesgo:** ¿Evita elementos de stock o estéticas de venta agresiva?
6.  **Consistencia visual:** ¿Se mantiene una paleta de colores coherente en todo el lote?

---

## 8. Estados visuales posibles
El auditor asignará uno de los siguientes estados visuales en el reporte:
-   `VISUAL_NOT_REQUIRED`: La publicación está configurada como texto simple y no requiere soporte gráfico.
-   `VISUAL_READY`: El recurso visual o carrusel cumple con todas las reglas y está listo para publicación.
-   `VISUAL_NEEDS_EDIT`: Se requieren modificaciones menores (ej. corregir un error ortográfico en una diapositiva o reducir texto).
-   `BLOCKED_BY_VISUAL_RISK`: El diseño infringe las políticas de calidad (imagen de IA de mala calidad, datos sin fuente o estética gurú).

---

## 9. Criterio de completitud
Una pieza visual se considera lista para pasar a la aprobación humana compacta cuando:
1.  Ha sido calificada con el estado `VISUAL_READY` o `VISUAL_NOT_REQUIRED`.
2.  El guion de slides está completo y revisado (si es un carrusel).
3.  Se adjuntan los archivos o imágenes correspondientes en la traza en su ruta final.
