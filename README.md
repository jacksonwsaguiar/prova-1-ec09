# Simulação do Protocolo MQTT para prova

Este projeto tem como objetivo simular a comunicação MQTT utilizando dados ficticios simulados provenientes de um freezer e uma geladeira. A aplicação gera mensagens MQTT a partir dos dados e as envia para um broker MQTT.

## Requisitos

- Python 3.x
- Biblioteca `paho-mqtt` (instalável via `pip install paho-mqtt`)

## Estrutura do Projeto

- `publisher.py`: Módulo contendo funções para iniciar o cliente MQTT e enviar mensagens para um tópico MQTT.
- `subscriber.py`: Módulo contendo funções se inscrever em um topico MQTT e receber mensagens de um tópico MQTT.

## Execução

1. Execute o script do publisher `publisher.py` para iniciar a simulação.
    ```
    python3 publisher.py
    ```
2. Execute o script `subscriber.py` para iniciar o subscriber e receber mensagens.
    ```
    python3 subscriber.py
    ```
## Tests
Testes unitarios de casos para publisher e subscriber, onde são testados items como validação de envio, recebimento de mensagem, alerts e qos.

### Para executar

1. Execute o script de teste do publisher:
    ```
    pytest test_publisher.py
    ```
2. Execute o script de teste do subscriber:
    ```
    pytest test_subscriber.py
    ```
3. Execute o script de teste dos alerts do subscriber:
    ```
    pytest test_subscriber_alert.py
    ```
