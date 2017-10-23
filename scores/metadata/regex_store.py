import re


def _build_key_regex(key):
    return re.compile(re.escape(key) + r': (.*)')


class RegexStore:
    # people
    composers = _build_key_regex('Composer')
    editors = _build_key_regex('Editor')
    years = re.compile(r'.*(\d{4}).+(\d{4}).*')
    clean_name = re.compile(r'\([0-9-/+]*\)')

    # score attributes
    genre = _build_key_regex('Genre')
    key = _build_key_regex('Key')
    composition = _build_key_regex('Composition Year')
    incipit = _build_key_regex('Incipit')

    # voice
    voice = re.compile(r'Voice (\d*): (.*)')

    # edition
    edition = _build_key_regex('Edition')
    year = re.compile(r'.*(\d{4}).*')

    # print
    print_number = _build_key_regex('Print Number')
    partiture = _build_key_regex('Partiture')
