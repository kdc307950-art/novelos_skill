import json
import tempfile
import unittest
from pathlib import Path
from crawler.cleaner import text_hash, quality
from crawler.downloader import download
from crawler.build_dataset import build
from crawler.validate_dataset import validate

class DatasetTests(unittest.TestCase):
    def test_normalized_dedup(self):
        self.assertEqual(text_hash('Ａ  story\ntext'), text_hash('A story text'))

    def test_no_label_fabrication_and_group_split(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            src = root / 'input.json'
            src.write_text(json.dumps([{'document_id':'book1','text':'A long context. '*30,'q':'Why?','a':'Because.'},
                {'document_id':'book1','text':'A long context. '*30,'q':'Who?','a':'A.'},
                {'document_id':'book1','text':'A long context. '*30,'q':'Who?','a':'A.'}]), encoding='utf-8')
            out = root / '01_Continuity' / 'cases.jsonl'
            stats = build(src, {'text':'text','question':'q','answer':'a'},
                {'status':'approved','data_license':'MIT','commit':'a'*40,'url':'test:source'}, '01_Continuity', out)
            self.assertEqual(stats['accepted'], 2)
            self.assertEqual(stats['rejected'], {'duplicate':1})
            cases = [json.loads(s) for s in out.read_text(encoding='utf-8').splitlines()]
            self.assertEqual(cases[0]['metadata']['split'], cases[1]['metadata']['split'])
            self.assertEqual(cases[0]['labels'], {})
            self.assertFalse(cases[0]['verified'])
            self.assertEqual(validate(root)['errors'], [])

    def test_download_license_gate(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                download({'status':'pending'}, Path(tmp))
            with self.assertRaises(ValueError):
                download({'status':'approved','data_license':'MIT','commit':'main'}, Path(tmp))

    def test_missing_answer_rejected(self):
        self.assertFalse(quality({'text':'a'*300,'question':'q'})[0])

    def test_published_seeds(self):
        root = Path(__file__).resolve().parents[2] / 'dataset' / 'literary_benchmark'
        result = validate(root)
        self.assertEqual(result['errors'], [])
        self.assertEqual(len(result['categories']), 6)

if __name__ == '__main__':
    unittest.main()
