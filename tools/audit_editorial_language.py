#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de auditoría determinista de lenguaje editorial.
Analiza patrones de lenguaje definidos en docs/governance/editorial_lexicon.yml.
"""

import os
import sys
import re

LEXICON_PATH = "docs/governance/editorial_lexicon.yml"
REPORT_DIR = "output/reports"
REPORT_PATH = os.path.join(REPORT_DIR, "editorial_language_report.md")

def parse_simple_yaml(filepath):
    """
    Parsea de forma básica y determinista el archivo YAML de léxico sin dependencias externas.
    Soporta secciones 'restringidos' y 'bloqueantes' con listas de patrones.
    """
    lexicon = {"restringidos": {}, "bloqueantes": {}}
    current_section = None
    current_key = None
    current_list_name = None

    if not os.path.exists(filepath):
        print(f"Error: No se encontró el archivo de léxico en {filepath}")
        return lexicon

    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line_strip = line.strip()
            # Omitir comentarios y líneas vacías
            if not line_strip or line_strip.startswith("#"):
                continue

            # Detectar sección principal
            if line.startswith("restringidos:"):
                current_section = "restringidos"
                current_key = None
                continue
            elif line.startswith("bloqueantes:"):
                current_section = "bloqueantes"
                current_key = None
                continue

            if current_section:
                # Detectar subclave (ej: consultoría:) con indentación de 2 espacios
                if line.startswith("  ") and not line.startswith("    ") and line_strip.endswith(":"):
                    current_key = line_strip[:-1].strip()
                    lexicon[current_section][current_key] = {"criterio": "", "patrones": []}
                    continue

                if current_key:
                    # Detectar criterio
                    if line_strip.startswith("criterio:"):
                        # Extraer valor quitando comillas
                        val = line_strip.replace("criterio:", "").strip().strip('"').strip("'")
                        lexicon[current_section][current_key]["criterio"] = val
                    # Detectar inicio de lista de patrones
                    elif line_strip.startswith("patrones:"):
                        current_list_name = "patrones"
                    # Elementos de la lista
                    elif line_strip.startswith("- ") and current_list_name == "patrones":
                        pattern_val = line_strip[2:].strip().strip('"').strip("'")
                        lexicon[current_section][current_key]["patrones"].append(pattern_val)

    return lexicon

def audit_file(file_path, lexicon):
    """
    Audita el archivo especificado usando el diccionario del léxico.
    """
    if not os.path.exists(file_path):
        print(f"Error: El archivo a auditar no existe en: {file_path}")
        sys.exit(1)

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    findings_restricted = []
    findings_blocked = []

    # Auditar Restringidos
    for key, data in lexicon["restringidos"].items():
        criterio = data["criterio"]
        for pattern in data["patrones"]:
            # Usar regex insensible a mayúsculas si no se especifican límites complejos
            # pero soportando opcionalmente escapes básicos
            flags = re.IGNORECASE
            try:
                matches = list(re.finditer(pattern, content, flags=flags))
                for match in matches:
                    # Obtener número de línea
                    line_no = content.count('\n', 0, match.start()) + 1
                    # Obtener la línea completa
                    lines = content.split('\n')
                    line_content = lines[line_no - 1] if line_no <= len(lines) else ""
                    findings_restricted.append({
                        "termino": key,
                        "patron": pattern,
                        "linea": line_no,
                        "contenido": line_content.strip(),
                        "criterio": criterio
                    })
            except re.error as e:
                print(f"Error en patrón regex '{pattern}': {e}")

    # Auditar Bloqueantes
    for key, data in lexicon["bloqueantes"].items():
        criterio = data["criterio"]
        for pattern in data["patrones"]:
            flags = re.IGNORECASE
            try:
                matches = list(re.finditer(pattern, content, flags=flags))
                for match in matches:
                    line_no = content.count('\n', 0, match.start()) + 1
                    lines = content.split('\n')
                    line_content = lines[line_no - 1] if line_no <= len(lines) else ""
                    findings_blocked.append({
                        "termino": key,
                        "patron": pattern,
                        "linea": line_no,
                        "contenido": line_content.strip(),
                        "criterio": criterio
                    })
            except re.error as e:
                print(f"Error en patrón regex '{pattern}': {e}")

    return findings_restricted, findings_blocked

def generate_report(file_path, restricted, blocked):
    """
    Genera un reporte en markdown de los hallazgos encontrados.
    """
    os.makedirs(REPORT_DIR, exist_ok=True)
    
    status_str = "REJECTED (EXIT 1)" if blocked else "WARNINGS/CLEAN (EXIT 0)"
    
    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write(f"# Reporte de Auditoría de Lenguaje Editorial\n\n")
        f.write(f"- **Archivo auditado:** `{file_path}`\n")
        f.write(f"- **Estado final:** {status_str}\n")
        f.write(f"- **Términos bloqueantes encontrados:** {len(blocked)}\n")
        f.write(f"- **Términos restringidos encontrados:** {len(restricted)}\n\n")
        
        f.write("## 1. Hallazgos Bloqueantes (Críticos)\n")
        if not blocked:
            f.write("No se encontraron términos bloqueantes. ¡Excelente!\n\n")
        else:
            f.write("| Línea | Término | Patrón Detectado | Línea de Texto | Criterio de Resolución |\n")
            f.write("| --- | --- | --- | --- | --- |\n")
            for item in blocked:
                f.write(f"| {item['linea']} | `{item['termino']}` | `{item['patron']}` | *\"{item['contenido']}\"* | {item['criterio']} |\n")
            f.write("\n")
            
        f.write("## 2. Hallazgos Restringidos (Advertencias)\n")
        if not restricted:
            f.write("No se encontraron términos restringidos.\n\n")
        else:
            f.write("| Línea | Término | Patrón Detectado | Línea de Texto | Criterio / Acción Requerida |\n")
            f.write("| --- | --- | --- | --- | --- |\n")
            for item in restricted:
                f.write(f"| {item['linea']} | `{item['termino']}` | `{item['patron']}` | *\"{item['contenido']}\"* | {item['criterio']} |\n")
            f.write("\n")

def main():
    if len(sys.argv) < 2:
        print("Uso: python3 tools/audit_editorial_language.py <ruta_del_archivo_md>")
        sys.exit(1)

    file_to_audit = sys.argv[1]
    
    # Parsea léxico
    lexicon = parse_simple_yaml(LEXICON_PATH)
    
    # Audita
    restricted, blocked = audit_file(file_to_audit, lexicon)
    
    # Reporta
    generate_report(file_to_audit, restricted, blocked)
    
    # Salida por consola
    print(f"\n==================================================")
    print(f"RESULTADO DE AUDITORÍA EDITORIAL PARA: {file_to_audit}")
    print(f"==================================================")
    print(f"Bloqueantes detectados: {len(blocked)}")
    print(f"Restringidos detectados: {len(restricted)}")
    print(f"Reporte generado en: {REPORT_PATH}\n")
    
    if blocked:
        print("ERROR CRÍTICO: Se han detectado términos bloqueados por la política editorial.")
        for item in blocked:
            print(f"  [Línea {item['linea']}] Término bloqueado: '{item['patron']}' -> Criterio: {item['criterio']}")
        print("==================================================")
        sys.exit(1)
    
    if restricted:
        print("ADVERTENCIA: Se han detectado términos restringidos. Validar contexto:")
        for item in restricted:
            print(f"  [Línea {item['linea']}] Término restringido: '{item['patron']}' -> Criterio: {item['criterio']}")
    else:
        print("Todo limpio. El archivo cumple las directrices editoriales básicas.")
        
    print("==================================================")
    sys.exit(0)

if __name__ == "__main__":
    main()
