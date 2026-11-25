# Tree Layout Visualizer

[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github)](https://github.com/Olamideakinade/layout-tree-viz)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

![Project Snapshot](preview.svg)

A tool to transform flat list inputs (parent-child pairs) into hierarchical tree visualizations in the terminal.

## Capabilities
- Converts adjacency list format to visual trees.
- Detects circular dependencies.
- Support for custom depth markers.
- Zero-dependency implementation.

## Quickstart
```bash
pip install .
python main.py --input "A,B;B,C;A,D"
```

## Architecture
- `engine.py`: Handles the recursive tree building and cycle detection.
- `cli.py`: Argument parsing and formatted output stream.
- `tests/`: Unit tests for algorithmic edge cases.

## License
MIT