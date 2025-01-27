def count_words(message:str, ref):
	count = 0
	for word in message.split(' '):
		count += (word in ref)
	return count

def decode(message:str, alph_len:int=26):
	with open('../shared/resources/words.txt') as wordfile:
		words = {word.strip('\n') for word in wordfile.readlines()}
	scores = {shift:count_words(encode(message, shift, alph_len), words) for shift in range(26)}
	best = max(scores, key=scores.get)
	return encode(message, best, alph_len), best

def encode(message:str, shift:int, alph_len:int=26):
	ords = [ord(c)-ord('a') if c != ' ' else -1 for c in [*message]]
	shifted = [ord('a')+(c+shift)%alph_len if c != -1 else -1 for c in ords]
	return "".join([chr(c) if c != -1 else ' ' for c in shifted])

if __name__ == '__main__':
	import sys
	if len(sys.argv) == 4:
		import random
		seed = int(sys.argv[3])
		random.seed(seed)
		messages = ['hello world', 'coding club', 'you get the idea', 'good bye']
		content = r" \\[0.7in] \noindent{}".join([encode(message, random.randint(0,25)) for message in messages])
	else:
		message = sys.argv[1]
		shift = int(sys.argv[2])
		content = encode(message, shift)
	latex_content = r"""
	\documentclass{article}
	\usepackage[utf8]{inputenc}
	\title{Encoded Messages}
	\author{Coding Club | Sheet 1, seed """ + str(seed) + r"""}
	
	\begin{document}
	
	\maketitle

	\noindent{}Decode these messages:

	\noindent{}""" + content + r"""
	\end{document}
	"""
	with open('encoded_message.tex', mode='w') as f_out:
		f_out.write(latex_content)