# learning-github
Repository to learn, perform tests, solve exercises and take notes about 'Git' and 'Github'.

## O que é Git e Github?
Git é um software de controle de versão, enquanto o Github é uma plataforma que dispoe de diversos serviços, entre eles, colaboração e gerenciamento de projetos, armazenamento de codigos, entre outros.

# Git
### Comandos úteis
1. #### Configuração do Git
        git config --global user.name "Seu Nome"

        git config --global user.email "seu@email.com"
2. #### Utilização do Git
    | Comandos | descrição |
    --------|--------
    | git init | Inicia um novo repositório no diretório atual. |
    | git clone {remote} | Clona um repositório Git para o diretório atual. |
    | git add . | Adiciona todas as alterações para commit. |
    | git commit -m "msg" | Realiza um commit das alterações adicionadas com a mensagem descritiva.|
    | git status | Exibe as modificações realizadas no repositório. |
    | git log | Exibe o histórico de commits do repositório. |
    | git branch | Lista todas as branchs locais e destaca a atual. |
    | git branch {nome-da-branch} | Cria uma nova branch. |
    | git checkout {nome-da-branch} | Altera para uma branch específica. |
    | git merge {nome-da-branch} | Combina as alterações de uma branch para a branch atual. |
    | git pull | Atualiza o repositório local com as alterações do repositório remoto. |
    | git push {remote} {branch} | Envia os commits para o repositório remoto. |
    | git remote -v | Lista os repositórios remotos configurados |
    | git fetch | Recupera as últimas alterações do repositório remoto, mas não faz merge automaticamente. |
    | git reset {arquivo} | Desfaz as alterações no arquivo. |
    | git rm {arquivo} | Remove o arquivo do repositório e o inclui no próximo commit. |
    | git diff | Mostra as diferenças entre as alterações que ainda não foram adicionadas ao índice. |
    | git remote add {nome-remoto} {URL} | Adiciona um repositório remoto com um nome específico. |

# Github

### Segurança
- ### Métodos de autenticação
    1. #### Usuário e senha:
        Método mais conhecido familiaridade e facilidade, porém, recomenda-se utilizar opções mais seguras.
    2. #### Tokens de acesso pessoal:
        Também conhecidos como PATs (Tokens de Acesso Pessoal), substituem o uso do "Usuário e senha" por um token gerado previamente. Permite específicar quais ações o usuário do token pode realizar.
    3. #### Chaves SSH:
        A autenticação via chave SSH usa um par de chaves criptográficas (privada e pública) para acessar servidores remotos de forma segura, substituindo senhas. A chave privada fica com o usuário, e a pública no servidor, garantindo que apenas o detentor da chave privada possa acessar.
    4. #### Chaves de Implementação:
        Chaves de implementação são chaves digitais que dão acesso a um repositório específico no GitHub. Por padrão, permitem apenas leitura, mas podem ser configuradas para permitir escrita. Funcionam como "chaves especiais" que controlam o que pode ser feito no repositório.

- ### Outras opções
    1. #### Autenticação de dois Fatores (2FA):
        2FA adiciona uma camada extra de segurança além da senha, exigindo um código gerado por um aplicativo ou enviado ao celular. Isso dificulta o acesso não autorizado, protegendo melhor a conta.
    2. #### SSO do SAML:
        O SAML SSO permite login centralizado via um provedor de identidade (como Microsoft Entra ID ou Okta). Após autenticação, o usuário ganha acesso ao GitHub sem usar senhas, facilitando o controle e segurança organizacional.
    3. #### LDAP:
        LDAP é um protocolo que organiza e gerencia o acesso a informações em diretórios corporativos. No GitHub Enterprise, ele facilita o controle centralizado de repositórios usando contas já existentes da empresa.
