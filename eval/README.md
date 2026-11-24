# Evaluation data

Gold annotations and question sets used by `gloss-eval`. Planned layout:

```
eval/datasets/
├── dedup_pairs.jsonl        1.  known duplicate / non-duplicate pairs
├── parse_gold/              2.  LaTeX-derived structure per paper
├── questions.jsonl          3.  question, relevant chunk ids, reference answer
├── entities_gold.jsonl      4.  hand-labelled mentions + linked ids
└── defects.jsonl            5.  synthetic defects injected per paper
```

Annotations are small, hand-made and committed, while source documents are not.
