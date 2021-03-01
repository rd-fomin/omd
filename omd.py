def choose_option():
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        option = input('Введите вариант ({}/{}): '.format(*options))
        if option not in options:
            print('Команда {0} не поддерживается.'.format(option))
    return options[option]


def start():
    print(
       'Это симулятор утки-маляра\n'
       'Вы хотите погулять. Пойдете ли вы гулять?'
    )
    if choose_option():
        return walk()
    return home()


def umbrella():
    print(
        'Вы взяли зонтик и пошли гулять. На улице начался дождь.\n'
        'Вы раскрыли зонтик и пошли дальше. На вашем пути вам встретился промокший котик. Взять котика?'
    )
    if choose_option():
        return cat()
    return no_cat()


def cat():
    print(
        'Вы взяли котика и спрятали его под свое крылышко, чтобы согреть. '
        'Котенок захотел молока. Пойдете за ним в магазин?'
    )
    if choose_option():
        return shop()
    return no_shop()


def shop():
    print(
        'Вы зашли в магазин, купили молока, а затем вернулись домой и стали кормить котика. Конец'
    )


def no_shop():
    print(
        'Вы пошли домой, взяли молоко из холодильника и накормили котика им. Конец.'
    )


def no_cat():
    print(
        'Вы оставили котика мокнуть под дождем.\n'
        'А сами вернулись домой, сделали чай, сели у камина и стали наслаждаться прекрасным вечером.\n'
        'Котик в это время продолжал мерзнуть на улице. Конец.'
    )


def no_umbrella():
    print(
        'Вы пошли гулять без зонтика и на улице начался дождь.'
        'Кажется надо идти домой. Пойти домой?'
    )
    if choose_option():
        return home2()
    return no_home2()


def home2():
    print(
        'Придя домой вы сделали себе горячий чай, сели у камина и стали наслаждаться этим прекрасным вечером.\n'
        'Конец.'
    )
    return


def no_home2():
    print(
        'Вы не пошли домой и продолжили мокнуть под дождем.\n'
        'Вскоре вы замерзли и простудились.\n'
        'Вас забрала скорая и увезла в больницу. Конец.'
    )
    return


def home():
    print(
        'Вы решили никуда не идти и остаться дома. Конец.'
    )
    return


def walk():
    print(
        'Вы готовитесь к выходу. Возьмете ли вы зонтик?'
    )
    if choose_option():
        return umbrella()
    return no_umbrella()


if __name__ == "__main__":
    start()
