import os
import re
import sys
import json

STDLIB = sys.stdlib_module_names

def is_third_party(name):
    top_level = name.split(".")[0]
    return top_level not in STDLIB and top_level != "__future__"

def parse_requirements(path="requirements.txt"):
    if not os.path.exists(path):
        return set()
    packages = set()
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                name = re.split(r"[>=<!]", line)[0].strip()
                packages.add(name.lower())
    return packages

class Tracker:
    def __init__(self):
        self.seen = set()
    
    def find_spec(self, name, path, target=None):
        if is_third_party(name):
            self.seen.add(name.split(".")[0])
        return None
    
def get_explicit_imports(script_path: str) -> set:
    import ast
    with open(script_path) as f:
        tree = ast.parse(f.read())
    
    explicit = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                explicit.add(alias.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                explicit.add(node.module.split(".")[0])
    return explicit

