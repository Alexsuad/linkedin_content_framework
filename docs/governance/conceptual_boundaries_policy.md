<!-- File: docs/governance/conceptual_boundaries_policy.md -->

# Política de fronteras conceptuales del framework

## 1. Propósito

Este documento define las fronteras conceptuales que deben respetarse dentro de `linkedin_content_framework` para evitar contaminación entre el núcleo general del framework, el canal LinkedIn, los perfiles editoriales, los casos de uso, los sectores y las configuraciones temporales.

Su objetivo principal es impedir que un concepto específico de un perfil, sector u objetivo comunicativo se convierta accidentalmente en una regla universal del sistema.

Esta política no busca eliminar términos como `empresa`, `cliente`, `B2B`, `oferta`, `comercial`, `empleabilidad`, `reclutador`, `CV`, `institución` o `comunidad`.

La regla correcta es contextual:

> Un concepto específico puede existir dentro del framework, pero no puede convertirse en identidad universal del núcleo.

Por tanto, los conceptos específicos deben vivir en su sede documental correcta: perfil editorial, caso de uso, sector, ejemplo, configuración o referencia histórica.

---

## 2. Capas documentales del framework

El framework se organiza conceptualmente en capas. Cada capa tiene un nivel distinto de generalidad y no debe asumir responsabilidades que pertenecen a otra.

### 2.1 Núcleo universal

Incluye principalmente:

- `docs/core/`
- reglas constitucionales del framework;
- principios generales;
- contrato de identidad;
- alcance global;
- visión del sistema.

El núcleo solo debe contener conceptos válidos para cualquier perfil editorial.

Puede hablar de:

- perfil editorial;
- emisor;
- audiencia objetivo;
- objetivo comunicativo;
- señal real;
- trazabilidad;
- gates;
- validación;
- riesgo;
- formato;
- canal;
- configuración;
- aprendizaje.

No debe asumir como universal:

- empresa;
- cliente;
- comprador;
- lead;
- oferta comercial;
- reclutador;
- CV;
- logística;
- autónomo B2B;
- frecuencia fija;
- sector específico;
- objetivo único de venta, empleo, autoridad o comunidad.

### 2.2 Capa de canal

Incluye las reglas derivadas de que el canal principal es LinkedIn.

Puede hablar de:

- publicaciones;
- feed;
- lectura móvil;
- hook;
- CTA;
- comentarios;
- mensajes privados;
- carruseles;
- formato LinkedIn;
- interacción cualificada.

No debe convertir un tipo de perfil de LinkedIn en regla universal.

LinkedIn es el canal.  
No es el perfil.  
No es el sector.  
No es el objetivo comunicativo único.

### 2.3 Capa de perfiles editoriales

Define quién comunica.

Ejemplos de perfiles editoriales:

- profesional independiente;
- autónomo B2B;
- empresa;
- microempresa;
- empleado profesional;
- persona natural en búsqueda de empleo;
- marca corporativa;
- institución;
- organización;
- comunidad;
- proyecto educativo.

Cada perfil puede tener lenguaje propio, objetivos propios, audiencia propia y restricciones propias.

Estos conceptos no deben subir al núcleo como reglas generales.

### 2.4 Capa de casos de uso

Define para qué se usa el framework en un contexto concreto.

Ejemplos:

- generar conversaciones comerciales;
- posicionar autoridad profesional;
- mejorar visibilidad laboral;
- explicar proyectos;
- atraer talento;
- comunicar impacto institucional;
- educar a una comunidad;
- documentar aprendizajes;
- activar interacción cualificada.

Un caso de uso puede tener reglas específicas, pero esas reglas no deben convertirse en reglas universales del framework.

### 2.5 Capa sectorial

Define el sector, industria o contexto temático.

Ejemplos:

- logística;
- tecnología;
- educación;
- salud;
- servicios profesionales;
- comercio exterior;
- cultura;
- sector público.

Los sectores son configuraciones o casos de aplicación.  
Ningún sector debe ser tratado como identidad general del framework.

### 2.6 Capa operativa o temporal

Define decisiones de ejecución en un periodo concreto.

Ejemplos:

- frecuencia semanal;
- campañas activas;
- temas de la semana;
- señales disponibles;
- publicaciones candidatas;
- riesgos temporales;
- prioridades editoriales del periodo.

Estas decisiones no deben convertirse en reglas permanentes del núcleo.

---

## 3. Regla central de frontera conceptual

La regla principal de esta política es:

> Ningún concepto específico de perfil, sector, audiencia, objetivo o caso de uso puede actuar como identidad universal del framework.

Esto significa que una palabra no es problemática por existir.  
Es problemática cuando ocupa una sede que no le corresponde.

La evaluación de un término debe considerar tres factores:

1. **Ruta del archivo:** dónde aparece.
2. **Concepto detectado:** qué término o idea se está usando.
3. **Función contextual:** cómo está funcionando dentro de la frase.

---

## 4. Funciones contextuales permitidas y no permitidas

### 4.1 Funciones permitidas

Un concepto específico puede aparecer si funciona como:

- opción configurable;
- ejemplo;
- caso de uso;
- perfil editorial;
- referencia histórica;
- sector configurable;
- elemento de una lista amplia;
- condición marcada con `si aplica` o `según perfil`.

Ejemplo correcto:

> La audiencia objetivo puede incluir clientes, reclutadores, comunidades, lectores, responsables internos o interesados, según el perfil configurado.

En este caso, `clientes` es válido porque aparece como una opción dentro de una lista amplia.

### 4.2 Funciones no permitidas

Un concepto específico no debe aparecer como:

- identidad universal del framework;
- sujeto obligatorio de todos los perfiles;
- audiencia fija;
- objetivo único;
- métrica obligatoria;
- regla transversal;
- supuesto no configurado;
- comportamiento obligatorio del sistema.

Ejemplo incorrecto:

> El framework ayuda al cliente a generar leads comerciales cada semana.

Esta frase es incorrecta como regla universal porque asume que todos los perfiles tienen clientes, buscan leads y tienen un objetivo comercial.

Una versión correcta sería:

> El framework ayuda al perfil configurado a preparar contenido alineado con su objetivo comunicativo, que puede ser comercial, profesional, institucional, educativo o de empleabilidad, según el caso.

---

## 5. Matriz inicial de conceptos sensibles

Esta matriz no elimina conceptos. Define dónde pueden vivir y cuándo se consideran contaminación conceptual.

| Concepto | Permitido cuando | Problemático cuando | Alternativa en núcleo |
|---|---|---|---|
| empresa | aparece como tipo de perfil, marca corporativa, organización o caso de uso | se usa como sujeto universal del framework | perfil, organización, emisor o proyecto |
| cliente | aparece en perfiles comerciales, casos B2B o listas configurables | se asume que todo perfil tiene clientes | audiencia objetivo, destinatario, lector, interesado |
| B2B | aparece en el caso `linkedin_autonomo_b2b` o perfiles comerciales | se presenta como enfoque universal del framework | perfil configurado, objetivo comunicativo |
| oferta | aparece en perfiles comerciales o como opción `si aplica` | se exige a todos los perfiles tener oferta | propuesta, mensaje, acción esperada, objetivo comunicativo |
| lead | aparece en perfiles comerciales donde se mida captación | se usa como métrica universal | interacción cualificada, señal de interés |
| negocio | aparece en casos comerciales o empresariales | define todo el sistema como herramienta de negocio | actividad, proyecto, contexto, perfil |
| comprador | aparece en perfiles comerciales | se asume como audiencia universal | audiencia objetivo, decisor si aplica |
| reclutador | aparece en perfiles de empleabilidad | se asume como audiencia universal | audiencia objetivo |
| CV / hoja de vida | aparece en casos de búsqueda de empleo | se incorpora al núcleo como función general | trayectoria, experiencia, perfil profesional si aplica |
| empleabilidad | aparece en perfiles de búsqueda laboral | se convierte en objetivo universal | objetivo comunicativo configurado |
| comunidad | aparece en perfiles institucionales, educativos o comunitarios | reemplaza a toda audiencia posible | audiencia objetivo |
| institución | aparece como tipo de perfil u organización | se asume como modelo universal | organización, perfil editorial |
| logística | aparece como sector, caso heredado o ejemplo histórico | actúa como identidad del framework | sector configurable |
| Alex | aparece como referencia histórica o ejemplo autorizado | actúa como rol de aprobación total o identidad de todo el framework | aprobador humano, responsable del perfil |
| 3 publicaciones por semana | aparece como configuración de un caso concreto | se define como frecuencia universal | frecuencia configurada por perfil |

---

## 6. Reglas por sede documental

### 6.1 `docs/core/`

Esta sede debe mantenerse universal.

Puede contener conceptos específicos solo si aparecen como:

- ejemplo claramente marcado;
- opción configurable;
- referencia histórica justificada;
- advertencia de no contaminación.

No debe contener conceptos específicos como supuestos base.

Ejemplo correcto:

> El framework puede adaptarse a perfiles comerciales, profesionales, institucionales o de empleabilidad.

Ejemplo incorrecto:

> El framework está diseñado para que las empresas generen clientes mediante LinkedIn.

---

### 6.2 `docs/governance/`

Esta sede define reglas, gates, políticas y criterios de control.

Debe usar lenguaje general y adaptable.

Puede mencionar conceptos específicos si los trata como riesgos, ejemplos o condiciones.

Ejemplo correcto:

> Un claim comercial, laboral, institucional o técnico debe estar respaldado por evidencia cuando corresponda.

Ejemplo incorrecto:

> Todo claim debe demostrar resultados de negocio para clientes.

---

### 6.3 `docs/architecture/`

Esta sede define responsabilidades funcionales y ubicación preliminar de componentes.

Debe evitar decidir prematuramente que una responsabilidad pertenece a un agente, skill, workflow o script si todavía no se ha cerrado la fase correspondiente.

Debe describir funciones en términos amplios:

- audiencia;
- emisor;
- perfil;
- objetivo comunicativo;
- riesgo;
- trazabilidad;
- publicabilidad;
- validación.

Puede mencionar perfiles o casos si están claramente marcados como ejemplos.

---

### 6.4 `docs/templates/`

Esta sede contiene plantillas transversales.

Las plantillas pueden incluir opciones específicas, pero no deben obligar a todos los perfiles a usar una opción concreta.

Ejemplo correcto:

> Propuesta, servicio, proyecto, logro, aprendizaje u oferta a impulsar, si aplica.

Ejemplo incorrecto:

> Oferta comercial a impulsar.

---

### 6.5 `docs/use_cases/`

Esta sede sí puede contener lenguaje específico.

Aquí pueden aparecer términos como:

- cliente;
- empresa;
- B2B;
- oferta;
- reclutador;
- CV;
- comunidad;
- logística;
- sector;
- ventas;
- empleabilidad.

La condición es que el lenguaje corresponda al caso de uso concreto y no intente redefinir el núcleo del framework.

Ejemplo correcto:

> En el caso `linkedin_autonomo_b2b`, la audiencia puede incluir responsables de negocio y potenciales clientes.

Ejemplo incorrecto:

> Como todo uso del framework busca clientes, este caso aplica la regla general de captación comercial.

---

### 6.6 `docs/evidence/` y `output/`

Estas sedes pueden contener evidencias, dry runs, ejemplos históricos y reportes generados.

Los conceptos específicos pueden aparecer si forman parte de una prueba, evidencia o salida histórica.

No deben usarse como fuente normativa principal del framework.

---

### 6.7 `tools/`

Esta sede contiene lógica determinista.

Los scripts no deben inventar reglas conceptuales.  
Deben ejecutar reglas previamente definidas en documentos de gobernanza.

Por tanto, cualquier evolución futura de `tools/audit_conceptual_contamination.py` debe basarse en esta política o en documentos equivalentes de gobernanza.

---

## 7. Ejemplos de uso correcto e incorrecto

### 7.1 Concepto: cliente

Incorrecto en núcleo:

> El cliente completa el intake para definir su oferta y generar leads.

Correcto en núcleo:

> El responsable del perfil completa el intake para definir su objetivo comunicativo, audiencia y señales reales.

Correcto en caso comercial:

> El cliente ideal del perfil autónomo B2B puede ser una empresa que necesita mejorar su control operativo.

---

### 7.2 Concepto: empresa

Incorrecto en núcleo:

> El framework ayuda a empresas a publicar contenido de autoridad.

Correcto en núcleo:

> El framework ayuda a perfiles editoriales configurados a preparar contenido profesional para LinkedIn.

Correcto en perfil específico:

> Este perfil representa una empresa de servicios que busca fortalecer su autoridad en LinkedIn.

---

### 7.3 Concepto: B2B

Incorrecto en núcleo:

> El framework produce contenido B2B para generar oportunidades comerciales.

Correcto en núcleo:

> El framework produce contenido profesional alineado con el objetivo comunicativo del perfil.

Correcto en caso de uso:

> El caso `linkedin_autonomo_b2b` prioriza conversaciones comerciales cualificadas.

---

### 7.4 Concepto: empleabilidad

Incorrecto en núcleo:

> El framework ayuda a mejorar la empleabilidad del usuario.

Correcto en núcleo:

> El framework puede adaptarse a objetivos comunicativos de posicionamiento, empleabilidad, autoridad, educación, institución o comercialización, según el perfil.

Correcto en caso de uso:

> El perfil de búsqueda de empleo prioriza visibilidad profesional, claridad de trayectoria y conexión con reclutadores.

---

### 7.5 Concepto: logística

Incorrecto en núcleo:

> El framework está diseñado para comunicar problemas logísticos.

Correcto en núcleo:

> Los sectores específicos se configuran como casos de uso o contextos editoriales.

Correcto en caso heredado:

> El caso heredado de logística se conserva como referencia histórica y ejemplo de validación.

---

## 8. Relación con auditorías deterministas

Esta política debe servir como base para futuras mejoras de `tools/audit_conceptual_contamination.py`.

El auditor determinista no debe limitarse a buscar palabras aisladas.

Debe evaluar al menos tres factores:

1. **Ruta del archivo:** por ejemplo, `docs/core/`, `docs/templates/`, `docs/use_cases/`.
2. **Concepto sensible detectado:** por ejemplo, `cliente`, `empresa`, `B2B`, `empleabilidad`, `logística`.
3. **Función contextual probable:** por ejemplo, regla universal, opción configurable, caso de uso, ejemplo o referencia histórica.

El objetivo futuro del script será clasificar hallazgos como:

- `BLOCKING_CONTAMINATION`
- `WARNING_REVIEW_REQUIRED`
- `ALLOW_CONFIGURABLE_OPTION`
- `ALLOW_USE_CASE_CONTEXT`
- `ALLOW_HISTORICAL_REFERENCE`

Esta mejora pertenece a una fase posterior y no debe implementarse antes de cerrar la política documental y la alineación de los documentos base.

---

## 9. Criterio operativo para agentes y humanos

Cuando un humano, agente o asistente revise documentación del framework, debe aplicar este orden:

1. Identificar la sede documental.
2. Identificar el concepto sensible.
3. Determinar si el concepto actúa como regla universal o como opción contextual.
4. Corregir solo si el concepto invade una sede que no le corresponde.
5. Mantener el concepto si está correctamente ubicado como perfil, caso, ejemplo o configuración.
6. Evitar reemplazos mecánicos por coincidencia literal.
7. Registrar como deuda futura cualquier patrón que requiera mejora de auditoría determinista.

---

## 10. Regla de cierre

Una modificación documental respeta esta política si cumple las siguientes condiciones:

1. No convierte un caso específico en identidad general.
2. No convierte un perfil editorial en regla universal.
3. No elimina conceptos válidos cuando están correctamente contextualizados.
4. No generaliza tanto el lenguaje que el documento pierde utilidad práctica.
5. Mantiene la separación entre núcleo, canal, perfil, caso de uso, sector y ejecución temporal.
6. Puede ser revisada posteriormente por un gate determinista sin depender exclusivamente de interpretación manual.

---

## 11. Resumen ejecutivo

`linkedin_content_framework` no busca eliminar conceptos específicos como empresa, cliente, B2B, empleabilidad, institución o logística.

Busca impedir que esos conceptos contaminen el núcleo del sistema.

La solución no es borrar palabras.  
La solución es respetar sedes conceptuales.

El núcleo define reglas universales.  
Los perfiles definen identidad comunicativa.  
Los casos de uso definen objetivos concretos.  
Los sectores definen contexto.  
Las plantillas permiten configuración.  
Los gates verifican publicabilidad, riesgo y trazabilidad.  
Python, en fases posteriores, deberá hacer cumplir estas fronteras de forma determinista.
