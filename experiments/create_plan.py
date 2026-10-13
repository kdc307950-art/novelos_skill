import json
from pathlib import Path

def create(path=Path('experiments/tasks.jsonl')):
    kinds = [('continuity_test', 'continuity'), ('character_test', 'character'), ('structure_test', 'structure'), ('literary_test', 'literary'), ('editing_value_test', 'commercial')]
    rows = []
    for index in range(1, 21):
        name, task_type = kinds[(index - 1) % len(kinds)]
        rows.append({'id': f'EXP-{index:03d}', 'name': f'{name}_{index:03d}', 'dataset': 'golden_dataset/pending', 'baseline': 'same_model_without_novel_os', 'novelos_version': '3.8.0', 'metrics': ['accuracy', 'quality', 'human_score'], 'task_type': task_type, 'status': 'planned', 'notes': 'synthetic pending task; requires fixed model run and blind human evaluation'})
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(''.join(json.dumps(row, ensure_ascii=False) + '\n' for row in rows), encoding='utf-8')
    return len(rows)

if __name__ == '__main__':
    print(f'planned {create()} experiments')
