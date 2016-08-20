import unittest
import os.path
import json


class Tests(unittest.TestCase):
    def _getTarget(self):
        from gron import gron
        return gron

    def _related_path(self, filename):
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)

    def _get_answer(self, filename):
        with open(self._related_path(filename)) as rf:
            return rf.read().strip()

    def _callFUT(self, filename):
        with open(self._related_path(filename)) as rf:
            data = json.load(rf)
        return self._getTarget()(data)

    def test_one(self):
        target_file = "./data/one.json"
        answer_file = "./data/one-answer.json"

        result = self._callFUT(target_file)
        expected = self._get_answer(answer_file)
        result = "\n".join(result)
        self.assertEqual(result, expected)
