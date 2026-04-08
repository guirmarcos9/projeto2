import random
import datetime

def menu():
    nome_arq = 'log.txt'
    while True:
        print("\nMenu\n")
        print("1 - Gerar logs")
        print("2 - Analisar logs")
        print("3 - Gerar e Analisar logs")
        print("4 - Sair")

        try:
            opc = int(input("Escolha uma opção: "))
        except:
            print("Entrada invalida.")
            continue

        if opc == 1:
            try:
                qtd = int(input("Quantidade de logs (registros): "))
                gerarArquivo(nome_arq, qtd)
            except:
                print("Entrada invalida.")

        elif opc == 2:
            analisarLogs(nome_arq)

        elif opc == 3:
            try:
                qtd = int(input("Quantidade de logs (registros): "))
                gerarArquivo(nome_arq, qtd)
                analisarLogs(nome_arq)
            except:
                print("Entrada invalida.")

        elif opc == 4:
            print("Até mais")
            break

        else:
            print("Opção Invalida")


def gerarArquivo(nome_arq, qtd):
    with open(nome_arq, 'w', encoding='UTF-8') as arq:
        for i in range(qtd):
            arq.write(montarLog(i) + "\n")
    print('Log gerado')


def montarLog(i):
    data = gerarData(i)
    ip = gerarIp(i)
    recurso = gerarRecurso(i)
    metodo = gerarMetodo(recurso)
    status = gerarStatus(i, recurso)
    tempo = gerarTempo(i, status)
    agente = gerarAgente(i)
    tamanho = gerarTamanho(status, recurso)
    protocolo = gerarProtocolo(i)
    referer = gerarReferer(recurso)

    return '[' + data + '] ' + ip + ' - ' + metodo + ' - ' + str(status) + ' - ' + recurso + ' - ' + str(tempo) + 'ms - ' + str(tamanho) + 'B - ' + protocolo + ' - ' + agente + ' - ' + referer


def gerarData(i):
    base = datetime.datetime.now()
    delta = datetime.timedelta(seconds=i * random.randint(5, 20))
    return (base + delta).strftime('%d/%m/%Y %H:%M:%S')


def gerarIp(i):
    r = random.randint(1, 6)

    # faixa com repetição para simular suspeita
    if i >= 20 and i <= 24:
        return '203.120.45.7'

    # outra faixa para suspeita de bot
    if i >= 70 and i <= 75:
        return '177.88.10.9'

    if r == 1:
        return '192.168.12.1'
    elif r == 2:
        return '192.168.12.3'
    elif r == 3:
        return '192.100.12.3'
    elif r == 4:
        return '192.168.162.3'
    elif r == 5:
        return '192.168.23.3'
    else:
        return '192.168.0.3'


def gerarRecurso(i):
    # força bruta no login
    if i >= 20 and i <= 24:
        return '/login'

    # acesso indevido ao admin
    if i >= 40 and i <= 43:
        return '/admin'

    # páginas inexistentes
    if i >= 50 and i <= 53:
        return '/pagina-inexistente'

    # falha critica
    if i >= 60 and i <= 62:
        return '/api'

    # rotas sensiveis
    if i >= 70 and i <= 71:
        return '/backup'
    elif i >= 72 and i <= 73:
        return '/config'
    elif i >= 74 and i <= 75:
        return '/private'

    r = random.randint(1, 6)

    if r == 1:
        return '/home'
    elif r == 2:
        return '/produtos'
    elif r == 3:
        return '/contato'
    elif r == 4:
        return '/sobre'
    elif r == 5:
        return '/login'
    else:
        return '/carrinho'


def gerarMetodo(recurso):
    if recurso == '/login':
        return 'POST'
    elif recurso == '/api':
        return 'POST'
    else:
        r = random.randint(1, 2)
        if r == 1:
            return 'GET'
        else:
            return 'POST'


def gerarStatus(i, recurso):
    if i >= 20 and i <= 24 and recurso == '/login':
        return 403

    if i >= 40 and i <= 43 and recurso == '/admin':
        return 403

    if i >= 50 and i <= 53:
        return 404

    if i >= 60 and i <= 62:
        return 500

    if i >= 70 and i <= 75:
        if i % 2 == 0:
            return 403
        else:
            return 200

    r = random.randint(1, 10)

    if r <= 7:
        return 200
    elif r == 8:
        return 403
    elif r == 9:
        return 404
    else:
        return 500


def gerarTempo(i, status):
    # degradação de desempenho
    if i == 30:
        return 120
    elif i == 31:
        return 240
    elif i == 32:
        return 390
    elif i == 33:
        return 700

    if status == 500:
        return random.randint(900, 1800)
    elif status == 404:
        return random.randint(150, 500)
    elif status == 403:
        return random.randint(100, 450)
    else:
        return random.randint(80, 850)


def gerarAgente(i):
    if i >= 70 and i <= 72:
        return 'GoogleBot'
    elif i >= 73 and i <= 75:
        return 'CrawlerX'

    r = random.randint(1, 5)

    if r == 1:
        return 'Chrome'
    elif r == 2:
        return 'Firefox'
    elif r == 3:
        return 'Edge'
    elif r == 4:
        return 'Safari'
    else:
        return 'Opera'


def gerarTamanho(status, recurso):
    if status == 404:
        return random.randint(200, 700)
    elif status == 500:
        return random.randint(300, 900)
    elif recurso == '/home':
        return random.randint(1500, 3500)
    elif recurso == '/produtos':
        return random.randint(2500, 6000)
    elif recurso == '/login':
        return random.randint(500, 1200)
    elif recurso == '/admin':
        return random.randint(600, 1400)
    else:
        return random.randint(700, 2500)


def gerarProtocolo(i):
    r = random.randint(1, 3)

    if r == 1:
        return 'HTTP/1.0'
    elif r == 2:
        return 'HTTP/1.1'
    else:
        return 'HTTP/2'


def gerarReferer(recurso):
    if recurso == '/home':
        return '/'
    elif recurso == '/produtos':
        return '/home'
    elif recurso == '/login':
        return '/home'
    elif recurso == '/carrinho':
        return '/produtos'
    else:
        return '/home'


# lê a string até encontrar um marcador
def lerAte(texto, inicio, marcador):
    parte = ''
    i = inicio

    while i < len(texto):
        if texto[i:i + len(marcador)] == marcador:
            return parte, i + len(marcador)
        parte = parte + texto[i]
        i = i + 1

    return parte, i


# extrai os campos sem usar split()
def extrairCampos(linha):
    linha = linha.strip()

    if len(linha) == 0:
        return None

    if linha[0] != '[':
        return None

    posFecha = linha.find(']')

    if posFecha == -1:
        return None

    data = linha[1:posFecha]
    resto = linha[posFecha + 2:]

    ip, pos = lerAte(resto, 0, ' - ')
    metodo, pos = lerAte(resto, pos, ' - ')
    status, pos = lerAte(resto, pos, ' - ')
    recurso, pos = lerAte(resto, pos, ' - ')
    tempo, pos = lerAte(resto, pos, 'ms - ')
    tamanho, pos = lerAte(resto, pos, 'B - ')
    protocolo, pos = lerAte(resto, pos, ' - ')
    agente, pos = lerAte(resto, pos, ' - ')
    referer = resto[pos:]

    return data, ip, metodo, int(status), recurso, int(tempo), int(tamanho), protocolo, agente, referer


def classificarTempo(tempo):
    if tempo < 200:
        return 'rapido'
    elif tempo < 800:
        return 'normal'
    else:
        return 'lento'


def classificarEstado(disponibilidade, falhasCriticas, lentos, suspeitas):
    if falhasCriticas >= 1 or disponibilidade < 70:
        return 'CRÍTICO'
    elif disponibilidade < 85 or lentos >= 10:
        return 'INSTÁVEL'
    elif disponibilidade < 95 or suspeitas > 0:
        return 'ATENÇÃO'
    else:
        return 'SAUDÁVEL'


def contarRecurso(recurso, home, produtos, contato, sobre, login, carrinho, admin, api, pagina, backup, config, private):
    if recurso == '/home':
        home = home + 1
    elif recurso == '/produtos':
        produtos = produtos + 1
    elif recurso == '/contato':
        contato = contato + 1
    elif recurso == '/sobre':
        sobre = sobre + 1
    elif recurso == '/login':
        login = login + 1
    elif recurso == '/carrinho':
        carrinho = carrinho + 1
    elif recurso == '/admin':
        admin = admin + 1
    elif recurso == '/api':
        api = api + 1
    elif recurso == '/pagina-inexistente':
        pagina = pagina + 1
    elif recurso == '/backup':
        backup = backup + 1
    elif recurso == '/config':
        config = config + 1
    elif recurso == '/private':
        private = private + 1

    return home, produtos, contato, sobre, login, carrinho, admin, api, pagina, backup, config, private


def descobrirRecursoMaisAcessado(home, produtos, contato, sobre, login, carrinho, admin, api, pagina, backup, config, private):
    nome = '/home'
    maior = home

    if produtos > maior:
        maior = produtos
        nome = '/produtos'
    if contato > maior:
        maior = contato
        nome = '/contato'
    if sobre > maior:
        maior = sobre
        nome = '/sobre'
    if login > maior:
        maior = login
        nome = '/login'
    if carrinho > maior:
        maior = carrinho
        nome = '/carrinho'
    if admin > maior:
        maior = admin
        nome = '/admin'
    if api > maior:
        maior = api
        nome = '/api'
    if pagina > maior:
        maior = pagina
        nome = '/pagina-inexistente'
    if backup > maior:
        maior = backup
        nome = '/backup'
    if config > maior:
        maior = config
        nome = '/config'
    if private > maior:
        maior = private
        nome = '/private'

    return nome


def contarIp(ip, ip1, c1, ip2, c2, ip3, c3, ip4, c4, ip5, c5, ip6, c6, ip7, c7, ip8, c8):
    if ip == ip1:
        c1 = c1 + 1
    elif ip == ip2:
        c2 = c2 + 1
    elif ip == ip3:
        c3 = c3 + 1
    elif ip == ip4:
        c4 = c4 + 1
    elif ip == ip5:
        c5 = c5 + 1
    elif ip == ip6:
        c6 = c6 + 1
    elif ip == ip7:
        c7 = c7 + 1
    elif ip == ip8:
        c8 = c8 + 1

    return c1, c2, c3, c4, c5, c6, c7, c8


def descobrirIpMaisAtivo(ip1, c1, ip2, c2, ip3, c3, ip4, c4, ip5, c5, ip6, c6, ip7, c7, ip8, c8):
    nome = ip1
    maior = c1

    if c2 > maior:
        maior = c2
        nome = ip2
    if c3 > maior:
        maior = c3
        nome = ip3
    if c4 > maior:
        maior = c4
        nome = ip4
    if c5 > maior:
        maior = c5
        nome = ip5
    if c6 > maior:
        maior = c6
        nome = ip6
    if c7 > maior:
        maior = c7
        nome = ip7
    if c8 > maior:
        maior = c8
        nome = ip8

    return nome


def analisarLogs(nome_arq):
    try:
        arq = open(nome_arq, 'r', encoding='UTF-8')
    except:
        print("Arquivo não encontrado.")
        return

    totalAcessos = 0
    totalSucessos = 0
    totalErros = 0
    totalErrosCriticos = 0

    somaTempos = 0
    maiorTempo = -1
    menorTempo = -1

    qtdRapidos = 0
    qtdNormais = 0
    qtdLentos = 0

    qtd200 = 0
    qtd403 = 0
    qtd404 = 0
    qtd500 = 0

    rHome = 0
    rProdutos = 0
    rContato = 0
    rSobre = 0
    rLogin = 0
    rCarrinho = 0
    rAdmin = 0
    rApi = 0
    rPagina = 0
    rBackup = 0
    rConfig = 0
    rPrivate = 0

    ip1 = '192.168.12.1'
    ip2 = '192.168.12.3'
    ip3 = '192.100.12.3'
    ip4 = '192.168.162.3'
    ip5 = '192.168.23.3'
    ip6 = '192.168.0.3'
    ip7 = '203.120.45.7'
    ip8 = '177.88.10.9'

    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    c6 = 0
    c7 = 0
    c8 = 0

    e1 = 0
    e2 = 0
    e3 = 0
    e4 = 0
    e5 = 0
    e6 = 0
    e7 = 0
    e8 = 0

    eventosForcaBruta = 0
    ultimoIpForcaBruta = 'Nenhum'

    acessosAdminIndevidos = 0
    eventosDegradacao = 0
    eventosFalhaCritica = 0

    suspeitasBot = 0
    ultimoIpSuspeito = 'Nenhum'

    acessosRotasSensiveis = 0
    falhasRotasSensiveis = 0

    ipLoginAnterior = ''
    seqLogin403 = 0

    t1 = -1
    t2 = -1
    t3 = -1
    t4 = -1

    seq500 = 0

    ipAnterior = ''
    seqMesmoIp = 0

    for linha in arq:
        dados = extrairCampos(linha)

        if dados == None:
            continue

        data, ip, metodo, status, recurso, tempo, tamanho, protocolo, agente, referer = dados

        totalAcessos = totalAcessos + 1

        if status == 200:
            totalSucessos = totalSucessos + 1
        else:
            totalErros = totalErros + 1

        if status == 500:
            totalErrosCriticos = totalErrosCriticos + 1

        somaTempos = somaTempos + tempo

        if maiorTempo == -1 or tempo > maiorTempo:
            maiorTempo = tempo

        if menorTempo == -1 or tempo < menorTempo:
            menorTempo = tempo

        classeTempo = classificarTempo(tempo)

        if classeTempo == 'rapido':
            qtdRapidos = qtdRapidos + 1
        elif classeTempo == 'normal':
            qtdNormais = qtdNormais + 1
        else:
            qtdLentos = qtdLentos + 1

        if status == 200:
            qtd200 = qtd200 + 1
        elif status == 403:
            qtd403 = qtd403 + 1
        elif status == 404:
            qtd404 = qtd404 + 1
        elif status == 500:
            qtd500 = qtd500 + 1

        rHome, rProdutos, rContato, rSobre, rLogin, rCarrinho, rAdmin, rApi, rPagina, rBackup, rConfig, rPrivate = contarRecurso(
            recurso, rHome, rProdutos, rContato, rSobre, rLogin, rCarrinho, rAdmin, rApi, rPagina, rBackup, rConfig, rPrivate
        )

        c1, c2, c3, c4, c5, c6, c7, c8 = contarIp(
            ip, ip1, c1, ip2, c2, ip3, c3, ip4, c4, ip5, c5, ip6, c6, ip7, c7, ip8, c8
        )

        if status != 200:
            e1, e2, e3, e4, e5, e6, e7, e8 = contarIp(
                ip, ip1, e1, ip2, e2, ip3, e3, ip4, e4, ip5, e5, ip6, e6, ip7, e7, ip8, e8
            )

        # força bruta
        if recurso == '/login' and status == 403:
            if ip == ipLoginAnterior:
                seqLogin403 = seqLogin403 + 1
            else:
                ipLoginAnterior = ip
                seqLogin403 = 1
        else:
            ipLoginAnterior = ''
            seqLogin403 = 0

        if seqLogin403 == 3:
            eventosForcaBruta = eventosForcaBruta + 1
            ultimoIpForcaBruta = ip

        # acesso indevido ao admin
        if recurso == '/admin' and status != 200:
            acessosAdminIndevidos = acessosAdminIndevidos + 1

        # degradação de desempenho
        t1 = t2
        t2 = t3
        t3 = t4
        t4 = tempo

        if t1 != -1 and t2 != -1 and t3 != -1 and t4 != -1:
            if t1 < t2 and t2 < t3 and t3 < t4:
                eventosDegradacao = eventosDegradacao + 1

        # falha critica
        if status == 500:
            seq500 = seq500 + 1
        else:
            seq500 = 0

        if seq500 == 3:
            eventosFalhaCritica = eventosFalhaCritica + 1

        # bot por user agent
        if 'Bot' in agente or 'Crawler' in agente or 'Spider' in agente:
            suspeitasBot = suspeitasBot + 1
            ultimoIpSuspeito = ip

        # bot por muitas requisições seguidas do mesmo ip
        if ip == ipAnterior:
            seqMesmoIp = seqMesmoIp + 1
        else:
            ipAnterior = ip
            seqMesmoIp = 1

        if seqMesmoIp == 5:
            suspeitasBot = suspeitasBot + 1
            ultimoIpSuspeito = ip

        # rotas sensiveis
        if recurso == '/admin' or recurso == '/backup' or recurso == '/config' or recurso == '/private':
            acessosRotasSensiveis = acessosRotasSensiveis + 1
            if status != 200:
                falhasRotasSensiveis = falhasRotasSensiveis + 1

    arq.close()

    if totalAcessos > 0:
        disponibilidade = (totalSucessos / totalAcessos) * 100
        taxaErro = (totalErros / totalAcessos) * 100
        tempoMedio = somaTempos / totalAcessos
    else:
        disponibilidade = 0
        taxaErro = 0
        tempoMedio = 0

    recursoMaisAcessado = descobrirRecursoMaisAcessado(
        rHome, rProdutos, rContato, rSobre, rLogin, rCarrinho, rAdmin, rApi, rPagina, rBackup, rConfig, rPrivate
    )

    ipMaisAtivo = descobrirIpMaisAtivo(ip1, c1, ip2, c2, ip3, c3, ip4, c4, ip5, c5, ip6, c6, ip7, c7, ip8, c8)
    ipMaisErros = descobrirIpMaisAtivo(ip1, e1, ip2, e2, ip3, e3, ip4, e4, ip5, e5, ip6, e6, ip7, e7, ip8, e8)

    estadoFinal = classificarEstado(disponibilidade, eventosFalhaCritica, qtdLentos, suspeitasBot)

    print("\n========== RELATÓRIO FINAL ==========")
    print("Total de acessos:", totalAcessos)
    print("Total de sucessos:", totalSucessos)
    print("Total de erros:", totalErros)
    print("Total de erros críticos:", totalErrosCriticos)
    print("Disponibilidade do sistema: {:.2f}%".format(disponibilidade))
    print("Taxa de erro: {:.2f}%".format(taxaErro))
    print("Tempo médio de resposta: {:.2f} ms".format(tempoMedio))
    print("Maior tempo de resposta:", maiorTempo, "ms")
    print("Menor tempo de resposta:", menorTempo, "ms")
    print("Quantidade de acessos rápidos:", qtdRapidos)
    print("Quantidade de acessos normais:", qtdNormais)
    print("Quantidade de acessos lentos:", qtdLentos)
    print("Quantidade de status 200:", qtd200)
    print("Quantidade de status 403:", qtd403)
    print("Quantidade de status 404:", qtd404)
    print("Quantidade de status 500:", qtd500)
    print("Recurso mais acessado:", recursoMaisAcessado)
    print("IP mais ativo:", ipMaisAtivo)
    print("IP com mais erros:", ipMaisErros)
    print("Total de eventos de força bruta:", eventosForcaBruta)
    print("Último IP com força bruta detectada:", ultimoIpForcaBruta)
    print("Total de acessos indevidos ao /admin:", acessosAdminIndevidos)
    print("Total de eventos de degradação de desempenho:", eventosDegradacao)
    print("Total de eventos de falha crítica:", eventosFalhaCritica)
    print("Total de suspeitas de bot:", suspeitasBot)
    print("Último IP suspeito de bot:", ultimoIpSuspeito)
    print("Total de acessos a rotas sensíveis:", acessosRotasSensiveis)
    print("Total de falhas em rotas sensíveis:", falhasRotasSensiveis)
    print("Estado final do sistema:", estadoFinal)
    print("====================================")


menu()