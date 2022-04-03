# Torillic
> Magic is distilled laziness

This theme, named after the fantasy setting of [Dungeons & Dragons](https://www.dndbeyond.com/), is designed with tabletop RPG players in mind. The theme allows beautiful HTML exports designed to look like a professionally made tabletop resource, whilst remaining easy to edit in code view and in small windows, thanks to CSS media queries.

Torillic v2 is the second incarnation of the Torillic theme, you can download older versions [here](https://github.com/TEParsons/torillic/releases).

## Usage Guide

Like all Typora themes, Torillic uses [markdown syntax](https://www.markdownguide.org/basic-syntax/), but here's a few tips and tricks for getting the most out of this theme:

- Using `> blockquotes` will create a green box like the ones used in 5e stat blocks
- In full page view, content is arranged into two columns - however, `# heading 1` and `---` (horizontal line) elements span both columns so can be used as separators
- The heading with a yellow line underneath (you know the one) is `#### heading 4`
- Actions in 5e stat blocks are generally formatted like so:
```markdown
***Name.*** *Attack Type:* +[modifier] to hit, reach [reach] ft., [n targets] target(s). *Hit:* [approx damage] ([n dice]d[die size] + [additional]) [damage type] damage.
```
- For an example of a full stat sheet in Torillic, check out the markdown below the screenshots.
- Ultimately, it's yours to play with, so feel free to completely ignore this advice and lay things out however works for your capaign!

## Screenshots

[![full-width](https://github.com/typora/typora-theme-gallery/raw/gh-pages/media/theme/torillic/full.png)](https://github.com/typora/typora-theme-gallery/raw/gh-pages/media/theme/torillic/full.png)

[![thin](https://github.com/typora/typora-theme-gallery/raw/gh-pages/media/theme/torillic/thin.png)](https://github.com/typora/typora-theme-gallery/raw/gh-pages/media/theme/torillic/thin.png)

[![code](https://github.com/typora/typora-theme-gallery/raw/gh-pages/media/theme/torillic/code.png)](https://github.com/typora/typora-theme-gallery/raw/gh-pages/media/theme/torillic/code.png)

The above screenshots were all created using the following markdown:

```markdown
# Adult Blue Dragon

*Huge dragon, lawful evil*

> **Armor Class** 19 (Natural Armor)
> **Hit Points** 225 (18d12 + 108)
> **Speed** 40 ft., burrow 30 ft., fly 80 ft.
>
> | STR  | DEX  | CON  | INT  | WIS  | CHA  |
> |------|------|------|------|------|------|
> | 25   | 10   | 23   | 16   | 15   | 19   |
> | (+7) | (+0) | (+6) | (+3) | (+2) | (+4) |
> 
> **Saving Throws** DEX +5, CON +11, WIS +7, CHA +9
> **Skills** [Perception](https://www.dndbeyond.com/compendium/rules/basic-rules/using-ability-scores#Perception) +12, [Stealth](https://www.dndbeyond.com/compendium/rules/basic-rules/using-ability-scores#Stealth) +5
> **Damage Immunities** Lightning
> **Senses** [Blindsight](https://www.dndbeyond.com/compendium/rules/basic-rules/monsters#Blindsight) 60 ft., [Darkvision](https://www.dndbeyond.com/compendium/rules/basic-rules/monsters#Darkvision) 120 ft., Passive Perception 22
> **Languages** Common, Draconic
> **Challenge** 16 (15,000 XP)

![Ancient Blue Dragon - Monsters - Archives of Nethys: Pathfinder ...](https://2e.aonprd.com/Images/Monsters/DragonBlue_AncientBlueDragon.png)

---

***Legendary Resistance (3/Day).*** If the dragon fails a saving throw, it can choose to succeed instead.

#### Actions

***Multiattack.*** The dragon can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claws.

***Bite.*** *Melee Weapon Attack:* +12 to hit, reach 10 ft., one target. *Hit:* 18 (2d10 + 7) piercing damage plus 5 (1d10) lightning damage.

***Claw.*** *Melee Weapon Attack:* +12 to hit, reach 5 ft., one target. *Hit:* 14 (2d6 + 7) slashing damage.

***Tail.*** *Melee Weapon Attack:* +12 to hit, reach 15 ft., one target. *Hit:* 16 (2d8 + 7) bludgeoning damage.

***Frightful Presence.*** Each creature of the dragon's choice that is within 120 feet of the dragon and aware of it must succeed on a DC 17 Wisdom saving throw or become [frightened](https://www.dndbeyond.com/compendium/rules/basic-rules/appendix-a-conditions#Frightened) for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If a creature's saving throw is successful or the effect ends for it, the creature is immune to the dragon's Frightful Presence for the next 24 hours.

***Lightning Breath (Recharge 5–6).*** The dragon exhales lightning in a 90-­foot line that is 5 feet wide. Each creature in that line must make a DC 19 Dexterity saving throw, taking 66 (12d10) lightning damage on a failed save, or half as much damage on a successful one.

#### Legendary Actions

The dragon can take 3 legendary actions, choosing from the options below. Only one legendary action option can be used at a time and only at the end of another creature's turn. The dragon regains spent legendary actions at the start of its turn.

***Detect.*** The dragon makes a Wisdom ([Perception](https://www.dndbeyond.com/compendium/rules/basic-rules/using-ability-scores#Perception)) check.

***Tail Attack.*** The dragon makes a tail attack.

***Wing Attack (Costs 2 Actions).*** The dragon beats its wings. Each creature within 10 feet of the dragon must succeed on a DC 20 Dexterity saving throw or take 14 (2d6 + 7) bludgeoning damage and be knocked [prone](https://www.dndbeyond.com/compendium/rules/basic-rules/appendix-a-conditions#Prone). The dragon can then fly up to half its flying speed.
```