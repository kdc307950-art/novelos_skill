import hashlib
import re
import unicodedata

def normalize(text):
    return re.sub(r'\s+', ' ', unicodedata.normalize('NFKC', text)).strip()

def text_hash(text):
    return hashlib.sha256(normalize(text).encode('utf-8')).hexdigest()

def quality(record, min_chars=200):
    content = normalize(record.get('text', '') + ' ' + record.get('context', ''))
    if len(content) < min_chars:
        return False, 'short_context'
    if '\ufffd' in content or not any(c.isalpha() for c in content):
        return False, 'invalid_text'
    if not record.get('question') or not record.get('answer'):
        return False, 'missing_qa'
    return True, 'accepted_for_review'
