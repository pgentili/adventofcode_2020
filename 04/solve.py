import re

REQUIRED_FIELDS = set(['byr',
                       'iyr',
                       'eyr',
                       'hgt',
                       'hcl',
                       'ecl',
                       'pid'])

def parse_passports(text):
    pp_texts = [pp_text for pp_text in text.split('\n\n')]
    passports = []
    for pp_text in pp_texts:
        entries = re.split(r'\s+', pp_text)
        passport = {}
        for entry in entries:
            key, val = entry.split(':')
            passport[key] = val
        passports.append(passport)
    return passports

def validate_passport_1(passport):
    return REQUIRED_FIELDS.issubset(set(passport.keys()))

def validate_passport_2(passport):
    if not REQUIRED_FIELDS.issubset(set(passport.keys())):
        return False
    
    # check required conditions
    if not (1920 <= int(passport['byr']) <= 2002 and
            2010 <= int(passport['iyr']) <= 2020 and
            2020 <= int(passport['eyr']) <= 2030):
        return False

    if not passport['hgt'].endswith('cm') and not passport['hgt'].endswith('in'):
        return False
    try:
        height = int(passport['hgt'][:-2])
    except:
        return False
    if not (
        (passport['hgt'].endswith('cm') and 150 <= height <= 193) or
        (passport['hgt'].endswith('in') and 59 <= height <= 76)
    ):
        return False

    if not re.fullmatch(r'#[0-9a-f]{6}', passport['hcl']):
        return False
    
    if passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False
    
    if not re.fullmatch(r'[0-9]{9}', passport['pid']):
        return False
    
    return True

if __name__ == '__main__':
    with open('input.txt') as f:
        text = f.read()
    
    passports = parse_passports(text.rstrip('\n'))
    print(sum([validate_passport_1(passport) for passport in passports]))
    print(sum([validate_passport_2(passport) for passport in passports]))
