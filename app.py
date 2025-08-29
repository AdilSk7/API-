from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# === PUT YOUR DETAILS HERE ===
FULL_NAME_LOWER_SNAKE = "shaik_adil"   # change to your name
DOB_DDMMYYYY = "01012000"              # change to your dob ddmmyyyy
EMAIL = "example@vitap.ac.in"
ROLL_NUMBER = "ABCD1234"
# ==============================

def extract_letters(s: str):
    # all alphabetic characters from the token, in order
    return re.findall(r"[A-Za-z]", s)

def alternating_caps_reverse(letters):
    # letters: list of single-letter strings, original order
    out = []
    upper = True
    for ch in letters[::-1]:
        out.append(ch.upper() if upper else ch.lower())
        upper = not upper
    return "".join(out)

def is_digits(s: str) -> bool:
    return bool(re.fullmatch(r"\d+", s))

def is_alpha(s: str) -> bool:
    return bool(re.fullmatch(r"[A-Za-z]+", s))

@app.route("/bfhl", methods=["POST"])
def bfhl():
    try:
        payload = request.get_json(force=True)
        data = payload.get("data", None)
        if not isinstance(data, list):
            raise ValueError("`data` must be a list")

        even_numbers, odd_numbers = [], []
        alphabets, special_characters = [], []
        letters_all = []
        total = 0

        for item in data:
            s = str(item)

            # collect letters for the alternating-caps-reverse string (from ALL tokens)
            letters_all.extend(extract_letters(s))

            if is_digits(s):
                # keep numbers as strings in outputs
                if int(s) % 2 == 0:
                    even_numbers.append(s)
                else:
                    odd_numbers.append(s)
                total += int(s)
            elif is_alpha(s):
                alphabets.append(s.upper())
            elif len(s) == 1 and not s.isalnum():
                # single non-alnum character
                special_characters.append(s)
            else:
                # any mixed token: capture its special characters individually
                for ch in s:
                    if not ch.isalnum():
                        special_characters.append(ch)

        resp = {
            "is_success": True,  # required status flag
            "user_id": f"{FULL_NAME_LOWER_SNAKE}_{DOB_DDMMYYYY}",  # full_name_ddmmyyyy, lowercase
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,                   # pure alphabetic tokens, uppercased
            "special_characters": special_characters, # non-alphanumeric characters
            "sum": str(total),                        # return sum as a string
            "concat_string": alternating_caps_reverse(letters_all)
        }
        return jsonify(resp), 200  # success must be 200
    except Exception as e:
        return jsonify({
            "is_success": False,
            "error": str(e)
        }), 400

if __name__ == "__main__":
    # Local dev server
    app.run(host="0.0.0.0", port=5000)
