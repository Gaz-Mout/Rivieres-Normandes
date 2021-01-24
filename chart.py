import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import seaborn as sns

def visual_chimie(df_chimie, date_begin, date_end):
    # input type de données a visualiser
    inp_sandre = True
    while(inp_sandre):
        code_sandre = input('Entrer code sandre (? pour liste des codes): ')
        label_param = ''
        if code_sandre == '?':
            print('\n'
                  '1295: Turbidité Formazine Néphélométrique \n'
                  '1301: Température \n'
                  '1302: Potentiel en Hydrogène \n'
                  '1303: Conductivité éléctrique à 25°C \n'
                  '1305: Matières en suspension \n'
                  '1311: Oxygène dissous \n'
                  '1312: Taux de saturation en O2 \n'
                  "1313: Concentration en masse d'oxygène dissous consommé \n"
                  '1314: Demande Chimique en Oxygène \n'
                  '1319: Azote global \n'
                  '1335: Ammonium \n'
                  '1339: Nitrites \n'
                  '1340: Nitrates \n'
                  '1342: Silicates \n'
                  '1347: Titre alcalimétrique complet \n'
                  '1348: Silice \n'
                  '1350: Phosphore total \n'
                  '1371: Chrome hexavalent \n'
                  '1433: Orthophosphates (PO4) \n'
                  '1436: Phéopigments \n'
                  '1439: Chlorophylle a \n'
                  '1841: Carbone Organique \n')
        elif code_sandre == '1302':
            label_param = 'Potentiel en Hydrogène'
            inp_sandre = False
        elif code_sandre == '1301':
            label_param = 'Température'
            inp_sandre = False
        elif code_sandre == '1313':
            label_param = "Concentration en masse d'oxygène dissous consommé"
            inp_sandre = False
        elif code_sandre == '1312':
            label_param = 'Taux de saturation en O2'
            inp_sandre = False
        elif code_sandre == '1319':
            label_param = 'Azote global'
            inp_sandre = False
        elif code_sandre == '1303':
            label_param = 'Conductivité éléctrique à 25°C'
            inp_sandre = False
        elif code_sandre == '1311':
            label_param = 'Oxygène dissous'
            inp_sandre = False
        elif code_sandre == '1295':
            label_param = 'Turbidité Formazine Néphélométrique'
            inp_sandre = False
        elif code_sandre == '1350':
            label_param = 'Phosphore total'
            inp_sandre = False
        elif code_sandre == '1841':
            label_param = 'Carbone Organique'
            inp_sandre = False
        elif code_sandre == '1305':
            label_param = 'Matières en suspension'
            inp_sandre = False
        elif code_sandre == '1347':
            label_param = 'Titre alcalimétrique complet'
            inp_sandre = False
        elif code_sandre == '1433':
            label_param = 'Orthophosphates (PO4)'
            inp_sandre = False
        elif code_sandre == '1335':
            label_param = 'Ammonium'
            inp_sandre = False
        elif code_sandre == '1371':
            label_param = 'Chrome hexavalent'
            inp_sandre = False
        elif code_sandre == '1439':
            label_param = 'Chlorophylle a'
            inp_sandre = False
        elif code_sandre == '1436':
            label_param = 'Phéopigments'
            inp_sandre = False
        elif code_sandre == '1314':
            label_param = 'Demande Chimique en Oxygène'
            inp_sandre = False
        elif code_sandre == '1342':
            label_param = 'Silicates'
            inp_sandre = False
        elif code_sandre == '1348':
            label_param = 'Silice'
            inp_sandre = False
        elif code_sandre == '1340':
            label_param = 'Nitrates'
            inp_sandre = False
        elif code_sandre == '1339':
            label_param = 'Nitrites'
            inp_sandre = False
        else:
             print('Mauvais code')

    print('Données: ' + label_param)
    code_sandre = int(code_sandre)
    df_chimie_graph = df_chimie[(df_chimie.CdParametre == code_sandre)]
    # df_chimie_graph['DateTime'] = pd.to_datetime(df_chimie_graph['DateTime'], format='%Y-%m-%d %H:%M:%S')


    # creation graph simple
    # sns.set_theme()
    # graph = sns.barplot(x='DateTime', y='RsAna', data=df_chimie_graph, color='blue')

    # for name, data in df_chimie.groupby('LbLongParamètre'):
    #     plt.plot(data['DateTime'], data['RsAna'], label=name)

    # creation graph animée
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=20, metadata=dict(artist='Me'), bitrate=1800)

    ytitle = str(df_chimie_graph.iloc[6].SymUniteMesure)
    fig = plt.figure(figsize=(10, 6))
    # plt.xlim(date_begin, date_end)
    # plt.ylim(np.min(df_chimie_graph.RsAna)[0], np.max(df_chimie_graph.RsAna)[0])
    plt.title('Evolution paramètre chimique', fontsize=20)

    def animate(i):
        data = df_chimie_graph.iloc[:int(i+1)]
        graph = sns.barplot(y='RsAna', x='DatePrel', data=data, color="blue")
        graph.tick_params(labelsize=8, rotation=45)
        plt.xlabel('Date', fontsize=20)
        plt.ylabel(ytitle, fontsize=20)

    ani = matplotlib.animation.FuncAnimation(fig, animate, frames=200, repeat=True)

    # visualisation et resumé des données
    plt.show()
    print(df_chimie_graph.RsAna.describe())
