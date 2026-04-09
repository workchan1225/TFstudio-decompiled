# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: rhymes.pyc (Python 3.11)

from eng_to_ipa.transcribe import mode_type, get_cmu, preprocess

def remove_onset(word_in):
    phone_list = get_cmu([
        word_in])[0][0].split(' ')
    for i, phoneme in enumerate(phone_list):
        if '1' in phoneme:
            
            return None, ' '.join(phone_list[i:])
        return None


def get_rhymes(word, mode = ('sql',)):
    if len(word.split()) > 1:
        return word.split()()
    phones = None(preprocess(word))
    phones_full = get_cmu([
        preprocess(word)])[0][0]
    if mode == 'sql':
        c = mode_type(mode)
        c.execute('SELECT word, phonemes FROM dictionary WHERE phonemes LIKE "%{0}" AND NOT word="{1}" '.format(phones, word) + 'AND NOT phonemes="{0}"'.format(phones_full))
        return list(set((lambda .0: [ r[0] for r in .0 ])(c.fetchall()())))
    if None == 'json':
        r_list = []
        for key, val in mode_type(mode).items():
            for v in val:
                if v.endswith(phones) and word != key and v != phones_full:
                    r_list.append(key)
                return sorted(set(r_list))
                return None


def jhymes(word):
    '''Get rhymes with forced JSON mode.'''
    return get_rhymes(word, mode = 'json')

if __name__ == '__main__':
    test = 'testing'
    rhymes = get_rhymes(test)
    for rhyme in rhymes:
        print(rhyme)
        return None
        return None
