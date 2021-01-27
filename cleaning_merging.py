import pandas as pd

def clean_chimie(download_path):
    # chargement dataframes
    df_chimie = pd.read_csv(download_path + 'Analyses.CSV', delimiter=';')

    # eliminer colonnes superflues
    df_chimie = df_chimie.drop(columns=['CdSupport', 'LbSupport', 'CdFractionAnalysee', 'LbFractionAnalysee', \
                                        'CdPrelevement', 'DateAna', 'HeureAna', 'CdRqAna', 'MnemoRqAna', \
                                        'CdInsituAna', 'LbInsituAna', 'ProfondeurPrel', 'CdDifficulteAna', \
                                        'MnemoDifficulteAna', 'LdAna', 'LqAna', 'LsAna', 'IncertAna', \
                                        'CdMetFractionnement', 'NomMetFractionnement', 'CdMethode', 'NomMethode', \
                                        'RdtExtraction', 'CdMethodeExtraction', 'NomMethodeExtraction', 'CdAccreAna', \
                                        'MnemoAccredAna', 'AgreAna', 'CdStatutAna', 'MnemoStatutAna', 'CdQualAna', \
                                        'LbQualAna', 'CommentairesAna', 'ComResultatAna', 'CdRdd', 'NomRdd', \
                                        'CdProducteur', 'NomProducteur', 'CdPreleveur', 'NomPreleveur', 'CdLaboratoire', \
                                        'NomLaboratoire', 'CdUniteMesure'])

    # garde les lignes associees aux 22 analyses selectionnees / chimie
    df_chimie = df_chimie[(df_chimie.CdParametre == 1302) | (df_chimie.CdParametre == 1301) | \
                          (df_chimie.CdParametre == 1312) | (df_chimie.CdParametre == 1313) | \
                          (df_chimie.CdParametre == 1303) | (df_chimie.CdParametre == 1319) | \
                          (df_chimie.CdParametre == 1335) | (df_chimie.CdParametre == 1311) | \
                          (df_chimie.CdParametre == 1350) | (df_chimie.CdParametre == 1295) | \
                          (df_chimie.CdParametre == 1841) | (df_chimie.CdParametre == 1305) | \
                          (df_chimie.CdParametre == 1433) | (df_chimie.CdParametre == 1347) | \
                          (df_chimie.CdParametre == 1340) | (df_chimie.CdParametre == 1339) | \
                          (df_chimie.CdParametre == 1314) | (df_chimie.CdParametre == 1348) | \
                          (df_chimie.CdParametre == 1342) | (df_chimie.CdParametre == 1436) | \
                          (df_chimie.CdParametre == 1439) | (df_chimie.CdParametre == 1371)]

    # formatage des dates
    df_chimie['DateTime'] = df_chimie['DatePrel'].map(str) + ' ' + df_chimie['HeurePrel'].map(str)
    df_chimie['DateTime'] = pd.to_datetime(df_chimie['DateTime'], format='%Y-%m-%d %H:%M:%S')
    df_chimie = df_chimie.sort_values('DateTime')
    #df_chimie = df_chimie.drop(columns=['DatePrel', 'HeurePrel'])

    # retour du dataframe
    return df_chimie

    # sauvegarde CSV (optionnel)
    # df_chimie.to_csv(download_path + 'chimie_edited.csv', index=False)


def clean_temp(download_path):
    # chargement dataframes
    df_temp = pd.read_csv(download_path + 'AnalysesTemperature.CSV', delimiter=';')

    # eliminer colonnes superflues
    df_temp = df_temp.drop(columns=['CdParametre', 'LbLongParametre', 'CdFractionAnalysee', 'LbFractionAnalysee', \
                                 'CdUniteMesure', 'SymUniteMesure', 'CdStatutAnaTemp', 'MnemoStatutAna', \
                                 'CdQualAnaTemp', 'LbQualAnaTemp', 'CdRdd', 'NomRdd', 'INTProd', 'NomProducteur', \
                                 'INTGest', 'NomGest'])

    # formatage des dates
    df_temp['DateTime'] = df_temp['DtAnaTemp'].map(str) + ' ' + df_temp['HrAnaTemp'].map(str)
    df_temp['DateTime'] = pd.to_datetime(df_temp['DateTime'], format='%Y-%m-%d %H:%M:%S')
    df_temp = df_temp.sort_values('DateTime')
    df_temp = df_temp.drop(columns=['DtAnaTemp', 'HrAnaTemp'])

    # retour du dataframe
    return df_temp

    # sauvegarde CSV (optionnel)
    # df_temp.to_csv('temp_edited.csv', index=False)


# verifications
# for col in df_chimie.columns:
#     print(col)
# print('\n')
# print(df_chimie.dtypes)
# print('\n')
