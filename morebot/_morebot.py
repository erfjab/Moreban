import requests
from typing import Optional, Dict
from config import MOREBOT_LICENSE, MOREBOT_SECRET

class Morebot:
    _base_url = f"https://{MOREBOT_LICENSE}.morebot.top:443/api/{MOREBOT_SECRET}/moreban"
    _timeout = 3

    @classmethod
    def get_inbounds(cls) -> Optional[Dict]:
        response = requests.get(url=f"{cls._base_url}/inbounds", timeout=cls._timeout)
        response.raise_for_status()
        return response.json
