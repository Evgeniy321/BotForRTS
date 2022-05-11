token = open('token.txt', encoding='utf-8')
tokenread = token.read()
id = open('clientid.txt', encoding='utf-8')
idread = token.read()
prefix = open('prefix.txt', encoding='utf-8')
prefixread = token.read()
name = open('botname.txt', encoding='utf-8')
nameread = token.read()
settings = {
    'token': tokenread, #Токен бота
    'bot': nameread, #Имя бота
    'id': idread, #ClientID бота
    'prefix': prefixread #Префикс Пример ($rocketcoins)
}