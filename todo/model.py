import datetime

class Todo:
    # pass

    DONE = chr(9989)
    PENDING = chr(10060)

    COLORS = {
        'Learn': 'yellow',
        'Work': 'red',
        'Sport': 'cyan',
        'Study': 'green'
    }

    keys = ['name', 'style', 'width', 'min_width', 'justify']

    values = [
        ["#", "dim", 6, None, "left"],
        ["Todo", None, None, 20, "left"],
        ["Category", None, None, 12, "right"],
        ["Done", None, None, 12, "right"],
    ]

    @staticmethod
    def make_header():
        headers = []
        for v in Todo.values:
            d = dict(zip(Todo.keys, v))
            headers.append(d)
        return headers
    
    @staticmethod
    def get_category_color(category):
        if category in Todo.COLORS:
            return Todo.COLORS[category]
        return 'white'
        
    def __init__(self, task, category, added_at=None, completed_at=None, status=None, position=None):
        self._task = task
        self._category = category
        self._added_at = added_at if added_at is not None else datetime.datetime.now().isoformat()
        self._completed_at = completed_at if completed_at is not NameError else None
        self._status = status if status is not None else 1
        self._position = position if position is not None else None 

    def __repr__(self):
        return f"({self._task}, {self._category}, {self._added_at}, {self._completed_at}, {self._status}, {self._position})"

    


