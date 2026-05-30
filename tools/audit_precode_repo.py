#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de auditoría pre-código para el framework linkedin_content_framework.
Valida la integridad del repositorio, la existencia de archivos clave y 
evita la contaminación conceptual del núcleo con términos del caso heredado.
"""

import os
import sys

# Definir la raíz del repositorio de forma dinámica
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Lista de archivos requeridos
REQUIRED_FILES = [
    "README.md",
    "AGENTS.md",
    "MIGRATION_NOTES.md",
    ".gitignore",
    "docs/core/identity_contract.md",
    "docs/core/vision.md",
    "docs/core/scope_yes_no.md",
    "docs/core/principles.md",
    "docs/use_cases/linkedin_logistica_caso_heredado/README.md"
]

# Lista de archivos .gitkeep requeridos
REQUIRED_GITKEEPS = [
    ".harness/memory/.gitkeep",
    ".harness/state/.gitkeep",
    ".harness/traces/.gitkeep",
    "output/trace/.gitkeep"
]

# Expresiones prohibidas en docs/core/
FORBIDDEN_CORE_TERMS = [
    "empresas logísticas",
    "pymes logísticas",
    "operaciones logísticas",
    "albaranes",
    "facturas logísticas",
    "perfil de Alex",
    "3 publicaciones por semana"
]

def check_required_files():
    """
    Verifica que todos los archivos obligatorios estén presentes en el repositorio.
    """
    success = True
    results = []
    
    for relative_path in REQUIRED_FILES:
        full_path = os.path.join(REPO_ROOT, relative_path)
        if os.path.isfile(full_path):
            results.append((True, relative_path, "Archivo obligatorio presente."))
        else:
            results.append((False, relative_path, "Falta el archivo obligatorio en el repositorio."))
            success = False
            
    return success, results


def check_gitkeep_files():
    """
    Verifica la existencia de los archivos .gitkeep obligatorios para conservar
    la estructura de carpetas temporales y de trazas.
    """
    success = True
    results = []
    
    for relative_path in REQUIRED_GITKEEPS:
        full_path = os.path.join(REPO_ROOT, relative_path)
        if os.path.isfile(full_path):
            results.append((True, relative_path, "Archivo .gitkeep de estructura presente."))
        else:
            results.append((False, relative_path, "Falta el archivo .gitkeep para mantener la estructura de directorios."))
            success = False
            
    return success, results


def check_vision_content():
    """
    Verifica que vision.md no contenga las expresiones antiguas obsoletas.
    """
    success = True
    results = []
    relative_path = "docs/core/vision.md"
    full_path = os.path.join(REPO_ROOT, relative_path)
    
    if not os.path.isfile(full_path):
        return False, [(False, relative_path, "No se puede auditar porque el archivo no existe.")]
        
    forbidden_terms = ["consultores B2B", "de bajo valor técnico"]
    
    try:
        with open(full_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        for term in forbidden_terms:
            if term in content:
                results.append((False, relative_path, f"Contiene el término prohibido: '{term}'."))
                success = False
            else:
                results.append((True, relative_path, f"No contiene el término prohibido: '{term}'."))
    except Exception as e:
        results.append((False, relative_path, f"Error al leer el archivo: {str(e)}"))
        success = False
        
    return success, results


def check_principles_content():
    """
    Verifica que principles.md no contenga mezcla de idiomas (debe living).
    """
    success = True
    results = []
    relative_path = "docs/core/principles.md"
    full_path = os.path.join(REPO_ROOT, relative_path)
    
    if not os.path.isfile(full_path):
        return False, [(False, relative_path, "No se puede auditar porque el archivo no existe.")]
        
    forbidden_term = "debe living"
    
    try:
        with open(full_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        if forbidden_term in content:
            results.append((False, relative_path, f"Contiene la mezcla de idiomas prohibida: '{forbidden_term}'."))
            success = False
        else:
            results.append((True, relative_path, f"No contiene la mezcla de idiomas: '{forbidden_term}'."))
    except Exception as e:
        results.append((False, relative_path, f"Error al leer el archivo: {str(e)}"))
        success = False
        
    return success, results


def check_core_contamination():
    """
    Escanea la carpeta docs/core/ en busca de términos específicos del caso
    heredado (logística, datos de Alex) para asegurar la higiene del núcleo.
    """
    success = True
    results = []
    core_dir = os.path.join(REPO_ROOT, "docs", "core")
    
    if not os.path.isdir(core_dir):
        return False, [("docs/core", "Directorio docs/core/ no encontrado.")]
        
    for root, _, files in os.walk(core_dir):
        for file in files:
            full_path = os.path.join(root, file)
            relative_path = os.path.relpath(full_path, REPO_ROOT)
            
            try:
                with open(full_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    
                for term in FORBIDDEN_CORE_TERMS:
                    if term in content:
                        results.append((False, relative_path, f"Contaminación del núcleo: se encontró el término '{term}'."))
                        success = False
            except Exception as e:
                results.append((False, relative_path, f"Error al leer el archivo para buscar contaminación: {str(e)}"))
                success = False
                
    # Si no hubo fallos en ningún archivo de la carpeta docs/core/
    if success:
        results.append((True, "docs/core/*", "Higiene conceptual del núcleo verificada con éxito. Sin términos del caso heredado."))
        
    return success, results


def check_gitignore_exclusions():
    """
    Verifica que el archivo .gitignore no contenga las exclusiones completas
    de .harness/ ni output/ como líneas exactas.
    """
    success = True
    results = []
    relative_path = ".gitignore"
    full_path = os.path.join(REPO_ROOT, relative_path)
    
    if not os.path.isfile(full_path):
        return False, [(False, relative_path, "Falta el archivo .gitignore.")]
        
    forbidden_lines = [".harness/", "output/"]
    
    try:
        with open(full_path, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f.readlines()]
            
        for forbidden_line in forbidden_lines:
            if forbidden_line in lines:
                results.append((False, relative_path, f"Exclusión completa prohibida en .gitignore: '{forbidden_line}'."))
                success = False
            else:
                results.append((True, relative_path, f"Correcto: no se excluye completamente la carpeta '{forbidden_line}'."))
    except Exception as e:
        results.append((False, relative_path, f"Error al leer .gitignore: {str(e)}"))
        success = False
        
    return success, results


def main():
    """
    Función principal de ejecución del script de auditoría.
    """
    print("======================================================================")
    print("   INICIANDO AUDITORÍA PRE-CÓDIGO DE LINKEDIN_CONTENT_FRAMEWORK")
    print("======================================================================")
    
    all_passed = True
    
    # 1. Verificar archivos obligatorios
    ok, details = check_required_files()
    if not ok:
        all_passed = False
    print("\n[CHECK 1] Existencia de archivos obligatorios del núcleo:")
    for status, path, desc in details:
        icon = "✓" if status else "✗"
        print(f"  {icon} {path}: {desc}")
        
    # 2. Verificar archivos .gitkeep
    ok, details = check_gitkeep_files()
    if not ok:
        all_passed = False
    print("\n[CHECK 2] Existencia de archivos .gitkeep de estructura:")
    for status, path, desc in details:
        icon = "✓" if status else "✗"
        print(f"  {icon} {path}: {desc}")
        
    # 3. Verificar contenido de docs/core/vision.md
    ok, details = check_vision_content()
    if not ok:
        all_passed = False
    print("\n[CHECK 3] Contenido obsoleto en vision.md:")
    for status, path, desc in details:
        icon = "✓" if status else "✗"
        print(f"  {icon} {path}: {desc}")
        
    # 4. Verificar contenido de docs/core/principles.md
    ok, details = check_principles_content()
    if not ok:
        all_passed = False
    print("\n[CHECK 4] Mezcla de idiomas en principles.md:")
    for status, path, desc in details:
        icon = "✓" if status else "✗"
        print(f"  {icon} {path}: {desc}")
        
    # 5. Verificar contaminación conceptual en docs/core/
    ok, details = check_core_contamination()
    if not ok:
        all_passed = False
    print("\n[CHECK 5] Higiene conceptual en docs/core/ (caso heredado / logística):")
    for status, path, desc in details:
        icon = "✓" if status else "✗"
        print(f"  {icon} {path}: {desc}")
        
    # 6. Verificar exclusiones completas en .gitignore
    ok, details = check_gitignore_exclusions()
    if not ok:
        all_passed = False
    print("\n[CHECK 6] Exclusiones completas de carpetas en .gitignore:")
    for status, path, desc in details:
        icon = "✓" if status else "✗"
        print(f"  {icon} {path}: {desc}")
        
    print("\n======================================================================")
    if all_passed:
        print("  RESULTADO: TODAS LAS COMPROBACIONES PASARON CORRECTAMENTE (EXIT 0)")
        print("======================================================================")
        sys.exit(0)
    else:
        print("  RESULTADO: SE ENCONTRARON FALLOS EN LA AUDITORÍA (EXIT 1)")
        print("  Por favor, revise las recomendaciones listadas arriba.")
        print("======================================================================")
        sys.exit(1)


if __name__ == "__main__":
    main()
