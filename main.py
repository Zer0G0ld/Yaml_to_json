import yaml
import json

def yaml_to_json(yaml_str):
    try:
        yaml_data = yaml.safe_load(yaml_str)
        json_data = json.dumps(yaml_data, indent=2)
        return json_data
    except yaml.YAMLError as e:
        return f"Erro ao processar YAML: {e}"

# Exemplo de uso
yaml_string = """
key1: value1
key2:
  - item1
  - item2
key3:
  subkey1: subvalue1
"""

json_result = yaml_to_json(yaml_string)
print(json_result)
