import json
from pathlib import Path

agent_sheets = {
    "Alaric": {
        "name": "Alaric, the Exiled Blood Prince",
        "race": "Vampire",
        "class": "Warlock (Hexblade)",
        "level": 10,
        "alignment": "Chaotic Neutral",
        "background": "Once heir to a vampiric kingdom, now a wandering drunk exiled after a tragic betrayal",
        "physical_description": {
            "age": "412",
            "gender": "Male",
            "height": "6'4\"",
            "eyes": "blood-red",
            "hair": "long silver",
            "skin": "ashen pale"
        },
        "attributes": {
            "strength": 16,
            "dexterity": 14,
            "constitution": 18,
            "intelligence": 10,
            "wisdom": 8,
            "charisma": 20
        },
        "skills": ["Intimidation", "Deception", "Arcana", "Athletics"],
        "equipment": ["Broken Crown", "Hexblade (shattered)", "Bottomless Flask of Bloodwine"],
        "features_and_traits": ["Darkvision", "Fey Presence", "Pact of the Blade", "Eldritch Invocations"],
        "motive": "Drinks to forget. Remembers to suffer. Leads because no one else dares."
    },
    "Stitch": {
        "name": "Stitch, the Bound Servant",
        "race": "Undead",
        "class": "Artificer (Fleshcrafter)",
        "level": 6,
        "alignment": "Neutral",
        "background": "Once a rogue necromancer, now magically bound to serve the Blood Prince for eternity",
        "physical_description": {
            "age": "???",
            "gender": "Male",
            "height": "5'5\"",
            "eyes": "sewn shut, magical vision",
            "hair": "none",
            "skin": "stitched patchwork"
        },
        "attributes": {
            "strength": 10,
            "dexterity": 14,
            "constitution": 16,
            "intelligence": 18,
            "wisdom": 12,
            "charisma": 8
        },
        "skills": ["Arcana", "Medicine", "Insight", "Sleight of Hand"],
        "equipment": ["Bone Toolkit", "Binding Sigils", "Wand of Mending"],
        "features_and_traits": ["Magical Servitude", "Necrotech Infusion", "Pain Memory"],
        "motive": "Forced into loyalty, but learned comfort in the chaos of service."
    },
    "Ravella": {
        "name": "Ravella, the Blood-Bard",
        "race": "Half-Vampire (Banshee)",
        "class": "Bard (College of Whispers)",
        "level": 9,
        "alignment": "Neutral Evil",
        "background": "A once famous bard who sold her voice for vampiric power, now haunting taverns with melody and secrets",
        "physical_description": {
            "age": "204",
            "gender": "Female",
            "height": "5'8\"",
            "eyes": "violet glowing",
            "hair": "jet black, floating unnaturally",
            "skin": "white with a ghostly hue"
        },
        "attributes": {
            "strength": 9,
            "dexterity": 16,
            "constitution": 14,
            "intelligence": 13,
            "wisdom": 12,
            "charisma": 20
        },
        "skills": ["Performance", "Persuasion", "History", "Deception"],
        "equipment": ["Violin of Wailing Souls", "Scrolls of Forgotten Ballads", "Bloodstained Lute"],
        "features_and_traits": ["Bardic Inspiration", "Mantle of Whispers", "Hypnotic Performance"],
        "motive": "To immortalize tragedy in song and extract truth through melody."
    },
    "Arkwin": {
        "name": "Arkwin, the Arcane Chronicler",
        "race": "Elf",
        "class": "Wizard (Lorekeeper)",
        "level": 7,
        "alignment": "Lawful Neutral",
        "background": "A scholar exiled from elven lands for his obsession with forbidden vampire lore",
        "physical_description": {
            "age": "187",
            "gender": "Male",
            "height": "6'0\"",
            "eyes": "green with gold flecks",
            "hair": "white tied-back",
            "skin": "bronzed"
        },
        "attributes": {
            "strength": 9,
            "dexterity": 12,
            "constitution": 13,
            "intelligence": 19,
            "wisdom": 14,
            "charisma": 11
        },
        "skills": ["Investigation", "Arcana", "History", "Insight"],
        "equipment": ["Runed Grimoire", "Spectral Quill", "Sapphire Monocle"],
        "features_and_traits": ["Ritual Casting", "Arcane Recovery", "Keen Mind"],
        "motive": "Truth is sacred, even if buried in blood."
    },
    "Bellatrix": {
        "name": "Bellatrix, the Shadow Witch",
        "race": "Human",
        "class": "Sorcerer (Shadow Magic)",
        "level": 8,
        "alignment": "Chaotic Neutral",
        "background": "Born during a lunar eclipse, marked by fate to unveil cursed secrets.",
        "physical_description": {
            "age": "38 (sustained magically, does not age)",
            "gender": "Female",
            "height": "5'10\"",
            "eyes": "solid black",
            "hair": "void-like, flows on its own",
            "skin": "ashen"
        },
        "attributes": {
            "strength": 8,
            "dexterity": 13,
            "constitution": 15,
            "intelligence": 14,
            "wisdom": 12,
            "charisma": 19
        },
        "skills": ["Religion", "Arcana", "Perception", "Deception"],
        "equipment": ["Wand of Null Stars", "Tome of Eclipse", "Veil of Shadows"],
        "features_and_traits": ["Sorcery Points", "Darkvision", "Strength of the Grave", "Eyes of the Dark"],
        "motive": "She speaks to the void, hoping it never answers back."
    }
}

# Salvar JSON
agents_path = Path("src/resources/agents")
agents_path.mkdir(parents=True, exist_ok=True)
with open(agents_path / "agent_sheets.json", "w", encoding="utf-8") as f:
    json.dump(agent_sheets, f, indent=2)

print("✅ Agent sheets saved in agents/agent_sheets.json")
