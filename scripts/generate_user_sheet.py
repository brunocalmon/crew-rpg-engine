import json
from pathlib import Path

user_data = {
    "name": "Seraphine Duskveil",
    "race": "Dhampir",
    "class": "Blood Hunter",
    "level": 8,
    "alignment": "Neutral Good",
    "physical_features": {
        "eyes": "silver with red rims",
        "hair": "white and braided",
        "height": "5'9\"",
        "presence": "silent but commanding"
    },
    "attributes": {
        "strength": 14,
        "dexterity": 17,
        "constitution": 15,
        "intelligence": 13,
        "wisdom": 16,
        "charisma": 12
    },
    "skills": [
        "Tracking",
        "Blood magic",
        "Stealth",
        "Insight",
        "Investigation",
        "Survival"
    ],
    "equipment": [
        "Twin daggers of ancestral bone",
        "Blood-sensing amulet",
        "Cloak of midnight mist"
    ],
    "features_and_traits": [
        "Crimson Rite",
        "Blood Curse of Exposure",
        "Darkvision",
        "Hunter's Bane"
    ],
    "topic": "You all seem familiar... I saw these sigils before, marked in crimson on a ruined cathedral wall."
}

# Cria pasta se necessário
user_path = Path("src/resources/users")
user_path.mkdir(parents=True, exist_ok=True)

# Salva ficha do usuário
with open(user_path / "user_sheets.json", "w", encoding="utf-8") as f:
    json.dump(user_data, f, indent=2)

print("✅ User sheet saved in users/user_sheets.json")
