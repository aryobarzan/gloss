from gloss_quality.checklist import ItemResult, coverage_score, load_checklist


def test_bundled_checklist_loads() -> None:
    checklist = load_checklist()
    assert checklist.name == "reproducibility"
    assert any(item.id == "code_available" for item in checklist.items)


def test_coverage_counts_only_required_items() -> None:
    checklist = load_checklist()
    required = [i.id for i in checklist.items if i.required]
    results = [ItemResult(item_id=required[0], satisfied=True)]
    results.append(ItemResult(item_id="limitations", satisfied=True))  # optional, ignored
    assert coverage_score(checklist, results) == 1 / len(required)
