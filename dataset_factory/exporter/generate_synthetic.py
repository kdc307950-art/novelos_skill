"""Generate transparent, synthetic benchmark seeds for human review."""
import argparse
import json
from pathlib import Path

QUOTAS = {'01_Continuity': 200, '02_Character': 200, '03_Structure': 200, '04_Literary': 150, '05_Commercial': 150, '06_Failure': 100}
TEMPLATES = {
    '01_Continuity': ('第{n}章记录角色失去右手，第{m}章角色双手弹琴。', '检查身体状态与后续行为是否冲突，引用两处事实并给出解释或修复。', '存在待核实的连续性冲突；需要假肢、再生规则或改写行为的证据。'),
    '02_Character': ('角色在前文长期拒绝权威，第{m}章突然服从命令。', '判断转变是否有动机和压力节点。', '需要寻找触发器、内在需求和可见选择；没有证据时标记为人物转变缺口。'),
    '03_Structure': ('本章连续三个场景都在解释背景，主角没有行动，章末没有新问题。', '检查目标、冲突、推进和钩子。', '结构推进不足；应把背景嵌入行动或补充不可逆选择。'),
    '04_Literary': ('雨在离别和重逢场景反复出现，但语义逐渐改变。', '分析主题、象征和叙事功能，区分事实与候选解读。', '可以提出反复意象和语义变化的候选解释；不能把单一意象断言为唯一主题。'),
    '05_Commercial': ('开篇承诺七日破案，连续五章没有线索、期限压力或主角主动行为。', '预测追读风险并给可验证的优化建议。', '承诺兑现延迟会增加流失风险；建议前置行动并用读者数据验证，不能伪造精确概率。'),
    '06_Failure': ('分析器看到一次雨景就断言其象征时代压迫，并给文学分9.8。', '识别错误类型、原因和修正。', '这是过度解读和虚假精确；应降低置信度、请求更多证据并解释评分标尺。'),
}

def generate(out: Path):
    out.mkdir(parents=True, exist_ok=True)
    total = 0
    for category, count in QUOTAS.items():
        path = out / f'{category}.jsonl'
        with path.open('w', encoding='utf-8') as handle:
            for index in range(1, count + 1):
                text, task, answer = TEMPLATES[category]
                record = {'id': f'GOLD-{category}-{index:04d}', 'text': text.format(n=index, m=index + 10), 'task': task, 'expected_answer': answer, 'reasoning_summary': 'synthetic seed; requires human review', 'labels': {}, 'source': 'synthetic', 'license': 'MIT', 'confidence': 0.35, 'status': 'pending', 'category': category, 'annotation_id': None}
                handle.write(json.dumps(record, ensure_ascii=False) + '\n')
                total += 1
    return total

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--out', type=Path, default=Path('golden_dataset/pending'))
    args = p.parse_args()
    print(f'generated {generate(args.out)} pending synthetic cases')
