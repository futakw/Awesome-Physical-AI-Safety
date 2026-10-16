# Research Landscape

These views are generated from the structured metadata in [`data/papers.json`](../../data/papers.json). They describe the current catalog rather than the full publication volume of the field.

For hoverable paper lists, open the [interactive explorer](../index.html#heatmap). Each README preview links directly to its corresponding view.

## Field Timeline

![Timeline of research areas](../visualizations/field-timeline.svg)

Bubble area encodes the number of cataloged papers in each area-year cell.

## Submission Growth

![Cumulative papers by first submission date](../visualizations/submission-growth.svg)

The line uses verified initial submission dates, such as arXiv v1 dates. Unknown dates are excluded.

## Threat-Model Cross-Map

![Threat mechanism and surface heatmap](../visualizations/threat-heatmap.svg)

The heatmap includes concrete threat models and excludes broad survey/evaluation coverage. Multi-label papers contribute to every applicable mechanism-surface pair.

## Threat Mechanism × Evaluated Risk

![Threat mechanism and evaluated risk heatmap](../visualizations/threat-risk-heatmap.svg)

Rows follow the same top threat-mechanism order as the Threat Cross-Map. Columns are the four evidence-coded `risks` outcomes; a paper contributes only when it reports a corresponding empirical metric.

## Defense Mechanism × Defended Threat

![Defense mechanism and defended threat heatmap](../visualizations/defense-heatmap.svg)

This view uses the optional `defense` extension across every primary section. It includes only substantive proposed or experimentally evaluated mitigations.

## Affected Target × Consequence

This interactive-only cross-map connects the affected component to the resulting failure or harm. Open the [Project Page](../index.html#target) to inspect and filter its paper table.

Static benchmark and evaluation-extension heatmaps are also generated for metadata review. They are not currently top-level Project Page navigation views.

## Regeneration

```bash
python3 scripts/build_visualizations.py
python3 scripts/build_visualizations.py --check
python3 scripts/build_explorer.py
```
