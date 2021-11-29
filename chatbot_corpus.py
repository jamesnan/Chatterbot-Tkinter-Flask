from chatterbot import ChatBot

from chatterbot.trainers import UbuntuCorpusTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging

# # Enable info level logging
# logging.basicConfig(level=logging.INFO)

my_bot = ChatBot(name='Sam',
                 read_only=True,
                 logic_adapters=['chatterbot.logic.MathematicalEvaluation',
                                 'chatterbot.logic.BestMatch'],
                 storage_adapter='chatterbot.storage.SQLStorageAdapter',
                 database_uri='sqlite:///database.sqlite3'
)
                                 
# To trian again with chatterbot.corpus.english, use the code below:
# trainer = ChatterBotCorpusTrainer(my_bot)
# trainer.train('chatterbot.corpus.english')
# trainer.export_for_training('./export.yml')