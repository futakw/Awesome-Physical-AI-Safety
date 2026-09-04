# Research Landscape

These views are generated from the structured metadata in [`data/papers.json`](../data/papers.json). They describe the current catalog rather than the full publication volume of the field.

For hoverable paper lists, open the [interactive explorer](index.html). GitHub README markdown cannot execute JavaScript, so the README keeps a static preview and links to this page.

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
python3 scripts/build_explorer.py
```
