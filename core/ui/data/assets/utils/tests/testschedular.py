import unittest
from core.scheduler import generate_schedule

class TestScheduler(unittest.TestCase):
    def setUp(self):
        self.sample_tasks = [
            {
                "id": "1",
                "name": "Task A",
                "subject": "Math",
                "duration": 2,
                "deadline": "2025-07-20",
                "priority": 5,
                "difficulty": 3
            },
            {
                "id": "2",
                "name": "Task B",
                "subject": "History",
                "duration": 1.5,
                "deadline": "2025-07-19",
                "priority": 4,
                "difficulty": 2
            }
        ]

    def test_schedule_generation(self):
        schedule = generate_schedule(self.sample_tasks)
        self.assertTrue(len(schedule) > 0)
        self.assertIn("start_time", schedule[0])
        self.assertIn("name", schedule[0])

if __name__ == '__main__':
    unittest.main()
