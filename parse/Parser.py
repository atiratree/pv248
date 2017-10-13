import re
from metadata.regex_store import RegexStore
from functools import partial


class Parser:
    @staticmethod
    def parse(line, block):
        return Parser.__lookup_person(line, RegexStore.composers, block.add_composer) or \
               Parser.__lookup_person(line, RegexStore.editors, block.add_editor) or \
               Parser.__lookup_score_attr(line, RegexStore.genre, block, 'genre') or \
               Parser.__lookup_score_attr(line, RegexStore.key, block, 'key') or \
               Parser.__lookup_score_attr(line, RegexStore.composition, block, 'year') or \
               Parser.__lookup_score_attr(line, RegexStore.incipit, block, 'incipit') or \
               Parser.__lookup_voice(line, partial(block.add_voice, block.score)) or \
               Parser.__lookup_edition(line, block) or \
               Parser.__lookup_print_number(line, block) or \
               Parser.__lookup_partiture(line, block)

    @staticmethod
    def __lookup_person(line, people_regex, callback):
        reg_res = people_regex.match(line)
        if reg_res:
            people = reg_res.group(1)
            for person in people.split(';'):
                years_reg = RegexStore.years.match(person)
                born, died = None, None
                if years_reg:
                    if years_reg.lastindex >= 1:
                        born = years_reg.group(1)
                    if years_reg.lastindex >= 2:
                        died = years_reg.group(2)

                clean_name = re.sub(RegexStore.clean_name, '', person.strip())
                if not clean_name:
                    continue
                callback(clean_name, born, died)
        return reg_res

    @staticmethod
    def __lookup_score_attr(line, regex, block, attr_name):
        reg_res = regex.match(line)
        if reg_res:
            value = reg_res.group(1).strip()
            if value:
                setattr(block.score, attr_name, value)
        return reg_res

    @staticmethod
    def __lookup_voice(line, callback):
        reg_res = RegexStore.voice.match(line)
        if reg_res:
            number = reg_res.group(1).strip()
            name = reg_res.group(2).strip()
            callback(name, number)
        return reg_res

    @staticmethod
    def __lookup_edition(line, block):
        reg_res = RegexStore.edition.match(line)
        if reg_res:
            name = reg_res.group(1).strip()
            if not name:
                return reg_res
            yr_regex = RegexStore.year.match(name)
            if yr_regex:
                block.edition.year = yr_regex.group(1)

            block.edition.name = name
        return reg_res

    @staticmethod
    def __lookup_print_number(line, block):
        reg_res = RegexStore.print_number.match(line)
        if reg_res:
            block.partiture.id = reg_res.group(1).strip()
        return reg_res

    @staticmethod
    def __lookup_partiture(line, block):
        reg_res = RegexStore.partiture.match(line)
        if reg_res:
            value = reg_res.group(1).strip()
            if value == 'no':
                block.partiture.partiture = 'N'
            elif value == 'yes':
                block.partiture.partiture = 'Y'
            else:
                block.partiture.partiture = 'P'
        return reg_res
