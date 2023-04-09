base_rate = 5.5
far_east_regions = ['Камчатский край', 'Приморский край', 'Хабаровский край']
region = input('Введите регион: ')
num_children = int(input('Введите количество детей: '))
has_salary_project = input('Есть ли у вас зарплатный проект в банке? (да/нет): ')
has_insurance = input('Оформляется ли страхование в этом банке? (да/нет): ')

if num_children > 3:
    base_rate -= 1

if has_salary_project == 'да':
    base_rate -= 0.5


if has_insurance == 'да':
    base_rate -= 1.5
if region in far_east_regions:
    base_rate = 2    

print('Финальная процентная ставка:', base_rate, '%')

