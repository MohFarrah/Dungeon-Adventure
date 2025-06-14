from typing import Dict, Any, Optional
from .GameDatabase import CharacterStats

class MockCharacterStats(CharacterStats):
    def __init__(self):
        self.mock_hero_stats = {
            'knight': {
                'hero_type': 'knight',
                'max_health': 375,
                'health': 375,
                'speed': 50,
                'damage': 55,
                'attack_range': 80,
                'attack_speed': 1.3,
                'special_cooldown': 10.0,
                'defense': 20,
                'critical_chance': 0.1,
                'critical_damage': 1.5
            },
            'archer': {
                'hero_type': 'archer',
                'max_health': 150,
                'health': 150,
                'speed': 40,
                'damage': 40,
                'attack_range': 120,
                'attack_speed': 2.0,
                'special_cooldown': 8.0,
                'defense': 10,
                'critical_chance': 0.15,
                'critical_damage': 2.0
            },
            'cleric': {
                'hero_type': 'cleric',
                'max_health': 250,
                'health': 250,
                'speed': 35,
                'damage': 85,
                'attack_range': 60,
                'attack_speed': 0.75,
                'special_cooldown': 12.0,
                'defense': 15,
                'critical_chance': 0.05,
                'critical_damage': 1.8
            }
        }
    def get_hero_stats(self, hero_type: str) -> Optional[Dict[str, Any]]:
        return self.mock_hero_stats.get(hero_type)
    def get_monster_stats(self, monster_type: str) -> Optional[Dict[str, Any]]:
        return None
    def get_hero_animation_data(self, hero_type: str, animation_state: str) -> Optional[Dict[str, Any]]:
        return None
    def get_monster_animation_data(self, monster_type: str, animation_state: str) -> Optional[Dict[str, Any]]:
        return None
    def get_all_hero_animations(self, hero_type: str) -> Dict[str, Dict[str, Any]]:
        return {}
    def get_all_monster_animations(self, monster_type: str) -> Dict[str, Dict[str, Any]]:
        return {}
