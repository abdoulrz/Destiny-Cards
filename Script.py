
zodiac_quotes = {
    'Aries': "Humm, you are of the adventurous type.",
    'Taurus': "Ah, a lover of comfort and stability.",
    'Gemini': "Curious and adaptable, aren't you?",
    'Cancer': "Sensitive and nurturing, I see.",
    'Leo': "Bold and charismatic, as expected.",
    'Virgo': "Practical and analytical, a true Virgo.",
    'Libra': "Balanced and harmonious, just like a Libra.",
    'Scorpio': "Intense and passionate, as always.",
    'Sagittarius': "Free-spirited and philosophical.",
    'Capricorn': "Disciplined and ambitious, naturally.",
    'Aquarius': "Innovative and independent, how unique.",
    'Pisces': "Compassionate and artistic, a dreamer."
}

age_destiny_messages = {
    '18-40': "Your destiny is bright, but tread carefully. Opportunities and challenges await.",
    '41-60': "Mysteries await you. Secrets will unravel in unexpected ways.",
    '61+': "Nostalgia fills the air. Cherished memories come to life."
}


number_meanings = {
    1: "A new beginning is on the horizon.",
    2: "Balance and harmony are key.",
    3: "Creativity will guide your path.",
    4: "Stability and structure are important.",
    5: "Change is inevitable, embrace it.",
    6: "Love and care surround you.",
    7: "Wisdom and introspection are your allies.",
    8: "Power and success are within reach.",
    9: "Completion and fulfillment are near.",
    10: "A cycle is ending, prepare for the next.",
    11: "Intuition and insight will lead you.",
    12: "Growth and expansion are ahead.",
    13: "Transformation is at hand."
}

season_messages = {
    'Spring': "A time of renewal and growth.",
    'Summer': "Energy and vibrancy fill the air.",
    'Autumn': "Reflection and change are upon you.",
    'Winter': "Rest and introspection are needed."
}


final_message = ''
first = input('Zodiac Sign Please:')

def generate_message(user_input):
    final_message = ''

    if user_input in zodiac_quotes:
      print(zodiac_quotes[first])
      second = input('Age Please:')
      if int(second) <= 18 and int(second) <=40:
        final_message += str(age_destiny_messages['18-40'])
        final_message += ' '
      elif int(second) <= 41 and int(second) <=60:
        final_message += age_destiny_messages['41-60']
        final_message += ' '
      elif int(second) <= 61 and int(second) <=100:
        final_message += age_destiny_messages['61+']
        final_message += ' '
      else: 
        print('Destiny is out of your reach!')
      third = input('Choose a number between 1 and 13:')
      if int(third) in number_meanings:
        final_message += number_meanings[int(third)]
        final_message += ' '
        fourth = input('Any favorite Season:')
        if fourth in season_messages:
          final_message += season_messages[fourth]
          print(final_message)
        else:
          final_message += '!'
          print(final_message)

    
generate_message(first)