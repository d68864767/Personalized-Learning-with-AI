```python
# content_creation_toolkit.py

import os
import json
from config import TOOLKIT_DIR

class ContentCreationToolkit:
    def __init__(self):
        self.toolkit_dir = TOOLKIT_DIR

    def create_course(self, course_name, course_description, created_by):
        course = {
            'course_name': course_name,
            'course_description': course_description,
            'created_by': created_by,
            'lessons': []
        }
        course_file = os.path.join(self.toolkit_dir, f"{course_name.replace(' ', '_').lower()}.json")
        with open(course_file, 'w') as file:
            json.dump(course, file)
        print(f"Course '{course_name}' created successfully.")

    def add_lesson(self, course_name, lesson_name, lesson_content):
        course_file = os.path.join(self.toolkit_dir, f"{course_name.replace(' ', '_').lower()}.json")
        if os.path.exists(course_file):
            with open(course_file, 'r') as file:
                course = json.load(file)
            course['lessons'].append({
                'lesson_name': lesson_name,
                'lesson_content': lesson_content
            })
            with open(course_file, 'w') as file:
                json.dump(course, file)
            print(f"Lesson '{lesson_name}' added to course '{course_name}' successfully.")
        else:
            print(f"Course '{course_name}' not found.")

    def view_course(self, course_name):
        course_file = os.path.join(self.toolkit_dir, f"{course_name.replace(' ', '_').lower()}.json")
        if os.path.exists(course_file):
            with open(course_file, 'r') as file:
                course = json.load(file)
            print(json.dumps(course, indent=4))
        else:
            print(f"Course '{course_name}' not found.")
```
