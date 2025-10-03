#!/usr/bin/env bash
set -euo pipefail

# Crea un virtualenv si no existe, instala dependencias y corre pytest
if [ ! -d .venv ]; then
	python3 -m venv .venv
fi

# activar el venv
# shellcheck disable=SC1091
source .venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

# Asegurar que el directorio del proyecto esté en PYTHONPATH para que
# pytest pueda importar el paquete local `miniapp`
export PYTHONPATH="${PYTHONPATH:-}:$(pwd)"

# Usar el módulo de Python para ejecutar pytest con el mismo intérprete
python -m pytest -q
