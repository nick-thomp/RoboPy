import unittest
from unittest.mock import patch
from tasks import ClickTask

class TestClickTask(unittest.TestCase):
    
    def test_initialization(self):
        step_data = {'button': 'right', 'x': 100, 'y': 200}
        task = ClickTask(step_data)
        self.assertEqual(task.button, 'right')
        self.assertEqual(task.x, 100)
        self.assertEqual(task.y, 200)

    def test_missing_coordinates(self):
        step_data = {'button': 'left'}
        task = ClickTask(step_data)
        result = task.run()
        self.assertEqual(result['status'], 'error')
        self.assertEqual(result['message'], 'Missing coordinates for click')

    @patch('tasks.click.click')
    def test_successful_click(self, mock_click):
        step_data = {'button': 'left', 'x': 50, 'y': 50}
        task = ClickTask(step_data)
        result = task.run()
        mock_click.assert_called_once_with(x=50, y=50, button='left')
        self.assertEqual(result['status'], 'success')
        self.assertIn('left click at (50, 50)', result['message'])


    @patch('tasks.click.click', side_effect=Exception('Mock error'))
    def test_click_error_handling(self, mock_click):
        step_data = {'button': 'left', 'x': 50, 'y': 60}
        task = ClickTask(step_data)
        result = task.run()
        self.assertEqual(result['status'], 'error')
        self.assertIn('Error: Mock error', result['message'])

if __name__ == '__main__':
    unittest.main()