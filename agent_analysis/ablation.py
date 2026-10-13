CONFIGS = {
    'baseline': [],
    'memory': ['memory'],
    'agents': ['structure', 'character', 'continuity', 'literary', 'commercial'],
    'full_novel_os': ['memory', 'debate', 'evaluation', 'structure', 'character', 'continuity', 'literary', 'commercial'],
}

def plan():
    return [{'name': name, 'components': components, 'status': 'planned'} for name, components in CONFIGS.items()]
