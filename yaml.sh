#!/bin/bash

yaml_file="exemplo.yaml"

if [ -f "$yaml_file" ]; then
    # Converte YAML para JSON usando yq e jq
    yq eval '.' "$yaml_file" | jq -c .
else
    echo "Arquivo YAML não encontrado."
fi
