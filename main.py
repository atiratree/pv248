from collections import Counter
import re
import sqlite3


def to_century(number):
    return (int(number) // 100) + 1


def update_composers(composers_regex, line, counter):
    composer_regex = composers_regex.match(line)
    if composer_regex:
        composers = composer_regex.group(1)
        for composer in composers.split(';'):
            clean_composer = re.sub(r"\([0-9-/+]*\)", '', composer.strip())
            if not clean_composer:
                continue
            counter[clean_composer] += 1


def update_centuries(years_regex, year_regex, line, counter):
    years_matched = years_regex.match(line)
    if years_matched:
        matched_year = year_regex.match(years_matched.group(1))
        if matched_year:
            year = to_century(matched_year.group(1))
            counter[year] += 1


def update_keys(key_regex, line, counter):
    keys_matched = key_regex.match(line)
    if keys_matched:
        for key in re.split(';|,', keys_matched.group(1)):
            key = key.strip()
            if key:
                counter[key] += 1


def print_counter(counter, text='Counter printed'):
    print('\n' + text + '\n')
    for key in sorted(counter.keys()):
        print("{0}: {1}".format(key, counter[key]))


def main():
    f = open('scorelib.txt', 'r')
    composers_regex = re.compile(r"Composer: (.*)")
    composition_year_regex = re.compile(r"Composition Year: (.*)")
    key_regex = re.compile(r"Key: (.*)")
    year_regex = re.compile(r".*([0-9]{4})")

    composers_count = Counter()
    century_count = Counter()
    keys_count = Counter()

    for line in f:
        update_composers(composers_regex, line, composers_count)
        update_centuries(composition_year_regex, year_regex, line, century_count)
        update_keys(key_regex, line, keys_count)

    # print_counter(composers_count, "Composers")
    # print_counter(century_count, "Centuries")
    print_counter(keys_count, "Keys")


main()
