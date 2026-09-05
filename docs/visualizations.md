# Research Landscape

These views are generated from the structured metadata in [`data/papers.json`](../data/papers.json). They describe the current catalog rather than the full publication volume of the field.

For hoverable paper lists, open the [interactive explorer](index.html). GitHub README markdown cannot execute JavaScript, so the README keeps a static preview and links to this page.

## Field Timeline

![Timeline of research areas](../assets/visualizations/field-timeline.svg)

Bubble area encodes the number of cataloged papers in each area-year cell.

## Threat-Model Cross-Map

![Threat mechanism and surface heatmap](../assets/visualizations/threat-heatmap.svg)

The heatmap includes concrete threat models and excludes broad survey/evaluation coverage. Multi-label papers contribute to every applicable mechanism-surface pair.

## Threat Mechanism × Evaluated Risk

![Threat mechanism and evaluated risk heatmap](../assets/visualizations/threat-risk-heatmap.svg)

Rows follow the same top threat-mechanism order as the Threat Cross-Map. Columns are the four evidence-coded `risks` outcomes; a paper contributes only when it reports a corresponding empirical metric.

## Defense Cross-Map

![Defense coverage map](../assets/visualizations/defense-heatmap.svg)

Rows are `defense.mechanism` values. Columns follow the same top threat-mechanism order as the Threat Cross-Map; mechanisms with no matching defense remain visible as empty columns.

## Benchmark Cross-Map

![Benchmark coverage map](../assets/visualizations/benchmark-heatmap.svg)

Rows are `threat_model.mechanism` values and columns are `threat_model.consequence` values for benchmark papers. Evaluation-style threat models use `coverage.mechanisms` and `coverage.consequences`.

## Evaluation Cross-Map

![Evaluation protocol map](../assets/visualizations/evaluation-heatmap.svg)

Rows are `evaluation.environments` values and columns are `evaluation.metrics` values. Only records enriched with the optional Evaluation extension are counted.

## Regeneration

```bash
python3 scripts/build_visualizations.py
python3 scripts/build_visualizations.py --check
python3 scripts/build_explorer.py
```
