from typing import List, Dict, Any, NamedTuple

class DBResponse(NamedTuple):
    todo_list: List[Dict[str, Any]]
    error: int