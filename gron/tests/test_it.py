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

    def test_it(self):
        candidates = [
            ("./data/one.json", "./data/one-answer.json"),
            ("./data/two.json", "./data/two-answer.json"),
            ("./data/two-b.json", "./data/two-b-answer.json"),
            ("./data/three.json", "./data/three-answer.json"),
        ]

        for target_file, answer_file in candidates:
            with self.subTest(target_file=target_file, answer_file=answer_file):
                result = self._callFUT(target_file)
                expected = self._get_answer(answer_file)
                result = "\n".join(result)

                msg = "\n".join(["\n@result", result, "=", "@expected", expected])
                self.assertEqual(result, expected, msg=msg)
