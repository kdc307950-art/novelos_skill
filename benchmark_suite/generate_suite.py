import argparse
import json
from pathlib import Path

QUOTAS = {'continuity': 1000, 'character': 700, 'structure': 500, 'literary': 400, 'commercial': 300, 'failure': 100}
TEMPLATES = {
    'continuity': ('C{n}: character state conflicts with C{m}.', 'Find the time, state, world-rule or foreshadowing conflict and cite both facts.'),
    'character': ('A character changes a long-held position under pressure in C{n}.', 'Explain motivation, psychology, evidence and growth.'),
    'structure': ('A chapter contains setup but no conflict or irreversible choice in C{n}.', 'Assess goal, conflict, pacing, turning point and hook.'),
    'literary': ('An image repeats with a changed meaning in C{n}.', 'Analyze theme, symbol, irony and emotional aftertaste without overclaiming.'),
    'commercial': ('The opening promises a deadline but delays action for five scenes in C{n}.', 'Assess hook, reader expectation, retention risk and an actionable fix.'),
    'failure': ('An analyst makes a confident claim from one weak clue in C{n}.', 'Identify failure, root cause and a testable correction.'),
}

def generate(out: Path):
    out.mkdir(parents=True, exist_ok=True)
    total = 0
    for category, count in QUOTAS.items():
        with (out / f'{category}.jsonl').open('w', encoding='utf-8') as handle:
            for index in range(1, count + 1):
                text, question = TEMPLATES[category]
                record = {'id': f'BMS-{category.upper()}-{index:04d}', 'category': category, 'input': text.format(n=index, m=index + 40), 'question': question, 'expected': 'synthetic pending case; human verification required', 'status': 'pending', 'source': 'synthetic', 'license': 'MIT', 'split': 'test' if index % 10 == 0 else 'validation' if index % 10 == 1 else 'train'}
                handle.write(json.dumps(record, ensure_ascii=False) + '\n')
                total += 1
    return total

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', type=Path, default=Path('benchmark_suite/pending'))
    args = parser.parse_args()
    print(f'generated {generate(args.out)} pending benchmark cases')
