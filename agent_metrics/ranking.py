def rank(summary):
    return sorted(({'agent': name, **metrics} for name, metrics in summary.items()), key=lambda row: (row['gain'] is not None, row.get('gain') or 0), reverse=True)
