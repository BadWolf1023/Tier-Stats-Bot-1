import aiohttp

async def fetch(url, headers=None):
    async with aiohttp.ClientSession() as session:
        if headers == None:
            async with session.get(url) as response:
                return await response.read()
        else:
            async with session.get(url, headers=headers) as response:
                return await response.read()

# "bAD W olf" -> "badwolf"
def format_name(name):
    return ''.join(name.split()).lower()

rt_tier_map = {
    't1': "Tier 1",
    't2': "Tier 2",
    't3': "Tier 3",
    't4': "Tier 4",
    't5': "Tier 5",
    't6': "Tier 6",
    't7': "Tier 7",
    'top50': "Top 50",
    '50': "Top 50",
    '1': "Tier 1",
    '2': "Tier 2",
    '3': "Tier 3",
    '4': "Tier 4",
    '5': "Tier 5",
    '6': "Tier 6",
    '7': "Tier 7",
    'tier1': "Tier 1",
    'tier2': "Tier 2",
    'tier3': "Tier 3",
    'tier4': "Tier 4",
    'tier5': "Tier 4",
    'tier6': "Tier 6",
    'tier7': "Tier 7",
    'tier50': "Top 50",
    'tiertop50': "Top 50"
}

ct_tier_map = {
    't1': "Tier 1",
    't2': "Tier 2",
    't3': "Tier 3",
    't4': "Tier 4",
    't5': "Tier 5",
    't6': "Tier 6",
    'top50': "Top 50",
    '50': "Top 50",
    '1': "Tier 1",
    '2': "Tier 2",
    '3': "Tier 3",
    '4': "Tier 4",
    '5': "Tier 5",
    '6': "Tier 6",
    'tier1': "Tier 1",
    'tier2': "Tier 2",
    'tier3': "Tier 3",
    'tier4': "Tier 4",
    'tier5': "Tier 4",
    'tier6': "Tier 6",
    'tier50': "Top 50",
    'tiertop50': "Top 50"
}
