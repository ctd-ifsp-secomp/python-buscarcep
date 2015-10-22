# -*- coding: utf-8 -*-
#
# buscarcep.py
# 
# Exemplo de uso do webservice http://buscarcep.com.br/
# Para Python 2.7
# 
# Daniel Gonçalves <daniel@base4.com.br>
#

import httplib
import sys
import urllib
import urlparse


def localizar_pelo_cep(numero):
    """
    Localiza endereços pelo número do CEP retornando o conteúdo da requisição.
    Este exemplo solicita o retorno como uma string. Para localizar pelo
    endereço, incluindo outros atributos (como tipo de logradouro ou bairro),
    basta modificar o dicionário ``params``.
    """

    params = urllib.urlencode(dict(
            formato='xml',
            chave='Chave_Gratuita_BuscarCep',
            identificador='CLIENTE1',
            cep=numero))


    conn = httplib.HTTPSConnection('buscarcep.com.br')
    conn.connect()
    conn.request('GET', '/?{0}'.format(params))

    response = conn.getresponse()

    if response.status == httplib.OK:
        return response.read()
    else:
        raise httplib.HTTPException('{0:d} {1}'.format(
                response.status,
                httplib.responses[response.status]))


def tratar_resposta_xml(conteudo):
    import xml.dom.minidom
    xml = xml.dom.minidom.parseString(conteudo)
    print xml.toprettyxml()


def tratar_resposta_string(conteudo):
    from pprint import pprint
    dicionario = urlparse.parse_qs(conteudo.replace('\n', ''))
    pprint(dicionario)


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print 'Uso: python buscarcep.py NUMEROCEP\n'
        sys.exit(1)

    conteudo = localizar_pelo_cep(sys.argv[1])

    # se estiver trabalhando com retornos em xml...
    tratar_resposta_xml(conteudo)

    # se estiver trabalhando com retornos em string...
    # tratar_resposta_string(conteudo)
