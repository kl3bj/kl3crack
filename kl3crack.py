#Crack de hash

from tqdm import tqdm
from passlib.context import CryptContext
import sys

#Forçando o usuario a selecionar a wordlist
if len(sys.argv) != 2:
    print(f"Modo de uso da ferramenta: python {sys.argv[0]} wordlist.txt")
    sys.exit(1)

wordlist = sys.argv[1]
ha = input("Digite o Hash completo: ")

ctx = CryptContext(
    schemes=["md5_crypt", "sha256_crypt", "sha512_crypt"],
    deprecated="auto"
)

found = False

total = sum(1 for _ in open(wordlist, "r", errors="ignore"))

#Lendo cada linha da wordlist e mostrando na tela
with open(wordlist, "r", encoding="utf-8", errors="ignore") as f:
	for linha in tqdm(f, total=total, desc="Crackeando hash", colour='green'):
		senha = linha.strip()

		if ctx.verify(senha,ha):
			print(f"[+] Senha encontrada: {senha}")
			found = True
			break

if not found:
	print("[-] Senha não encontrada nessa wordlist!")
