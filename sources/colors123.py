class colors:
  INCORRECT = '\033[31m' # red
  CORRECT = '\033[32m' # green
  WARNING = '\033[33m'#'\033[33m' # orange
  BLUE = '\033[35m' # blue
  UNDERLINED = '\033[4m'
  BOLD = '\033[1m'
  END = '\033[0m' # simple text (stop colourful text)
# print smth with color :print(f"{colors.INCORRECT}Error : Test message !{colors.END}") 