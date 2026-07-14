import csv
import datetime as dt


def read_tasks_from_csv(file_path):
    """Read tasks from a CSV file and return a list of task dictionaries."""
    tasks = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            start_time_str = row.get('start_date').strip()
            start_time = dt.datetime.strptime(start_time_str, '%Y-%m-%dT%H:%M')
            print(start_time)
            title = row.get('title').strip()
            description = row.get('description').strip()
            completed = row.get('completed', '0').strip() == '1'
            tasks.append({
                'title': title,
                'description': description,
                'completed': completed,
                'start_time': start_time,
            })
            tasks.sort(key=lambda x: x['start_time'])
    return tasks