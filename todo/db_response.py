from typing import Any, Dict, List, NamedTuple

class DBResponse(NamedTuple):
    todo_list: List[Dict[str, Any]]
    error: int
