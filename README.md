# Python-Project
## Objective:
The project aims to simulate the functionalities of the Seaborn library for data visualization using custom-built methods. It provides a simplified implementation to plot graphs such as bar charts, scatter plots, line plots, count plots, heatmaps, and box plots through a console-based interface. This project helps users understand the inner workings of data visualization libraries by interacting with dynamic inputs.

## Features
- Dynamic graph creation with user input.
- Supports bar charts, scatter plots, line plots, count plots, heatmaps, and box plots.
- Fully console-based visualization.

---

## Workflow
Below is the flowchart depicting the workflow of the project:

```mermaid
graph TD
    A[Start] --> B[Initialize Seaborn Class]
    B --> C[Set Style]
    B --> D[Set Color Palette]
    D --> E[Create Figure]
    E --> F[Create Axes]
    F --> G[Set Title]
    G --> H[User Selects Plot Type]
    H -->|Bar| I[Bar Plot Logic]
    H -->|Scatter| J[Scatter Plot Logic]
    H -->|Line| K[Line Plot Logic]
    H -->|Count| L[Count Plot Logic]
    H -->|Heatmap| M[Heatmap Logic]
    H -->|Box| N[Box Plot Logic]
    I --> O[Add Plot to Axes]
    J --> O
    K --> O
    L --> O
    M --> O
    N --> O
    O --> P[Display Figure]
    P --> Q[End]




