from googletrans import Translator

translator = Translator()

def translate(text_in,lang_in,lang_out):
    text_out = translator.translate(text_in, src=lang_in, dest=lang_out).text
    return text_out
