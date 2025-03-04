from flask import Flask, render_template, jsonify
import json
import random

app = Flask(__name__)

# 음식 데이터 불러오는 함수
def load_foods():
    with open('foods.json', 'r', encoding='utf-8') as file:
        return json.load(file)
    
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['GET'])
def recommand():
    foods = load_foods()
    random_food = random.choice(foods) # 랜덤 음식
    return jsonify({'food': random_food})

def main():
    app.run(debug=True, port=80)

if __name__=='__main__':
    main()