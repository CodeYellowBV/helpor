def add_orderings(target: dict) -> dict:
    next_ordering = 0
    for value in target.values():
        if isinstance(value, dict):
            if 'type' in value and isinstance(value['type'], str):
                value['ordering'] = next_ordering
                next_ordering += 1
            add_orderings(value)
    return target
