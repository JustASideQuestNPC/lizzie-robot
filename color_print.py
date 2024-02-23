from typing import Literal

COLOR_CODES = {
  'black': 30,
  'red': 31,
  'green': 32,
  'yellow': 33,
  'blue': 34,
  'magenta': 35,
  'cyan': 36,
  'white': 37,
  'bright black': 90,
  'bright red': 91,
  'bright green': 92,
  'bright yellow': 93,
  'bright blue': 94,
  'bright magenta': 95,
  'bright cyan': 96,
  'bright white': 97
}

# just a little bit of type hinting...just a little bit.
def color_print(text: str,
                foreground: Literal['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan',
                                    'white', 'bright black', 'bright red', 'bright green',
                                    'bright yellow', 'bright blue', 'bright magenta', 'bright cyan',
                                    'bright white', ''] = '',
                background: Literal['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan',
                                    'white', 'bright black', 'bright red', 'bright green',
                                    'bright yellow', 'bright blue', 'bright magenta', 'bright cyan',
                                    'bright white', ''] = '',
                end='\n', bold: bool=False, italic: bool=False, underline: bool=False) -> None:
  
  if foreground not in COLOR_CODES and foreground != '':
    raise ValueError(("Invalid foreground color passed to color_print()! (expected a color or '', "
                     f"received '{foreground}')"))
  
  if background not in COLOR_CODES and background != '':
    raise ValueError(("Invalid background color passed to color_print()! (expected a color or '', "
                     f"received '{background}')")) 
  
  options = []
  if bold:
    options.append(1)
  if italic:
    options.append(3)
  if underline:
    options.append(4)
  if foreground != '':
    options.append(COLOR_CODES[foreground])
  if background != '':
    options.append(COLOR_CODES[background] + 10)

  print(f'\x1b[{";".join([str(i) for i in options])}m{text}\x1b[0m', end=end)