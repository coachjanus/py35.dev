"""
todo/model.py: Class Todo model
This module provides the To-Do database functionality.
"""

import datetime

class Todo:

    DONE = chr(9989)
    PENDING = chr(10060)
    
    COLORS = {
        'Learn': 'yellow', 
        'Work': 'red', 
        'Sports': 'cyan', 
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
    
    todo = {
        "task": None,
        "category": None,
        "added_at": None,
        "completed_at": None,
        "status": None,
        "position":None
        }
    
    def __init__(self, task, category, 
                 added_at=None,
                 completed_at= None,
                 status=None,
                 position=None
                 ) -> None:
        
        self.task = Todo.endswith_sentence(task)
        self.category = category
        self.added_at = added_at if added_at is not None else datetime.datetime.now().isoformat()
        self.completed_at = completed_at if completed_at is not NameError else None
        self.status = status if status is not None else 1 # 1 - open
        self.position = position if position is not None else None

    @classmethod
    def endswith_sentence(cls, task):
        if not task.endswith("."):
            task += "."
        return task

    def to_dict(self):
        return {
            'task': self.task,
            'category': self.category,
            'added_at': self.added_at,
            'completed_at': self.completed_at,
            'status': self.status,
            'position': self.position
        }
    
    def __repr__(self):
        return str(self.to_dict())
