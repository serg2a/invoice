def generate_text(sett:dict, summ):
    """Generate mail for text """

    text = ' Здравствуйте %s. \n\n' % sett['persone']
    text += '    Итог:\t%s : %s %s \n' % (sett['corp'], summ, sett['money'])
    text += '    Подробно:\t%s \n\n' % sett['www']
    text += '--\n С Уважением \n    %s' % sett['actor']

    return text
