from services.CrytoService import CryptoService
from models.ScratchCards import ScratchCards
from models.Challenges import Challenges
from models.Store import Store
from datetime import datetime

class ScratchCardService:
    cryptoService = CryptoService()
    
    def addChallenges(self,payload):
        scratchCards = ScratchCards(date = datetime.now(), 
                                    seri = self.cryptoService.encrypt(payload['seri']),
                                    code = self.cryptoService.encrypt(payload['code']),
                                    )
        scratchCards.save()

        challenges = Challenges(date = datetime.now(),
                                challenge = payload['challenge']
                                )
        challenges.save()

        store = Store(date = datetime.now(),
                      challenge = challenges,
                      scratch_card = scratchCards
        )
        store.save()

