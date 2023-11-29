import yaml
import json

def yaml_to_json(yaml_str):
    try:
        yaml_data = yaml.safe_load(yaml_str)
        json_data = json.dumps(yaml_data, indent=2)
        return json_data
    except yaml.YAMLError as e:
        return f"Erro ao processar YAML: {e}"

def read_yaml_file(file_path):
    try:
        with open(file_path, 'r') as file:
            yaml_str = file.read()
        return yaml_str
    except Exception as e:
        return f"Erro ao ler arquivo YAML: {e}"

# Exemplo de uso com leitura de arquivo
yaml_file_path = 'exemplo.yaml'

try:
    yaml_content = read_yaml_file(yaml_file_path)
    json_result = yaml_to_json(yaml_content)
    print(json_result)
except Exception as e:
    print(f"Erro: {e}")
