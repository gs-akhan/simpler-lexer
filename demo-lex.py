import ply.lex as lex

tokens = (
	'WORD',
	'OPENINGTAG',
	'CLOSINGTAG',
	'LANGLE'
	)

myText = """<a><!-- This is ****ing comment,,,
a comment--></a>"""
t_ignore = " "


states = (
		('htmlcomment','exclusive'),
	)

def t_htmlcomment(token):
	r'<!--'
	token.lexer.begin('htmlcomment')

def t_htmlcomment_newline(token) :
	r'\n'
	token.lexer.lineno += 1;

def t_htmlcomment_end(token):
	r'-->'
	token.lexer.begin('INITIAL')

def t_htmlcomment_error(token):
	token.lexer.skip(1)

def t_NEWLINE(token):
	r'\n'
	token.lexer.lineno += 1
	pass

def t_CLOSINGTAG(token):
	r'</'
	return token 

def t_OPENINGTAG(token):
	r'<'
	return token

def t_LANGLE(token):
	r'>'
	return token

def t_WORD(token):
	r'[^<>\n ]+'
	return token

htmlLexer = lex.lex()
htmlLexer.input(myText)

while True:
	tok = htmlLexer.token()
	if not tok:
		break
	print tok

