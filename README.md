# klecrack 🔐

**klecrack** é uma ferramenta simples de cracking de hashes escrita em Python, criada com fins **educacionais**, **CTFs** e **laboratórios de segurança**.
Ela utiliza wordlists para tentar descobrir a senha original de hashes no formato `crypt` do Linux, suportando algoritmos como **MD5**, **SHA-256** e **SHA-512**.

---

## 🚀 Funcionalidades

- Suporte a hashes:
  - `$1$` → MD5-crypt
  - `$5$` → SHA-256-crypt
  - `$6$` → SHA-512-crypt
- Leitura de wordlist personalizada
- Barra de progresso com porcentagem (`tqdm`)
- Detecção automática de algoritmo e salt
- Saída simples e direta

---

## 🛠️ Requisitos

- Python 3.8+
- Dependências:
  - `passlib`
  - `tqdm`

Instale as dependências com:
```bash
pip install passlib tqdm
```
---

## 📦 Uso

```bash
python klecrack.py wordlist.txt
```
Após executar, o programa solicitará o hash completo:

```bash
Digite o Hash completo: $6$salt$hash...
```
Se a senha estiver na wordlist, o resultado será exibido:

```bash
[+] Senha encontrada: senha123
```
Caso contrário:

```bash
[-] Senha não encontrada nessa wordlist!
```

---

## 🧪 Exemplo de hash compatível

Hashes no formato padrão do Linux (/etc/shadow):

```bash
$6$abc123$9Wqv5qv1zq9H3nKQKJ0...
```

---

## ⚠️ Aviso Legal

Esta ferramenta foi desenvolvida exclusivamente para fins educacionais, como:
 - Estudos de segurança
 - Capture The Flag (CTF)
 - Testes em ambientes controlados
 - Aprendizado de hashing e autenticação

❌ Não utilize esta ferramenta para acessar sistemas sem autorização.
O autor não se responsabiliza pelo uso indevido.

---

## 📚 Objetivo do Projeto

O objetivo do klecrack é:
 - Entender como funcionam hashes crypt
 - Aprender sobre salts e algoritmos de hashing
 - Reproduzir, de forma didática, o funcionamento básico de ferramentas como john

Não é um substituto para ferramentas profissionais como John the Ripper ou Hashcat.

---

## 👤 Autor

Desenvolvido por kl3bj
profissional de segurança ofensiva, CTFs e engenharia de software.

---

## ⭐ Contribuições

Sugestões, melhorias e estudos são bem-vindos!
Sinta-se à vontade para abrir issues ou pull requests.
