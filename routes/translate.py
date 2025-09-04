from flask import Blueprint, request, jsonify
from googletrans import Translator

translate_bp = Blueprint("translate", __name__)
translator = Translator()

@translate_bp.route("/translate", methods=["POST"])
def translate_text():
    try:
        data = request.get_json()
        if not data or "text" not in data or "lang" not in data:
            return jsonify({"error": "Missing text or lang"}), 400

        text = data["text"]
        target_lang = data["lang"]

        
        translated = translator.translate(text, dest=target_lang)

        return jsonify({
            "original_text": text,
            "translated_text": translated.text,
            "target_lang": target_lang
        })
    except Exception as e:
        
        return jsonify({
            "original_text": data.get("text", ""),
            "translated_text": f"[MOCK TRANSLATION in {data.get('lang', '')}]",
            "error": str(e)
        }), 200
