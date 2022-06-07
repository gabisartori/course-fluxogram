curso = 'CCO'

sem1 = {
    'EEL5105': [curso],
    'INE5401': [curso],
    'INE5402': [curso],
    'INE5403': [curso],
    'MTM3110': [curso]
}

sem2 = {
    'INE5404': ['INE5402'],
    'INE5406': ['EEL5105'],
    'INE5407': [curso],
    'MTM3111': [curso],
    'MTM3120': ['MTM3110'],
    'MTM3121': [curso]
}

sem3 = {
    'INE5202': ['MTM3120', 'MTM3111'],
    'INE5408': ['INE5404'],
    'INE5410': ['INE5404'],
    'INE5411': ['INE5406'],
    'MTM3131': ['MTM3120', 'MTM3121']
}

sem4 = {
    'INE5412': ['INE5410', 'INE5411'],
    'INE5413': ['INE5403', 'INE5408'],
    'INE5414': ['INE5404'],
    'INE5415': ['INE5403', 'INE5408'],
    'INE5416': ['INE5408'],
    'INE5417': ['INE5408']
}

sem5 = {
    'INE5405': ['MTM3110'],
    'INE5418': ['INE5412', 'INE5414'],
    'INE5419': ['5417'],
    'INE5420': ['INE5408', 'MTM3120', 'MTM3121'],
    'INE5421': ['INE5415'],
    'INE5422': ['5414']
}

sem6 = {
    'INE5423': ['INE5408'],
    'INE5424': ['INE5412'],
    'INE5425': ['INE5202', 'INE5405'],
    'INE5426': ['INE5421'],
    'INE5427': ['INE5417'],
    'INE5430': ['INE5405', 'INE5413', 'INE5416'],
    'TCC0': ['INE5417']
}

sem7 = {
    'INE5428': ['INE5407'],
    'INE5429': ['INE5403', 'INE5414'],
    'INE5432': ['INE5423'],
    'TCC1': ['INE5427', 'TCC0']
}

sem8 = {
    'TCC2': ['TCC1']
}

sems = sem1 | sem2 | sem3 | sem4 | sem5 | sem6 | sem7 | sem8