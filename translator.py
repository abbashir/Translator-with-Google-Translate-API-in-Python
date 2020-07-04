from googletrans import Translator
import googletrans

translator = Translator()
while True:
    trans_des = input("Enter your primary language code, like \'bn\' for Bengali: ")
    if trans_des in googletrans.LANGUAGES:
        # pseudo code start
        text = input("Enter your speech: ")
        result = translator.translate(text, dest=trans_des)
        print(f'{result.origin} = {result.text}')
        scr_lan = googletrans.LANGUAGES[result.src]
        des_lan = googletrans.LANGUAGES[result.dest]
        print(f'You are translate from \'{scr_lan}\' to \'{des_lan}\'.')
        # pseudo code end
        break
    else:
        print("You entered wrong code.")
        continue
