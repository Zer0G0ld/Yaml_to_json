#!/bin/bash

yaml_file="exemplo.yaml"

if [ -f "$yaml_file" ]; then
    # Convertendo YAML para JSON usando yq
    json_data=$(yq eval '.' "$yaml_file" | jq -c .)
    echo "$json_data"
else
    echo "Arquivo YAML não encontrado."
fi
