import random

while True:
    # 入力バリデーション
    while True:
        try:
            min_number = int(input("最小値を入力してください: "))
            max_number = int(input("最大値を入力してください: "))
        except ValueError:
            print("数値を入力してください")
            continue

        if min_number > max_number:
            print("最小値が最大値よりも大きいです。最小値を最大値以下にしてください")
        else:
            break

    # ランダムな数を生成
    random_number = random.randint(min_number, max_number)
    try_count = 5

    for i in range(try_count):
        try:
            answer = int(input("回答を入力してください: "))
        except ValueError:
            print("整数を入力してください")
            continue

        if answer == random_number:
            print("正解！！")
            break
        else:
            print(f"残り試行回数は {try_count - i - 1} 回です")
            if i == try_count - 1:
                print(f"正解は {random_number} でした")

    # ゲーム継続確認
    while True:
        continue_prompt = input("もう一度ゲームをしますか？(y/n): ").lower()
        if continue_prompt == "y":
            break
        elif continue_prompt == "n":
            print("ゲームを終了します")
            exit()
        else:
            print("y または n を入力してください")
