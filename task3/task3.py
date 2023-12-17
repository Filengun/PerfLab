import json

def update_values(tests: dict, values: dict) -> None:
    """Обновление значений."""
    if isinstance(tests, dict):
        for key, value in tests.items():
            if key == 'id' and value in values:
                tests['value'] = values[value]
            else:
                update_values(value, values)
    elif isinstance(tests, list):
        for item in tests:
            update_values(item, values)

def generate_report(tests_file: str, values_file: str,
                    report_file: str) -> None:
    """Создание файла report с обновленными данными."""
    with open(tests_file, 'r') as f:
        tests = json.load(f)
    with open(values_file, 'r') as f:
        values = {item['id']: item['value'] for item in json.load(f)['values']}
    update_values(tests, values)
    with open(report_file, 'w') as f:
        json.dump(tests, f, ensure_ascii=False, indent=4)

generate_report('tests.json', 'values.json', 'report.json')