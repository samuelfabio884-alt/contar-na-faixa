# Otimização de receptor Android TV via ADB

Projeto pessoal de suporte técnico: analisar um receptor de satélite e IPTV com Android TV 10 que apresentava travamentos e desativar, de forma segura e reversível, serviços que não eram necessários, sem afetar o funcionamento da operadora.

## Resumo

| Item | Detalhe |
|---|---|
| Aparelho | Receptor híbrido satélite/IPTV, fabricante Technicolor, modelo SKR02 |
| Sistema | Android TV 10 (SDK 29) |
| Conexão | ADB pela rede local, sem root |
| Ferramenta | Cliente ADB em Python do projeto open source [CleanYourTV](https://github.com/Gathin23/cleanyourtv) (licença MIT) |
| Computador | MacBook, na mesma rede do receptor |
| Resultado | 8 pacotes desativados, canais ao vivo funcionando e leve melhora de desempenho |

## Objetivo

Reduzir os travamentos do aparelho, liberando recursos, com três regras de segurança definidas antes de começar:

1. **Não mexer em nada da operadora.** Nenhum pacote com `sky`, `iptv`, `satellite`, `dvb`, `linear`, `epg` ou `tuner` no nome poderia ser desativado. Por precaução, também ficaram de fora os pacotes de acesso condicional, middleware e drivers de decodificação.
2. **Não desativar o assistente de configuração** (`setupwraith`), para não correr o risco de perder as credenciais de rede.
3. **Sem root.** Tudo feito com `pm disable-user`, que pode ser desfeito a qualquer momento.

## Passo a passo

### 1. Conexão e identificação

Com a depuração USB ativada no receptor, o `--probe` do cliente ADB retornou o modelo, a versão do Android e a confirmação de que a chave RSA foi aceita (`ro.adb.secure = 1`).

### 2. Backup antes de qualquer mudança

Foram salvos três arquivos com o estado original:

- lista completa de pacotes instalados (103);
- lista de pacotes já desativados de fábrica (nenhum);
- lista de pacotes ativos.

Com isso, o estado original pode ser restaurado com precisão.

### 3. Levantamento e análise

- **Memória:** 2,8 GB de RAM no total, com cerca de 1,2 GB livres em uso normal.
- **Armazenamento:** 34% usado, com 7 GB livres. Disco cheio foi descartado como causa.
- **Tela inicial:** confirmei, com `resolve-activity`, que a Home é o app da operadora, então o launcher não foi trocado.
- **Maiores consumidores de RAM:** Google Play Services, Netflix, app da operadora e recomendações do Google.

Os pacotes foram separados em três grupos: **protegidos**, **incertos** e **seguros para desativar**.

### 4. Desativação (apenas após aprovação)

Foram desativados 8 pacotes, todos do Google e sem relação com a operadora:

| Pacote | Função |
|---|---|
| `com.google.android.play.games` | Play Games |
| `com.google.android.youtube.tvmusic` | YouTube Music |
| `com.google.android.videos` | Google Play Filmes |
| `com.google.android.feedback` | Envio de feedback |
| `com.google.android.tv.bugreportsender` | Relatório de erros |
| `com.google.android.backdrop` | Protetor de tela |
| `com.google.android.tvrecommendations` | Recomendações do Google na tela inicial (~71 MB de RAM) |
| `com.google.android.apps.mediashell` | Chromecast integrado (não utilizado) |

A busca por voz (`katniss`) foi mantida, por ser uma função usada no controle.

### 5. Validação

- A lista de pacotes desativados continha exatamente os 8 itens autorizados.
- A tela inicial continuou sendo a da operadora.
- Teste manual: canais ao vivo por satélite, guia de programação e aplicativos de streaming funcionando normalmente após reiniciar o aparelho.

## Como reverter

Com a lista dos pacotes salva em um arquivo `desativados_autorizados.txt`:

```
while read p; do tools/venv/bin/python -I tools/tv.py "pm enable $p"; done < desativados_autorizados.txt
```

Como o backup mostrou que nada estava desativado antes, isso devolve o aparelho ao estado original.

## O que aprendi

- Usar ADB e `pm` para listar, analisar e desativar pacotes sem root.
- Fazer backup e plano de reversão antes de alterar um sistema.
- Ler a saída de `dumpsys meminfo` para identificar processos que consomem memória.
- Que otimizar nem sempre significa remover muita coisa: neste caso, o ganho veio de poucos itens e de uma análise cuidadosa do que não podia ser mexido.
- Medir antes de agir: as leituras de RAM e de armazenamento ajudaram a descartar causas e a definir o que valia desativar.

## Aviso

Este projeto documenta uma experiência pessoal em um aparelho próprio. Os pacotes e os resultados podem ser diferentes em outros modelos. Faça backup antes de qualquer alteração, e não use esta lista como regra geral. Não tenho vínculo com a operadora, com o fabricante ou com o projeto CleanYourTV.
