KEYWORDS = {
    'continuity': ('时间线', '冲突', '记得', '受伤', '失明', '死亡'),
    'character': ('动机', '人物', '心理', '成长', '选择', '欲望'),
    'structure': ('章节', '钩子', '高潮', '转折', '场景', '节奏'),
    'literary': ('主题', '象征', '反讽', '意象', '叙事声音'),
    'commercial': ('读者', '爽点', '追读', '付费', '开篇', '信息差'),
    'failure': ('错误', '失败', '工具化', '幻觉', '过度解读', '缺少铺垫'),
}

def classify(text: str):
    scores = {category: sum(text.count(word) for word in words) for category, words in KEYWORDS.items()}
    category, value = max(scores.items(), key=lambda item: item[1])
    total = sum(scores.values())
    return {'category': category, 'confidence': round(value / max(total, 1), 3), 'scores': scores}
