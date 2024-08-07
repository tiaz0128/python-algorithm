class Character:
    def __init__(self, max_health, bandage):
        self.max_health = max_health
        self.current_health = max_health
        self.heal_time, self.heal_per_second, self.bonus_heal = bandage
        self.consecutive_heal_count = 0

    def heal(self):
        self.consecutive_heal_count += 1
        heal_amount = self.heal_per_second
        if self.consecutive_heal_count == self.heal_time:
            heal_amount += self.bonus_heal
            self.consecutive_heal_count = 0
        self.current_health = min(self.current_health + heal_amount, self.max_health)

    def take_damage(self, damage):
        self.current_health -= damage
        self.consecutive_heal_count = 0
        return self.current_health > 0

    def __str__(self):
        return f"Health: {self.current_health}/{self.max_health}"


class BattleSimulation:
    def __init__(self, bandage, max_health, attacks):
        self.character = Character(max_health, bandage)
        self.attacks = attacks
        self.total_time = self.attacks[-1][0]

    def run(self):
        print(f"Time 0: Initial, {self.character}")

        for current_time in range(1, self.total_time + 1):
            attack = next(
                (dmg for time, dmg in self.attacks if time == current_time), None
            )

            if attack:
                if not self.character.take_damage(attack):
                    print(f"Time {current_time}: Character died")
                    return -1
                print(f"Time {current_time}: Attacked (-{attack}), {self.character}")
            else:
                self.character.heal()
                print(f"Time {current_time}: Healed, {self.character}")

        return self.character.current_health


def solution_1(bandage, health, attacks):
    simulation = BattleSimulation(bandage, health, attacks)
    return simulation.run()
