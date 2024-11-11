import re

class Kata():
    def __init__(self, kata: str, index: str = '0', surat: str = 'query', surat_id: int = 0, ayat: int = 0, ayat_id: int = 0):
        self.kata: str = kata
        self.index: str = index
        self.surat: str = surat
        self.surat_id: int = surat_id
        self.ayat: int = ayat
        self.ayat_id: int = ayat_id
        self.similarity: float = 0.00
        
    @property
    def normalized(self) -> str:
        normalized: str = self.kata.lower()
        # Normalisasi huruf ain dan hamzah mati menjadi 'k'
        normalized = re.sub(r"\b'([^aiu])", r'k\1', normalized)
        normalized = re.sub(r'\b`([^aiu])', r'k\1', normalized)
        
        # Penghilangan 'al` hamzah hidup
        normalized = re.sub(r'\bal`', '', normalized)
        # Penghilangan petik
        normalized = normalized.replace("'", '').replace('`', '')
        
        # Alif Lam Syamsiah and tasdid removal
        normalized = re.sub(r'\b(a)l([t,s,d,z,r,d,l,n])', r'\1\2', normalized)
        normalized = re.sub(r'\b([^aiu][aiu])l([t,s,d,z,r,d,l,n])', r'\1\2', normalized)

        # Remove all symbols
        normalized = re.sub(r'[()-`]', '', normalized)
        
        # Other substitutions based on specific phonetic mappings
        substitutions: dict[str, str] = {
            'iyy': 'i', 
            'kh': 'h', 
            'sh': 's', 
            'ts': 's', 
            'sy': 's',
            'dz': 'z', 
            'zh': 'z', 
            'dh': 'd', 
            'th': 't', 
            'q': 'k',
            'aw': 'au', 
            'ay': 'ai', 
            'v': 'f', 
            'p': 'f', 
            'j': 'z',
            'ng': 'n', 
            'nb': 'mb', 
            'ny': 'y', 
            'nw': 'w', 
            'nm': 'm', 
            'nn': 'n', 
            'nl': 'l', 
            'nr': 'r'
        }
        
        for pattern, replacement in substitutions.items():
            normalized = normalized.replace(pattern, replacement)

        return normalized
    
    @property
    def phonetic_code(self) -> str:
        # Reference: TA Sukma Rahadian string matching soundex dan metaphone 113030012 (2007)
        encoding_map: dict[str, str] = {
            'a': '/',
            'e': '/',
            'i': '/',
            'o': '/',
            'u': '/',
            'h': '/',
            'y': '/',
            'b': '0',
            'p': '0',
            'c': '1',
            'j': '1',
            's': '1',
            'x': '1',
            'z': '1',
            'd': '2',
            'f': '3',
            'v': '3',
            'g': '4',
            'k': '4',
            'q': '4',
            'l': '5',
            'm': '6',
            'n': '7',
            'r': '8',
            't': '9',
            'w': 'w'
        }
        
        encoded: str = ''.join(encoding_map.get(char, '') for char in self.normalized)
        result: list[str] = [encoded[0]]
        for i in range(1, len(encoded)):
            if encoded[i] != encoded[i - 1]:
                result.append(encoded[i])
        encoded: str = ''.join(result)

        phonetic_code: str = self.normalized[0] + encoded[1:]
        phonetic_code: str = phonetic_code.replace('/', '') + '***'
        return phonetic_code[:4]