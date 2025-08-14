from retab import Retab
import dotenv

dotenv.load_dotenv()

_retab = None

def get_retab() -> Retab: 
    global _retab
    if _retab is None:
        _retab = Retab()
    return _retab
