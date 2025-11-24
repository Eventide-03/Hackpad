# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
# The Press, Release, and Tap imports are now part of the Macro module, 
# but are kept here for clarity (although only KC.Macro is strictly needed now)
from kmk.modules.macros import Press, Release, Tap, Macros 

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Define your pins here!
PINS = [board.D3, board.D4, board.D2, board.D1] 

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Define the macros for Mac productivity shortcuts:

# 1. KC.LCMD + KC.LBRC (Command + Left Bracket) for Previous Tab (Works in Chrome, Safari, etc.)
#    NOTE: The Mac standard is Command-Shift-[ for previous and Command-Shift-] for next. 
#    We will use the Mac standard to ensure cross-application compatibility.

PREV_TAB = KC.Macro(
    Press(KC.LCMD, KC.RSFT), # Press Command and Right Shift
    Tap(KC.LBRC),            # Tap Left Bracket ([)
    Release(KC.LCMD, KC.RSFT)  # Release Command and Right Shift
)

# 2. KC.LCMD + KC.RBRC (Command + Right Bracket) for Next Tab
NEXT_TAB = KC.Macro(
    Press(KC.LCMD, KC.RSFT), # Press Command and Right Shift
    Tap(KC.RBRC),            # Tap Right Bracket (])
    Release(KC.LCMD, KC.RSFT)  # Release Command and Right Shift
)

# 3. KC.LCTRL + KC.RIGHT (Control + Right Arrow) for Next Workstation/Space
NEXT_SPACE = KC.Macro(
    Press(KC.LCTRL),       # Press Control
    Tap(KC.RIGHT),         # Tap Right Arrow
    Release(KC.LCTRL)      # Release Control
)

# 4. KC.LCTRL + KC.LEFT (Control + Left Arrow) for Previous Workstation/Space
PREV_SPACE = KC.Macro(
    Press(KC.LCTRL),       # Press Control
    Tap(KC.LEFT),          # Tap Left Arrow
    Release(KC.LCTRL)      # Release Control
)

# Here you define the buttons corresponding to the pins
# The order corresponds directly to the PINS list: [D3, D4, D2, D1]
keyboard.keymap = [
    [PREV_TAB, NEXT_TAB, NEXT_SPACE, PREV_SPACE]
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()
