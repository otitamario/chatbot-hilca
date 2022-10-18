# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer


# Create a new instance of a ChatBot
bot = ChatBot(
    'PF Bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///chatbot.sqlite3',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'Desculpa, ainda não sei responder esta pergunta.',
            'maximum_similarity_threshold': 0.90
        }
    ]
)


conversa = ChatterBotCorpusTrainer(bot)
#conversa.train('chatterbot.corpus.portuguese')
conversa.train("chatterbot.corpus.portuguese",
    "chatterbot.corpus.portuguese.greetings",
    "chatterbot.corpus.portuguese.conversations"
)
conversa = ListTrainer(bot)

training_data_passaporte = open('passaporte.txt').read().splitlines()
training_data_armas= open('armas.txt').read().splitlines()
training_data_migracao = open('migracao.txt').read().splitlines()

training_data = training_data_passaporte+training_data_armas+training_data_migracao


conversa.train(training_data)



exit_conditions = (":q", "quit", "exit","-1","sair","tchau","bye")


while True:
    try:
        pergunta = input("Usuário: ")
        if pergunta in exit_conditions:
            break
        
        resposta = bot.get_response(pergunta)
        if float(resposta.confidence) > 0.5:
            print('PF Bot: ', resposta)
        else:
            print('PF Bot: Não entendi')
    except Exception as err:
        print(err)
        pass


'''
while True:
    try:
        pergunta = input("Usuário: ")
        if pergunta in exit_conditions:
            break
        
        resposta = bot.get_response(pergunta)
        if float(resposta.confidence) > 0.2:
            print('PF Bot: ', resposta)
        else:
            print('PF Bot: Ainda não sei responder esta pergunta')

    except Exception as err:
        print(err)
        pass

'''