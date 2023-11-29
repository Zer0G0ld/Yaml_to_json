#!/bin/bash

yaml_file="exemplo.yaml"
temp_dir=$(mktemp -d)

if [ -f "$yaml_file" ]; then
    # Copia o arquivo YAML para o diretório temporário
    cp "$yaml_file" "$temp_dir/"
    
    # Muda para o diretório temporário
    cd "$temp_dir" || exit
    
    # Converte YAML para JSON usando yq e jq
    yq eval '.' "$yaml_file" | jq -c .

    # Limpa o diretório temporário
    rm -rf "$temp_dir"
else
    echo "Arquivo YAML não encontrado."
fi
