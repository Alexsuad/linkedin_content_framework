# tools/audit_conceptual_contamination.py
# -*- coding: utf-8 -*-
"""
Script de auditoría determinista para la detección de contaminación conceptual
en el núcleo del LinkedIn Content Framework.
"""

import os
import sys

# Definir la raíz del repositorio
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Rutas a escanear (relativas a REPO_ROOT)
SCAN_DIRS = [
    "docs/core",
    "docs/governance",
    "docs/architecture",
    "docs/templates",
    "docs/use_cases"
]

SCAN_FILES = [
    "README.md",
    "AGENTS.md",
    "MIGRATION_NOTES.md"
]

# Carpetas a ignorar
IGNORE_DIRS = [
    ".git",
    ".harness",
    "output",
    "__pycache__"
]

# Definición de Patrones y Reglas por Grupos

# Grupo A - Sector / Logística
GRUPO_A_PATTERNS = [
    "logística", "logístico", "logísticas", "transporte", "albarán", "albaranes",
    "factura vs albarán", "pymes logísticas", "empresas logísticas"
]
GRUPO_A_ESCAPE = [
    "no debe contaminar", "caso heredado", "sector configurable", "no como identidad universal",
    "ejemplo", "referencia"
]
GRUPO_A_BLOCKING = [
    "el sistema debe generar contenido para empresas logísticas",
    "el objetivo principal es logística",
    "frecuencia para empresas logísticas",
    "audiencia fija logística"
]

# Grupo B - Persona / Alex
GRUPO_B_PATTERNS = [
    "alex", "alexander", "perfil de alex", "aprobación de alex"
]
GRUPO_B_ESCAPE = [
    "ejemplo", "referencia", "histórica", "histórico"
]
GRUPO_B_BLOCKING = [
    "aprobador universal", "aprobador único", "aprobación por parte de alex",
    "identidad general", "alex es el aprobador"
]

# Grupo C - Frecuencia Fija
GRUPO_C_PATTERNS = [
    "3 publicaciones semanales", "tres publicaciones semanales",
    "3 posts por semana", "frecuencia oficial"
]
GRUPO_C_BLOCKING = [
    "regla universal", "frecuencia oficial del framework", "frecuencia obligatoria",
    "debe publicar obligatoriamente"
]

# Grupo D - Aprobación Humana Rígida / No Flight
GRUPO_D_PATTERNS = [
    "no flight", "firma humana invariable", "ninguna publicación debe salir sin validación humana",
    "aprobación humana obligatoria", "prohibida cualquier publicación automática",
    "no publicar automáticamente nunca"
]
GRUPO_D_MATIZ = [
    "fase de calibración", "nivel de autonomía", "autonomía progresiva",
    "aprobación compacta", "revisión por excepción", "fase madura"
]

# Grupo E - Decisiones Prematuras Agénticas
GRUPO_E_PATTERNS = [
    "agente de redacción", "agente editor", "agente publicador", "skill determinista",
    "pipeline debe terminar", "workflow definitivo", "agente obligatorio"
]
GRUPO_E_REPLACEMENTS = {
    "agente de redacción": "posible agente futuro / responsabilidad funcional",
    "agente editor": "posible agente futuro / responsabilidad funcional",
    "agente publicador": "posible agente futuro / responsabilidad funcional",
    "skill determinista": "posible skill futura / ubicación arquitectónica preliminar",
    "pipeline debe terminar": "ubicación arquitectónica preliminar",
    "workflow definitivo": "fase futura / workflow preliminar",
    "agente obligatorio": "responsabilidad funcional"
}

def analyze_line(line, file_rel_path, line_num):
    """
    Analiza una línea de texto y retorna un hallazgo si coincide con algún patrón.
    """
    line_lower = line.lower()
    findings = []
    
    # 1. Analizar Grupo A (Logística/Sector)
    for pattern in GRUPO_A_PATTERNS:
        if pattern in line_lower:
            # Comprobar si está en carpetas restringidas
            is_in_core_or_gov = any(file_rel_path.startswith(d) for d in ["docs/core", "docs/governance", "docs/architecture"]) or file_rel_path in SCAN_FILES
            
            # Comprobar reglas semánticas
            is_blocking = any(b in line_lower for b in GRUPO_A_BLOCKING)
            is_escape = any(e in line_lower for e in GRUPO_A_ESCAPE)
            
            if is_blocking:
                severity = "BLOCKING_CONTAMINATION"
                rec = "Eliminar la pretensión de que la logística es una regla universal o identidad del framework."
            elif is_escape:
                severity = "ALLOW_NORMATIVE_REFERENCE"
                rec = "Ninguna (referencia normativa permitida o de ejemplo)."
            elif is_in_core_or_gov:
                severity = "WARNING_REVIEW_REQUIRED"
                rec = "Revisar uso de términos del sector logístico en el Core general del framework."
            else:
                severity = "ALLOW_NORMATIVE_REFERENCE"
                rec = "Uso en carpeta de plantillas o casos de uso permitido."
                
            findings.append({
                "file": file_rel_path,
                "line": line_num,
                "pattern": pattern,
                "group": "Grupo A - Sector / Logística",
                "severity": severity,
                "context": line.strip(),
                "recommendation": rec
            })
            break # Evitar duplicados del mismo grupo en la misma línea
            
    # 2. Analizar Grupo B (Alex)
    for pattern in GRUPO_B_PATTERNS:
        if pattern in line_lower:
            is_blocking = any(b in line_lower for b in GRUPO_B_BLOCKING)
            is_escape = "decision_log.md" in file_rel_path or "use_cases" in file_rel_path or any(e in line_lower for e in GRUPO_B_ESCAPE)
            
            if is_blocking:
                severity = "BLOCKING_CONTAMINATION"
                rec = "Reemplazar la referencia universal al aprobador 'Alex' por 'Aprobador Humano / Propietario del Perfil'."
            elif is_escape:
                severity = "ALLOW_NORMATIVE_REFERENCE"
                rec = "Ninguna (referencia histórica autorizada en log o caso de uso)."
            else:
                severity = "WARNING_REVIEW_REQUIRED"
                rec = "Revisar uso de nombre propio en documento general. Abstraer a 'Aprobador Humano'."
                
            findings.append({
                "file": file_rel_path,
                "line": line_num,
                "pattern": pattern,
                "group": "Grupo B - Persona / Alex",
                "severity": severity,
                "context": line.strip(),
                "recommendation": rec
            })
            break
            
    # 3. Analizar Grupo C (Frecuencia Fija)
    for pattern in GRUPO_C_PATTERNS:
        if pattern in line_lower:
            is_blocking = any(b in line_lower for b in GRUPO_C_BLOCKING)
            is_use_case = "use_cases/linkedin_autonomo_b2b" in file_rel_path
            
            if is_blocking:
                severity = "BLOCKING_CONTAMINATION"
                rec = "Hacer la frecuencia configurable. No definir una frecuencia fija como regla general del framework."
            elif is_use_case:
                severity = "ALLOW_NORMATIVE_REFERENCE"
                rec = "Ninguna (frecuencia configurada en caso operativo local)."
            else:
                severity = "WARNING_REVIEW_REQUIRED"
                rec = "Revisar la frecuencia fija. Debe presentarse de forma configurable o como ejemplo."
                
            findings.append({
                "file": file_rel_path,
                "line": line_num,
                "pattern": pattern,
                "group": "Grupo C - Frecuencia Fija",
                "severity": severity,
                "context": line.strip(),
                "recommendation": rec
            })
            break

    # 4. Analizar Grupo D (Aprobación Rígida / No Flight)
    for pattern in GRUPO_D_PATTERNS:
        if pattern in line_lower:
            has_matiz = any(m in line_lower for m in GRUPO_D_MATIZ)
            
            if has_matiz:
                severity = "ALLOW_NORMATIVE_REFERENCE"
                rec = "Ninguna (aprobación humana debidamente matizada por niveles de autonomía o calibración)."
            else:
                # Comprobación de rigidez
                severity = "WARNING_REVIEW_REQUIRED"
                rec = "Matizar el principio de aprobación agregando referencias a 'fase de calibración', 'niveles de autonomía', o 'aprobación compacta por lotes'."
                
            findings.append({
                "file": file_rel_path,
                "line": line_num,
                "pattern": pattern,
                "group": "Grupo D - Aprobación Rígida",
                "severity": severity,
                "context": line.strip(),
                "recommendation": rec
            })
            break

    # 5. Analizar Grupo E (Decisiones Prematuras)
    for pattern in GRUPO_E_PATTERNS:
        if pattern in line_lower:
            # Comprobar si el archivo es anterior a la fase agéntica
            is_premature = not ("docs/architecture/minimum_agent_architecture" in file_rel_path or "agent_skill_gate_matrix" in file_rel_path)
            
            if is_premature:
                severity = "WARNING_REVIEW_REQUIRED"
                sug = GRUPO_E_REPLACEMENTS.get(pattern, "responsabilidad funcional / posible componente futuro")
                rec = f"Reemplazar decisión agéntica prematura por: '{sug}'."
            else:
                severity = "ALLOW_NORMATIVE_REFERENCE"
                rec = "Ninguna (definido en documentos específicos de arquitectura agéntica)."
                
            findings.append({
                "file": file_rel_path,
                "line": line_num,
                "pattern": pattern,
                "group": "Grupo E - Decisiones Prematuras",
                "severity": severity,
                "context": line.strip(),
                "recommendation": rec
            })
            break

    return findings

def scan_files():
    """
    Escanea recursivamente el repositorio y retorna una lista con todos los hallazgos.
    """
    all_findings = []
    scanned_count = 0
    
    # Obtener archivos en directorios
    files_to_scan = []
    
    for scan_dir in SCAN_DIRS:
        full_dir_path = os.path.join(REPO_ROOT, scan_dir)
        if not os.path.isdir(full_dir_path):
            continue
            
        for root, dirs, files in os.walk(full_dir_path):
            # Eliminar directorios a ignorar
            dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
            
            for file in files:
                if file.endswith(".md"):
                    full_path = os.path.join(root, file)
                    rel_path = os.path.relpath(full_path, REPO_ROOT)
                    files_to_scan.append(rel_path)
                    
    # Añadir archivos individuales del raíz
    for file in SCAN_FILES:
        full_path = os.path.join(REPO_ROOT, file)
        if os.path.isfile(full_path):
            files_to_scan.append(file)
            
    # Escanear cada archivo
    for rel_path in sorted(list(set(files_to_scan))):
        full_path = os.path.join(REPO_ROOT, rel_path)
        scanned_count += 1
        
        try:
            with open(full_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
                
            for idx, line in enumerate(lines, 1):
                line_findings = analyze_line(line, rel_path, idx)
                all_findings.extend(line_findings)
        except Exception as e:
            print(f"Error leyendo archivo {rel_path}: {e}")
            
    return scanned_count, all_findings

def generate_report(scanned_count, findings):
    """
    Genera el reporte Markdown en output/reports/conceptual_contamination_report.md
    """
    reports_dir = os.path.join(REPO_ROOT, "output", "reports")
    os.makedirs(reports_dir, exist_ok=True)
    report_path = os.path.join(reports_dir, "conceptual_contamination_report.md")
    
    # Contar severidades
    blocking_count = sum(1 for f in findings if f["severity"] == "BLOCKING_CONTAMINATION")
    warning_count = sum(1 for f in findings if f["severity"] == "WARNING_REVIEW_REQUIRED")
    allow_count = sum(1 for f in findings if f["severity"] == "ALLOW_NORMATIVE_REFERENCE")
    
    with open(report_path, "w", encoding="utf-8") as r:
        r.write("# Reporte de contaminación conceptual\n\n")
        r.write("## Resumen\n")
        r.write(f"- Archivos escaneados: {scanned_count}\n")
        r.write(f"- Hallazgos totales: {len(findings)}\n")
        r.write(f"  - Bloqueantes (`BLOCKING_CONTAMINATION`): {blocking_count}\n")
        r.write(f"  - Advertencias (`WARNING_REVIEW_REQUIRED`): {warning_count}\n")
        r.write(f"  - Referencias permitidas (`ALLOW_NORMATIVE_REFERENCE`): {allow_count}\n\n")
        
        # 1. Bloqueantes
        r.write("## Hallazgos bloqueantes\n")
        if blocking_count == 0:
            r.write("No se han encontrado hallazgos bloqueantes en el repositorio.\n\n")
        else:
            for f in findings:
                if f["severity"] == "BLOCKING_CONTAMINATION":
                    r.write(f"### [BLOQUEANTE] Archivo: [{f['file']}](file:///{REPO_ROOT.replace('\\', '/')}/{f['file']}#L{f['line']})\n")
                    r.write(f"- **Línea:** {f['line']}\n")
                    r.write(f"- **Patrón detectado:** `{f['pattern']}`\n")
                    r.write(f"- **Grupo:** {f['group']}\n")
                    r.write(f"- **Contexto:**\n  > {f['context']}\n")
                    r.write(f"- **Recomendación:** {f['recommendation']}\n\n")
                    
        # 2. Advertencias
        r.write("## Advertencias para revisión\n")
        if warning_count == 0:
            r.write("No se han encontrado advertencias de revisión recomendada.\n\n")
        else:
            for f in findings:
                if f["severity"] == "WARNING_REVIEW_REQUIRED":
                    r.write(f"### [ADVERTENCIA] Archivo: [{f['file']}](file:///{REPO_ROOT.replace('\\', '/')}/{f['file']}#L{f['line']})\n")
                    r.write(f"- **Línea:** {f['line']}\n")
                    r.write(f"- **Patrón detectado:** `{f['pattern']}`\n")
                    r.write(f"- **Grupo:** {f['group']}\n")
                    r.write(f"- **Contexto:**\n  > {f['context']}\n")
                    r.write(f"- **Recomendación:** {f['recommendation']}\n\n")
                    
        # 3. Referencias permitidas
        r.write("## Referencias normativas permitidas\n")
        if allow_count == 0:
            r.write("No se registraron referencias normativas permitidas.\n\n")
        else:
            for f in findings:
                if f["severity"] == "ALLOW_NORMATIVE_REFERENCE":
                    r.write(f"- **Archivo:** `{f['file']}` (Línea {f['line']}) | **Patrón:** `{f['pattern']}` | **Grupo:** {f['group']}\n")
            r.write("\n")
            
        # 4. Recomendaciones de corrección generales
        r.write("## Recomendaciones de corrección\n")
        r.write("1. **Desacoplamiento:** Asegurar que todo término sobre 'logística', 'transporte' o albaranes viva de forma aislada en `docs/use_cases/` y no contamine los manuales generales de gobernanza.\n")
        r.write("2. **Identidad del Aprobador:** Reemplazar menciones rígidas a 'Alex' por términos de rol funcional como 'Aprobador Humano' o 'Propietario del Perfil'.\n")
        r.write("3. **Autonomía Progresiva:** Matizar los principios del framework asegurando que el control manual es prioritario en fase de calibración pero automatizable mediante gates y firmas compactas en producción.\n")
        r.write("4. **Abstracción de Agentes:** No referirse a agentes específicos de IA de forma obligatoria en la Fase 1; usar denominaciones funcionales de roles.\n")
        
    return report_path, blocking_count, warning_count, allow_count

def main():
    print("======================================================================")
    print("   INICIANDO AUDITORÍA DETERMINISTA DE CONTAMINACIÓN CONCEPTUAL")
    print("======================================================================")
    
    scanned_count, findings = scan_files()
    
    report_path, blocking, warning, allow = generate_report(scanned_count, findings)
    
    print(f"\nResumen de Hallazgos:")
    print(f"  - Total archivos escaneados: {scanned_count}")
    print(f"  - Total hallazgos detectados: {len(findings)}")
    print(f"    - Bloqueantes (BLOCKING_CONTAMINATION): {blocking}")
    print(f"    - Advertencias (WARNING_REVIEW_REQUIRED): {warning}")
    print(f"    - Referencias permitidas (ALLOW_NORMATIVE_REFERENCE): {allow}")
    
    print(f"\nReporte Markdown generado con éxito en:")
    print(f"  {report_path}")
    print("======================================================================")
    
    # Retornar código de salida
    if blocking > 0:
        print("  RESULTADO: SE ENCONTRÓ CONTAMINACIÓN CONCEPTUAL BLOQUEANTE (EXIT 1)")
        print("======================================================================")
        sys.exit(1)
    elif warning > 0:
        print("  RESULTADO: COMPROBACIÓN COMPLETADA CON ADVERTENCIAS (EXIT 0)")
        print("  Se recomienda revisar el reporte generado.")
        print("======================================================================")
        sys.exit(0)
    else:
        print("  RESULTADO: REPOSITORIO COMPLETAMENTE LIMPIO DE CONTAMINACIÓN (EXIT 0)")
        print("======================================================================")
        sys.exit(0)

if __name__ == "__main__":
    main()
