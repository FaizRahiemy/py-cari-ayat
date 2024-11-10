import re

class Kata():
    def __init__(self, kata: str = ''):
        self.kata: str = kata
        
    @property
    def normalized(self) -> str:
        # Normalisasi huruf ain dan hamzah mati menjadi 'k'
        normalized: str = re.sub(r"\b'([^aiu])", r'k\1', self.kata)
        normalized = re.sub(r"\b`([^aiu])", r'k\1', normalized)
        
        # Penghilangan 'al` hamzah hidup
        normalized = re.sub(r"\bal`", '', normalized)
        # Penghilangan petik
        normalized = normalized.replace("'", '').replace("`", '')
        
        # Alif Lam Syamsiah and tasdid removal
        normalized = re.sub(r"\b(a)l([t,s,d,z,r,d,l,n])", r"\1\2", normalized)
        normalized = re.sub(r"\b([^aiu][aiu])l([t,s,d,z,r,d,l,n])", r"\1\2", normalized)
        
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