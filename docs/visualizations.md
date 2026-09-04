# Research Landscape

These views are generated from the structured metadata in [`data/papers.json`](../data/papers.json). They describe the current catalog rather than the full publication volume of the field.

## Taxonomy Map

![Taxonomy map of the paper catalog](../assets/visualizations/topic-map.svg)

This projection uses risk, threat-model, and scope labels. It exposes metadata similarity and should not be interpreted as a semantic embedding of paper abstracts.

## Topic Trends

![Annual paper counts by research area](../assets/visualizations/topic-trends.svg)

The final year is an incomplete snapshot. Counts also reflect the repository's curation coverage.

## Field Timeline

![Timeline of research areas](../assets/visualizations/field-timeline.svg)

Bubble area encodes the number of cataloged papers in each area-year cell.

## Threat-Model Cross-Map

![Threat mechanism and surface heatmap](../assets/visualizations/threat-heatmap.svg)

The heatmap includes concrete threat models and excludes broad survey/evaluation coverage. Multi-label papers contribute to every applicable mechanism-surface pair.

## Regeneration

```bash
python3 scripts/build_visualizations.py
python3 scripts/build_visualizations.py --check
```
