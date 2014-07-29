HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = "\033[1m"

DILUIR = "\033[2m"
CURSIVA = "\033[3m"
SUBRAYADO = "\033[4m"
PARPADEO_LENTO = "\033[5m"
PARPADEO_RAPIDO = "\033[6m"
NEGATIVO = "\033[7m"

CYAN = '\033[96m'
DARKCYAN = '\033[36m'
UNDERLINE = '\033[4m'

equivalente  = {'azul': OKBLUE, 'verde': OKGREEN, 'amarillo': WARNING, 'rojo':FAIL, 'cian': CYAN}

def disable():
    HEADER = ''
    OKBLUE = ''
    OKGREEN = ''
    WARNING = ''
    FAIL = ''
    ENDC = ''

def infog( msg):
    print BOLD + OKGREEN + msg + ENDC

def info( msg):
    print BOLD + OKBLUE + msg + ENDC

def warn( msg):
    print BOLD + WARNING + msg + ENDC

def negativo_cursiva( msg):
	print NEGATIVO + CURSIVA + msg + ENDC

def cyan(msg):
	print CYAN + msg + ENDC

def err( msg):
    print BOLD + FAIL + msg + ENDC

def buildColor(key, msg):
	if equivalente.get(key, False):
		return equivalente.get(key) + msg + ENDC
	else:
		return msg