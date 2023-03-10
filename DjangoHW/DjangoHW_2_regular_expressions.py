# 1. Напишіть регулярний вираз, який знаходитиме в тексті фрагменти,
# що складаються з однієї літери R, за якою слідує одна або більше літер b, за якою одна r.
# Враховувати верхній та нижній регістр.

import re

string = 'Rbbbbbr bg rBBr RBbBbBr'

pattern = r'R[Bb]+r'

print(re.findall(pattern, string))

# 2. Напишіть функцію, яка виконує валідацію номера банківської картки (9999-9999-9999-9999).

import re

bankcard = '1234-5678-9012-3458'
pattern_sub = r'\D+'
pattern_search = r'^\d{16}$'
replace = ''

clean_bankcard = re.sub(pattern_sub, replace, bankcard)

if re.search(pattern_search, clean_bankcard):
    print(re.search(pattern_search, clean_bankcard).group())
else:
    print("pattern not found")


# 3. Напишіть функцію, яка приймає рядкові дані та виконує перевірку на їхню відповідність мейлу.
# Вимоги:
# -Цифри (0-9).
# -лише латинські літери у великому (A-Z) та малому (a-z) регістрах.
# -у тілі мейла допустимі лише символи "_" і "-". Але вони не можуть бути першим символом мейлу.
# -Символ "-" не може повторюватися.

import re

email = 'test.test@gmail.com'
pattern_search = r'^[0-9a-zA-Z]([\w\.]-?){1,63}@[0-9a-zA-Z]([\w\.]-?){1,63}$'

if re.search(pattern_search, email):
    print(re.search(pattern_search, email).group())
else:
    print("Email is not correct.")


# 4. Напишіть функцію, яка перевіряє правильність логіну. Правильний логін – рядок від 2 до 10 символів,
# що містить лише літери та цифри.

import re

login = 'Mfgd'
pattern_search = r'^[0-9a-zA-Z]{2,10}$'

if re.search(pattern_search, login):
    print(re.search(pattern_search, login).group())
else:
    print("Login is not correct.")
