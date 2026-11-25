from typing import Dict, List, Set, Optional

class TreeBuilder:
    def __init__(self, data: List[tuple]):
        self.nodes: Dict[str, List[str]] = {}
        self.roots: Set[str] = set()
        self._build(data)

    def _build(self, data: List[tuple]) -> None:
        all_children = set()
        for parent, child in data:
            if parent not in self.nodes:
                self.nodes[parent] = []
            self.nodes[parent].append(child)
            all_children.add(child)
            if parent not in all_children:
                self.roots.add(parent)
        
        for child in all_children:
            if child not in self.nodes and child in self.roots:
                self.roots.remove(child)

    def render(self, node: str, prefix: str = "", is_last: bool = True) -> str:
        output = f"{prefix}{'└── ' if is_last else '├── '}{node}\n"
        children = self.nodes.get(node, [])
        new_prefix = prefix + ("    " if is_last else "│   ")
        for i, child in enumerate(children):
            output += self.render(child, new_prefix, i == len(children) - 1)
        return output