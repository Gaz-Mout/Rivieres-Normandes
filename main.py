import shutil
import numpy as np
from scrap import *
from cleaning_merging import *
from chart import *

# titre
print('\n'
      'LES RIVIERES NORMANDES'
      '\n')

# effacer dossier temporaire
currdir = os.getcwd()
download_path = currdir + '/truite_donwload/'
shutil.rmtree(download_path, ignore_errors=True)

# programmme
running = True
while(running):
    # creation dossier rivieres
    os.mkdir(download_path)

    # input de la zone a visualiser
    inp_riv = True
    label_riv = ''
    code_massedeau = ''
    while (inp_riv):
        riviere = input('Riviere (1: Orne, 2: Sélune, 3: Touques): ')
        if riviere == '1':
            label_riv = 'Orne'
            inp_riv = False
            code_massedeau = 'HR307'
        elif riviere == '2':
            label_riv = 'Sélune'
            inp_riv = False
            code_massedeau = 'HR351'
        elif riviere == '3':
            label_riv = 'Touques'
            inp_riv = False
            code_massedeau = 'HR275'
        else:
            print('mauvais code')

    # input des dates a visualiser
    inp_date_begin = True
    inp_date_end = True
    dates_list = np.arange(2000, 2021)
    while (inp_date_begin):
        date_begin = input('Date de début (2000-2020): ')
        date_begin = int(date_begin)
        if date_begin in dates_list:
            inp_date_begin = False
    while (inp_date_end):
        date_end = input('Date de fin (2000-2020): ')
        date_end = int(date_end)
        if ((date_end >= date_begin) and (date_end in dates_list)):
            inp_date_end = False

    # appel fonction de scrap
    scraping(download_path, code_massedeau, date_begin, date_end)

    # appel fonction nettoyage de données
    df_chimie = clean_chimie(download_path)

    # appel fonction visualisation
    visual_chimie(df_chimie, date_begin, date_end)

    # relancer ou terminer le programme
    print('\n')
    inp_quit = True
    while (inp_quit):
        quit = input('Quitter (y/n): ')
        if quit == 'n':
            inp_quit = False
            shutil.rmtree(download_path)
            print('\n')
        elif quit == 'y':
            inp_quit = False
            running = False
            shutil.rmtree(download_path)
            print('cya !')