import os
import cassiopeia as cass
from dotenv import load_dotenv

# grab RIOT api key from local env
load_dotenv()
api_key = os.getenv('KEY')

# set cass's key and get a sample summoner
cass.set_riot_api_key(api_key)
summoner = cass.get_summoner(name="TSM Jart", region="NA")

match_history = cass.get_match_history(
    continent=summoner.region.continent,
    puuid=summoner.puuid,
    queue=cass.data.Queue.ranked_solo_fives,
)

champion_id_to_name_mapping = {
    champion.id: champion.name for champion in cass.get_champions(region=summoner.region)
}

for m in match_history:
    c_id = m.participants[summoner].champion.id
    c_name = champion_id_to_name_mapping[c_id]
    print(c_name)