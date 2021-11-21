# variaveis que auxiliam no controle e tratamento de erros
__status = None
__description = None


def report(status: int, description: str):
    global __status
    global __description

    __status = status
    __description = description


# gera o status de retorno da função, ao usalo o status e sua descrição sao redefinidos
def status():
    global __status
    global __description

    if __status:
        tmp = __status
        __status = None
        __description = None
        return tmp
    else:
        return None


# gera o status e sua descrição de retorno da função, ao usalo o status e sua descrição sao redefinidos
def description():
    global __status
    global __description

    if __status:
        tmp = __status
        __status = None
        tmp_d = __description
        __description = None
        return tmp, tmp_d
    else:
        return None
