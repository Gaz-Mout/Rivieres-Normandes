from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import os.path
import time
from zipfile import ZipFile

def scraping(download_path, code_massedeau, date_begin, date_end):
    # setup selenium
    profile = webdriver.FirefoxProfile()
    profile.set_preference('browser.download.folderList', 2) # custom location
    profile.set_preference('browser.download.panel.shown', False)
    profile.set_preference('browser.download.dir', download_path)
    profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/zip')
    options = webdriver.FirefoxOptions()
    options.add_argument('-headless')
    driver = webdriver.Firefox(firefox_profile=profile, options=options)
    driver.get(f"http://www.naiades.eaufrance.fr/"
               f"acces-donnees#/physicochimie/resultats/"
               f"?debut=01-01-{date_begin}&fin=31-12-{date_end}&masses-deau={code_massedeau}")

    # telechargement
    try:
        print('\n'
              'search...')
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "exportCsv"))
        )
    finally:
        elem = driver.find_element_by_id('exportCsv')
        elem.click()

    # verification telechargement
    no_file = True
    while(no_file):
        print(('downloading...'))
        time.sleep(5)
        if os.path.isfile(download_path + '/naiades_export.zip'):
            print('done! \n')
            no_file = False
        else:
            print('downloading...')
            time.sleep(5)
    driver.close()

    # extraction donnees
    with ZipFile(download_path + '/naiades_export.zip', 'r') as naiade_zip:
        naiade_zip.extractall(path=download_path)
    os.remove(download_path + '/naiades_export.zip')
